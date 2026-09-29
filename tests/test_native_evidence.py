import hashlib,json,subprocess,sys,tempfile,unittest
from pathlib import Path
class EvidenceIdentityTests(unittest.TestCase):
 def test_rejects_different_artifact(self):
  with tempfile.TemporaryDirectory() as td:
   d=Path(td);guide=d/"g.guide";guide.write_bytes(b"new")
   meta=d/"meta.json";meta.write_text(json.dumps({"sha256":hashlib.sha256(b"old").hexdigest()}))
   rr=d/"r.json";rr.write_text(json.dumps({"schema":"amiga-runtime-result-v1","runtime":"amigaos","status":"PASS"}))
   ver=d/"v.json";ver.write_text(json.dumps({"status":"PASS"}))
   p=subprocess.run([sys.executable,"tools/import_native_evidence.py","--guide",str(guide),"--metadata",str(meta),"--runtime-result",str(rr),"--verification",str(ver),"--output",str(d/"out.json")],capture_output=True,text=True)
   self.assertNotEqual(p.returncode,0);self.assertIn("artifact identity mismatch",p.stderr+p.stdout)
if __name__=="__main__":unittest.main()
