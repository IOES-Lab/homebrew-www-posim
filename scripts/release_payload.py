"""Verify that public download parts reconstruct the acceptance-tested engine."""
import hashlib
from pathlib import Path
import re


def verify(data, folder):
    diagnostic=data['dmg_acceptance']['mounted_diagnostic']
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
