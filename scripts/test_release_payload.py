import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from release_payload import verify


class PayloadPublication(unittest.TestCase):
    def fixture(self, root):
        pieces=[b'first part',b'second part'];parts=[]
        for i,content in enumerate(pieces):
            name=f'engine.part{i:03d}';(root/name).write_bytes(content)
            parts.append(dict(name=name,bytes=len(content),sha256=hashlib.sha256(content).hexdigest(),url='https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.5.26/'+name))
        sha=hashlib.sha256(b''.join(pieces)).hexdigest()
        return dict(tag='v0.5.26',dmg_acceptance=dict(mounted_diagnostic=dict(native_engine_download=True)),native_acceptance=dict(tested_archive_sha256=sha),assets=parts,native_payload=dict(schema=1,sha256=sha,bytes=sum(len(p) for p in pieces),parts=parts))

    def test_bootstrap_and_legacy_releases(self):
        with tempfile.TemporaryDirectory() as temp:
            data=self.fixture(Path(temp));verify(data,temp)
            data.pop('native_payload');data['dmg_acceptance']['mounted_diagnostic']=dict(native_engine_included=True)
            verify(data,temp)

    def test_invalid_or_missing_parts_stop_publication(self):
        for problem in ('missing','changed','oversized','reordered','url','descriptor'):
            with self.subTest(problem=problem),tempfile.TemporaryDirectory() as temp:
                root=Path(temp);data=self.fixture(root)
                # Separate the copied asset metadata from descriptor metadata.
                data=json.loads(json.dumps(data));parts=data['native_payload']['parts']
                if problem=='missing':data['assets'].pop()
                elif problem=='changed':(root/parts[0]['name']).write_bytes(b'corrupt')
                elif problem=='oversized':parts[0]['bytes']=2*1024**3
                elif problem=='reordered':parts.reverse()
                elif problem=='url':parts[0]['url']='https://other.example/file'
                elif problem=='descriptor':data.pop('native_payload')
                with self.assertRaises(ValueError):verify(data,temp)


if __name__=='__main__':unittest.main()
