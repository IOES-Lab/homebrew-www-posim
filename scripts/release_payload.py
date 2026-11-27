"""Verify that public download parts reconstruct the acceptance-tested engine."""
import hashlib
import json
from pathlib import Path
import re


MISSION_TAG = 'v0.6.20'
MISSION_RECEIPT = 'release-installed-missions.json'
MAX_RECEIPT_BYTES = 512 * 1024


def verify_installed_missions(data, content):
    """Bind the private producer's raw-replay result to this public candidate."""
    if data['tag'] != MISSION_TAG:
        return
    entries = [entry for entry in data['assets'] if entry['name'] == MISSION_RECEIPT]
    if (not isinstance(content, bytes) or not 0 < len(content) <= MAX_RECEIPT_BYTES
            or len(entries) != 1 or entries[0]['bytes'] != len(content)
            or hashlib.sha256(content).hexdigest() != entries[0]['sha256']):
        raise ValueError('Missing or changed installed mission receipt')
    try:
        receipt = json.loads(content)
        dmg = data['dmg_acceptance']
        native = data['native_acceptance']
        expected = dict(policy='bluerov2-installed-2p1-v1', version=MISSION_TAG[1:],
                        platform='macos-arm64', source_revision=data['source_revision'], posim_revision=data['posim_revision'],
                        dmg=dmg['dmg'], dmg_sha256=dmg['sha256'], engine_sha256=dmg['engine_sha256'],
                        launcher_sha256=dmg['mounted_executable_sha256'])
        trials = receipt['trials']
        if (any(receipt[key] != value for key, value in expected.items())
                or not re.fullmatch(r'[a-f0-9]{40}', expected['source_revision'])
                or not re.fullmatch(r'[a-f0-9]{40}', receipt['posim_revision'])
                or any(not re.fullmatch(r'[a-f0-9]{64}', receipt[key]) for key in
                       ('dmg_sha256', 'engine_sha256', 'launcher_sha256', 'suite_sha256'))
                or expected['launcher_sha256'] != dmg['app_executable_sha256']
                or expected['engine_sha256'] != native['tested_archive_sha256']
                or [row['outcome'] for row in trials] != ['completed', 'completed', 'dvl_stale']):
            raise ValueError('The installed mission receipt differs from this candidate')
        for key in ('nonce_sha256', 'mission_sha256', 'samples_sha256'):
            values = {row[key] for row in trials}
            if len(values) != 3 or any(not re.fullmatch(r'[a-f0-9]{64}', value) for value in values):
                raise ValueError('The installed mission trial identities or samples differ')
    except (KeyError, TypeError, UnicodeError, json.JSONDecodeError) as error:
        raise ValueError('Malformed installed mission receipt') from error


def verify(data, folder):
    if data['tag'] == MISSION_TAG:
        path = Path(folder) / MISSION_RECEIPT
        if not path.is_file() or path.stat().st_size > MAX_RECEIPT_BYTES:
            raise ValueError('Missing or oversized installed mission receipt')
        verify_installed_missions(data, path.read_bytes())
    diagnostic=data['dmg_acceptance']['mounted_diagnostic']
    if diagnostic.get('publishable') is False or diagnostic.get('edition','release')!='release':
        raise ValueError('Local development packages cannot be published')
    payload=data.get('native_payload')
    if payload is None:
        if diagnostic.get('native_engine_included') is not True:
            raise ValueError('A bootstrap installer must publish its engine parts')
        return
    expected=data['native_acceptance']['tested_archive_sha256']
    if payload.get('schema')!=1 or payload.get('sha256')!=expected:
        raise ValueError('Download payload differs from the accepted engine')
    parts=payload.get('parts')
    if not isinstance(parts,list) or not 1<=len(parts)<=64:
        raise ValueError('Invalid engine parts')
    names=[part['name'] for part in parts]
    if len(set(names))!=len(names):raise ValueError('Duplicate engine parts')
    assets={asset['name']:asset for asset in data['assets']}
    complete=hashlib.sha256();size=0
    for part in parts:
        name=part['name']
        if not re.fullmatch(r'[A-Za-z0-9_.-]+',name) or name in ('.','..'):
            raise ValueError('Invalid engine part filename')
        if type(part['bytes']) is not int or not 0<part['bytes']<2*1024**3:
            raise ValueError('Engine part must be below 2 GiB')
        if name not in assets or any(part[key]!=assets[name][key] for key in ('bytes','sha256')):
            raise ValueError('Engine part is missing from release assets')
        expected_url=f"https://github.com/IOES-Lab/homebrew-www-posim/releases/download/{data['tag']}/{name}"
        if part['url']!=expected_url:raise ValueError('Engine part points outside this release')
        file=Path(folder)/name;value=hashlib.sha256()
        if file.stat().st_size!=part['bytes']:raise ValueError('Engine part size changed')
        with file.open('rb') as source:
            while chunk:=source.read(1024**2):value.update(chunk);complete.update(chunk);size+=len(chunk)
        if value.hexdigest()!=part['sha256']:raise ValueError('Engine part checksum changed')
    if size!=payload['bytes'] or complete.hexdigest()!=expected:
        raise ValueError('Engine parts do not reconstruct the accepted archive')
