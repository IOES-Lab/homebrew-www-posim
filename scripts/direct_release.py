"""Promote directly uploaded assets after all platform and native checks pass."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

REPOSITORY = 'IOES-Lab/homebrew-www-posim'
SOURCE = 'IOES-Lab/WWW-POSIM'
MARKER = '<!-- www-posim-release: '


def command(*args, payload=None):
    result = subprocess.run(['gh', *args], capture_output=True,
        input=None if payload is None else json.dumps(payload).encode(), check=True, timeout=120)
    return result.stdout


def api(path, method='GET', payload=None):
    args = ['api', path, '--method', method]
    if payload is not None:
        args += ['--input', '-']
    return json.loads(command(*args, payload=payload))


def filename(name):
    if not isinstance(name, str) or not re.fullmatch(r'[A-Za-z0-9_.-]+', name) or name in ('.', '..'):
        raise ValueError('Invalid asset filename')
    return name


def same_asset(asset, value):
    filename(value['name'])
    if type(value['bytes']) is not int or not 0 < value['bytes'] < 2 * 1024**3:
        return False
    return (asset.get('id') == value.get('asset_id') and asset.get('name') == value['name']
            and asset.get('state') == 'uploaded' and asset.get('size') == value['bytes']
            and asset.get('digest') == 'sha256:' + value['sha256'])


def validate_acceptance(data):
    native, proof = data['native_acceptance'], data['dmg_acceptance']
    diagnostic = proof['mounted_diagnostic']
    if not (native.get('passed') is True and native.get('original_build_prefix_hidden') is True
            and native.get('autopilot_robots') == ['bluerov2', 'wamv']
            and native.get('local_ros_displacement_m', 0) >= 2
            and native.get('supervisor_exit_code') == 0 and not native.get('shutdown_faults')
            and proof.get('passed') is True and proof.get('mounted_signature_verified') is True
            and proof.get('staged_signature_verified') is True
            and proof.get('mounted_version') == 'WWW-POSIM ' + data['tag'][1:]
            and diagnostic.get('engine_mode') == 'native-metal'
            and diagnostic.get('publishable') is not False
            and diagnostic.get('edition', 'release') == 'release'
            and (diagnostic.get('native_engine_included') is True or diagnostic.get('native_engine_download') is True)
            and proof.get('engine_sha256') == native.get('tested_archive_sha256')):
        raise ValueError('Native/installed Mac acceptance has not passed')
    values = {entry['name']: entry for entry in data['assets']}
    dmg = values.get(proof['dmg'])
    if not dmg or dmg['sha256'] != proof['sha256']:
        raise ValueError('DMG does not match its installed acceptance')
    payload = data.get('native_payload')
    if payload is None:
        if diagnostic.get('native_engine_included') is not True:
            raise ValueError('Bootstrap installer requires its verified engine parts')
        return
    parts = payload.get('parts')
    if (payload.get('schema') != 1 or payload.get('sha256') != native['tested_archive_sha256']
            or not isinstance(parts, list) or not 1 <= len(parts) <= 64
            or len({part['name'] for part in parts}) != len(parts)):
        raise ValueError('Engine payload descriptor differs from its acceptance')
    size = 0
    for part in parts:
        name = filename(part['name'])
        expected_url = f'https://github.com/{REPOSITORY}/releases/download/{data["tag"]}/{name}'
        if (part.get('url') != expected_url or name not in values
                or any(values[name][key] != part[key] for key in ('bytes', 'sha256'))):
            raise ValueError('Engine part is missing or belongs to another release')
        size += part['bytes']
    if size != payload['bytes']:
        raise ValueError('Engine payload size differs')


def validate(data, release, remote, receipts):
    if not re.fullmatch(r'v\d+\.\d+\.\d+', data['tag']) or not re.fullmatch(r'[0-9a-f]{40}', data['source_revision']):
        raise ValueError('Invalid release source/version')
    expected = dict(schema=1, source_repository=SOURCE, version=data['tag'][1:], revision=data['source_revision'])
    marker = re.search(re.escape(MARKER) + r'(.*?) -->', release.get('body') or '')
    if (release.get('id') != data['draft_release_id'] or release.get('tag_name') != data['tag']
            or release.get('prerelease') or not marker or json.loads(marker[1]) != expected):
        raise ValueError('Draft identity/source differs')
    if len({value['name'] for value in data['assets']}) != len(data['assets']):
        raise ValueError('Duplicate release asset names')
    values = {value['name']: value for value in data['assets']}
    for value in values.values():
        if not re.fullmatch(r'[0-9a-f]{64}', value['sha256']) or not same_asset(remote.get(value['name'], {}), value):
            raise ValueError('Uploaded asset digest, size or identity differs: ' + value['name'])
    verification = data['upload_verification']
    if (verification.get('source_revision') != expected['revision']
            or verification.get('native_payload_sha256') != data['native_acceptance']['tested_archive_sha256']
            or verification.get('asset_ids') != [value['asset_id'] for value in data['assets']]):
        raise ValueError('Mac byte-verification receipt differs')
    for kind in ('windows', 'linux', 'images'):
        receipt = receipts[kind]
        if any(receipt.get(key) != value for key, value in expected.items()) or receipt.get('kind') != kind:
            raise ValueError('Producer receipt source/version differs')
        if kind == 'images':
            proofs = receipt.get('proofs', {})
            if receipt.get('files') != [] or set(proofs) != {'pushed-engine.json', 'pushed-web.json'}:
                raise ValueError('Image proof set differs')
            for name, proof in proofs.items():
                revision = proof.get('release_revision', proof.get('revision')) if name == 'pushed-engine.json' else proof.get('revision')
                if (revision != expected['revision'] or not proof.get('tag', '').endswith(':' + expected['version'] + '-amd64')
                        or not re.fullmatch(r'sha256:[0-9a-f]{64}', proof.get('image_id', ''))
                        or proof['image_id'] != proof.get('registry_index')):
                    raise ValueError('Image proof source, tag or registry digest differs')
        else:
            name = ('WWW-POSIM-' + expected['version'] + '-windows-x64.exe' if kind == 'windows'
                    else 'www-posim_' + expected['version'] + '_amd64.deb')
            if len(receipt['files']) != 1 or receipt['files'][0]['name'] != name:
                raise ValueError('Producer package set differs')
            value = receipt['files'][0]
            if name not in values or any(value[key] != values[name][key] for key in ('bytes', 'sha256', 'asset_id')):
                raise ValueError('Producer package differs from final manifest')
    validate_acceptance(data)
    return expected


def publish(data, notes):
    if os.environ.get('GITHUB_REPOSITORY') != REPOSITORY or os.environ.get('GITHUB_REF') != 'refs/heads/main':
        raise ValueError('Public promotion requires the download repository main branch')
    prefix = 'repos/' + REPOSITORY + '/releases/' + str(data['draft_release_id'])
    release = api(prefix)
    remote = {}
    for page in range(1, 21):
        rows = api(prefix + '/assets?per_page=100&page=' + str(page))
        for row in rows:
            if row['name'] in remote:
                raise ValueError('Duplicate remote asset name')
            remote[row['name']] = row
        if len(rows) < 100:
            break
    else:
        raise ValueError('Asset page limit exceeded')
    receipts = {}
    with tempfile.TemporaryDirectory(prefix='www-posim-receipts-') as folder:
        for kind in ('windows', 'linux', 'images'):
            name = 'release-build-' + kind + '.json'
            value = remote.get(name)
            if not value or not 0 < value['size'] <= 512 * 1024:
                raise ValueError('Missing producer receipt')
            path = Path(folder) / name
            command('release', 'download', data['tag'], '--repo', REPOSITORY,
                    '--pattern', name, '--output', str(path))
            content = path.read_bytes()
            if len(content) != value['size'] or 'sha256:' + hashlib.sha256(content).hexdigest() != value.get('digest'):
                raise ValueError('Producer receipt bytes differ')
            receipts[kind] = json.loads(content)
    expected = validate(data, release, remote, receipts)
    latest = api('repos/' + REPOSITORY + '/releases/latest')
    version = lambda tag: tuple(map(int, tag.removeprefix('v').split('.')))
    if version(latest['tag_name']) > version(data['tag']):
        raise ValueError('A newer stable release already exists')
    if release['draft']:
        body = notes.rstrip() + '\n\n' + MARKER + json.dumps(expected, sort_keys=True) + ' -->\n'
        api(prefix, 'PATCH', dict(draft=False, make_latest='true', body=body,
                                 name='WWW-POSIM ' + data['tag'][1:] + ' · Simulator packages'))
    Path('release-tag.txt').write_text(data['tag'])
    print('PASS: all direct uploads and native gates verified; stable release is public')


if __name__ == '__main__':
    publish(json.loads(Path('release-input.json').read_text()), Path('RELEASE.md').read_text())
