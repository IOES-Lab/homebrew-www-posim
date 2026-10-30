import copy
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import direct_release as release


class DirectPublication(unittest.TestCase):
    def fixture(self):
        version, revision = '0.6.3', 'a' * 40
        expected = dict(schema=1, source_repository=release.SOURCE, version=version, revision=revision)
        names = ['WWW-POSIM-0.6.3-windows-x64.exe', 'www-posim_0.6.3_amd64.deb',
                 'WWW-POSIM-0.6.3-macos-arm64.dmg', 'WWW-POSIM-0.6.3-macos-engine.part001']
        values, remote = [], {}
        for index, name in enumerate(names):
            value = dict(name=name, bytes=100 + index, sha256=hashlib.sha256(name.encode()).hexdigest(), asset_id=index + 10)
            values.append(value)
            remote[name] = dict(id=value['asset_id'], name=name, size=value['bytes'],
                                state='uploaded', digest='sha256:' + value['sha256'])
        engine = 'e' * 64
        part = dict(values[-1]);part.pop('asset_id')
        part['url'] = f'https://github.com/{release.REPOSITORY}/releases/download/v{version}/{part["name"]}'
        data = dict(tag='v' + version, source_revision=revision, draft_release_id=1, assets=values,
            native_acceptance=dict(passed=True, original_build_prefix_hidden=True, autopilot_robots=['bluerov2', 'wamv'],
                local_ros_displacement_m=3, supervisor_exit_code=0, shutdown_faults=[], tested_archive_sha256=engine),
            dmg_acceptance=dict(passed=True, mounted_signature_verified=True, staged_signature_verified=True,
                mounted_version='WWW-POSIM ' + version, engine_sha256=engine, dmg=names[2], sha256=values[2]['sha256'],
                mounted_diagnostic=dict(engine_mode='native-metal', native_engine_download=True, publishable=True)),
            native_payload=dict(schema=1, sha256=engine, bytes=part['bytes'], parts=[part]),
            upload_verification=dict(source_revision=revision, native_payload_sha256=engine,
                                     asset_ids=[value['asset_id'] for value in values]))
        receipts = {kind: dict(expected, kind=kind, files=[values[index]]) for index, kind in enumerate(('windows', 'linux'))}
        receipts['images'] = dict(expected, kind='images', files=[], proofs={
            'pushed-' + kind + '.json': dict(revision=revision, tag='image:' + version + '-amd64',
                image_id='sha256:' + 'b'*64, registry_index='sha256:' + 'b'*64) for kind in ('engine', 'web')})
        draft = dict(id=1, tag_name='v' + version, draft=True, prerelease=False,
                     body=release.MARKER + json.dumps(expected) + ' -->')
        return data, draft, remote, receipts

    def test_matching_platforms_and_native_acceptance_pass_without_relaying_installers(self):
        data, draft, remote, receipts = self.fixture()
        self.assertEqual(release.validate(data, draft, remote, receipts)['revision'], 'a' * 40)

    def test_corruption_mixed_sources_missing_parts_and_development_builds_block(self):
        for problem in ('digest', 'size', 'source', 'platform', 'missing_part', 'part_url', 'development', 'signature', 'native', 'image', 'byte_verification'):
            with self.subTest(problem=problem):
                data, draft, remote, receipts = self.fixture()
                if problem == 'digest':remote[data['assets'][0]['name']]['digest'] = 'sha256:' + 'f' * 64
                elif problem == 'size':remote[data['assets'][0]['name']]['size'] += 1
                elif problem == 'source':receipts['windows']['revision'] = 'f' * 40
                elif problem == 'platform':receipts['linux']['files'] = []
                elif problem == 'missing_part':data['assets'].pop()
                elif problem == 'part_url':data['native_payload']['parts'][0]['url'] = 'https://elsewhere.invalid/engine'
                elif problem == 'development':data['dmg_acceptance']['mounted_diagnostic']['publishable'] = False
                elif problem == 'signature':data['dmg_acceptance']['mounted_signature_verified'] = False
                elif problem == 'native':data['native_acceptance']['local_ros_displacement_m'] = 0
                elif problem == 'image':receipts['images']['proofs']['pushed-web.json']['registry_index'] = 'sha256:' + 'f'*64
                else:data['upload_verification']['native_payload_sha256'] = 'f' * 64
                with self.assertRaises(ValueError):release.validate(data, draft, remote, receipts)

    def test_finalizer_downloads_only_receipts_and_promotion_retry_is_noop(self):
        data, draft, remote, receipts = self.fixture()
        for index, (kind, receipt) in enumerate(receipts.items()):
            content = json.dumps(receipt).encode()
            remote['release-build-' + kind + '.json'] = dict(name='release-build-' + kind + '.json', id=index + 100,
                state='uploaded', size=len(content), digest='sha256:' + hashlib.sha256(content).hexdigest())
        calls, downloads = [], []
        def api(path, method='GET', payload=None):
            if method == 'PATCH':
                calls.append(payload);draft.update(payload);return draft
            if '/assets?' in path:return list(remote.values())
            if path.endswith('/latest'):return dict(tag_name='v0.6.1')
            return copy.deepcopy(draft)
        def command(*args, **kwargs):
            self.assertEqual(args[:2], ('release', 'download'))
            name = args[args.index('--pattern') + 1]
            downloads.append(name)
            kind = name.removeprefix('release-build-').removesuffix('.json')
            Path(args[args.index('--output') + 1]).write_bytes(json.dumps(receipts[kind]).encode())
        with tempfile.TemporaryDirectory() as folder, patch.object(release, 'api', side_effect=api), \
                patch.object(release, 'command', side_effect=command), patch.dict(os.environ,
                dict(GITHUB_REPOSITORY=release.REPOSITORY, GITHUB_REF='refs/heads/main')):
            previous = Path.cwd();os.chdir(folder)
            try:
                release.publish(data, 'Tested release')
                release.publish(data, 'Tested release')
                self.assertEqual(Path('release-tag.txt').read_text(), 'v0.6.3')
            finally:os.chdir(previous)
        self.assertEqual(len(calls), 1)
        self.assertTrue(all(name.startswith('release-build-') and name.endswith('.json') for name in downloads))
        self.assertEqual(len(downloads), 6)


if __name__ == '__main__':
    unittest.main()
