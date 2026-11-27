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
    def fixture(self, version='0.6.3'):
        revision = 'a' * 40
        expected = dict(schema=1, source_repository=release.SOURCE, version=version, revision=revision)
        names = [f'WWW-POSIM-{version}-windows-x64.exe', f'www-posim_{version}_amd64.deb',
                 f'WWW-POSIM-{version}-macos-arm64.dmg', f'WWW-POSIM-{version}-macos-engine.part001']
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

    def test_0620_missing_installed_suite_blocks_both_publishers(self):
        from release_payload import verify
        data, draft, remote, receipts = self.fixture('0.6.20')
        with self.assertRaisesRegex(ValueError, 'installed mission'):
            release.validate(data, draft, remote, receipts)
        with tempfile.TemporaryDirectory() as folder, self.assertRaisesRegex(ValueError, 'installed mission'):
            verify(data, folder)

    def mission_fixture(self):
        data, draft, remote, receipts = self.fixture('0.6.20')
        dmg = data['dmg_acceptance']
        dmg.update(mounted_executable_sha256='c'*64, app_executable_sha256='c'*64)
        data['posim_revision'] = 'f'*40
        rows = [dict(outcome=outcome, **{
            key: hashlib.sha256(f'{index}:{key}'.encode()).hexdigest()
            for key in ('mission_sha256', 'nonce_sha256', 'samples_sha256')})
            for index, outcome in enumerate(('completed', 'completed', 'dvl_stale'))]
        receipt = dict(policy='bluerov2-installed-2p1-v1', version='0.6.20', platform='macos-arm64',
                       source_revision=data['source_revision'], posim_revision=data['posim_revision'],
                       dmg=dmg['dmg'], dmg_sha256=dmg['sha256'], launcher_sha256='c'*64,
                       engine_sha256=dmg['engine_sha256'], suite_sha256='b'*64, trials=rows)
        return data, draft, remote, receipts, receipt

    def test_0620_direct_and_legacy_match_candidate_and_distinct_trial_commitments(self):
        from release_payload import MISSION_RECEIPT, verify
        for problem in ('', 'source_revision', 'posim_revision', 'dmg_sha256', 'launcher_sha256', 'engine_sha256',
                        'suite_sha256', 'nonce_sha256', 'samples_sha256', 'mission_sha256', 'outcome', 'digest'):
            with self.subTest(problem=problem), tempfile.TemporaryDirectory() as folder:
                data, draft, remote, receipts, receipt = self.mission_fixture()
                if problem in ('nonce_sha256', 'mission_sha256', 'samples_sha256'):
                    receipt['trials'][1][problem] = receipt['trials'][0][problem]
                elif problem == 'outcome':
                    receipt['trials'][2][problem] = 'completed'
                elif problem and problem != 'digest':
                    receipt[problem] = '0'*40 if problem.endswith('revision') else 'wrong'
                content = json.dumps(receipt).encode()
                sha = hashlib.sha256(content if problem != 'digest' else b'different').hexdigest()
                data['assets'].append(dict(name=MISSION_RECEIPT, bytes=len(content), sha256=sha, asset_id=99))
                data['upload_verification']['asset_ids'].append(99)
                remote[MISSION_RECEIPT] = dict(id=99, name=MISSION_RECEIPT, size=len(content), state='uploaded',
                                               digest='sha256:' + sha)
                receipts[MISSION_RECEIPT] = content
                (Path(folder)/MISSION_RECEIPT).write_bytes(content)
                data.pop('native_payload')
                data['dmg_acceptance']['mounted_diagnostic']['native_engine_included'] = True
                if problem:
                    with self.assertRaisesRegex(ValueError, 'installed mission'):
                        release.validate(data, draft, remote, receipts)
                    with self.assertRaisesRegex(ValueError, 'installed mission'):
                        verify(data, folder)
                else:
                    self.assertEqual(release.validate(data, draft, remote, receipts)['revision'], data['source_revision'])
                    verify(data, folder)

    def test_submerged_mission_exception_is_explicit_and_limited_to_0618(self):
        data, draft, remote, receipts = self.fixture('0.6.18')
        native = data['native_acceptance']
        native['autopilot_robots'] = ['wamv']
        with self.assertRaisesRegex(ValueError, 'Native/installed Mac acceptance'):
            release.validate(data, draft, remote, receipts)
        native['waived_tests'] = ['bluerov2_submerged_mission']
        self.assertEqual(release.validate(data, draft, remote, receipts)['version'], '0.6.18')
        data, draft, remote, receipts = self.fixture('0.6.19')
        data['native_acceptance'].update(native)
        with self.assertRaisesRegex(ValueError, 'Native/installed Mac acceptance'):
            release.validate(data, draft, remote, receipts)

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
        data, draft, remote, receipts, mission = self.mission_fixture()
        mission_content = json.dumps(mission).encode()
        name = release.MISSION_RECEIPT
        sha = hashlib.sha256(mission_content).hexdigest()
        data['assets'].append(dict(name=name, bytes=len(mission_content), sha256=sha, asset_id=99))
        data['upload_verification']['asset_ids'].append(99)
        remote[name] = dict(name=name, state='uploaded', id=99, size=len(mission_content), digest='sha256:' + sha)
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
            content = mission_content if name == release.MISSION_RECEIPT else json.dumps(receipts[kind]).encode()
            Path(args[args.index('--output') + 1]).write_bytes(content)
        with tempfile.TemporaryDirectory() as folder, patch.object(release, 'api', side_effect=api), \
                patch.object(release, 'command', side_effect=command), patch.dict(os.environ,
                dict(GITHUB_REPOSITORY=release.REPOSITORY, GITHUB_REF='refs/heads/main')):
            previous = Path.cwd();os.chdir(folder)
            try:
                release.publish(data, 'Tested release')
                release.publish(data, 'Tested release')
                self.assertEqual(Path('release-tag.txt').read_text(), 'v0.6.20')
                mission_content += b' '
                with self.assertRaisesRegex(ValueError, 'receipt bytes differ'):
                    release.publish(data, 'Changed receipt')
            finally:os.chdir(previous)
        self.assertEqual(len(calls), 1)
        self.assertTrue(all(name == release.MISSION_RECEIPT or (name.startswith('release-build-') and name.endswith('.json')) for name in downloads))
        self.assertEqual(downloads.count(release.MISSION_RECEIPT), 3)


if __name__ == '__main__':
    unittest.main()
