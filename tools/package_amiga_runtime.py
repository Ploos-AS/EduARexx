#!/usr/bin/env python3
"""Create an amiga-runtime qualification payload for EduARexx."""
import argparse,hashlib,json,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--guide",type=Path,default=Path("build/EduARexx.guide"));ap.add_argument("--contract",type=Path,default=ROOT/"qualification"/"amiga-runtime.json");ap.add_argument("--output",type=Path,default=Path("build/amiga-runtime-payload"));a=ap.parse_args()
 c=json.loads(a.contract.read_text(encoding="utf-8"))
 if c.get("architecture")!="m68k":raise SystemExit("qualification contract must target m68k")
 p=c.get("payload",{})
 if p.get("kind")!="document":raise SystemExit("payload.kind must be document")
 script=ROOT/"qualification"/p["script"]
 if not script.is_file():raise SystemExit("missing guest script: "+str(script))
 if a.output.exists():shutil.rmtree(a.output)
 a.output.mkdir(parents=True)
 shutil.copy2(a.guide,a.output/p["document"]);shutil.copy2(script,a.output/p["script"]);(a.output/"results").mkdir()
 meta={"artifact":p["document"],"sha256":digest(a.guide),"native_status":"NOT_RUN","contract_schema":c["schema"]}
 (a.output/"eduarexx-metadata.json").write_text(json.dumps(meta,indent=2)+"\n",encoding="utf-8")
 for key in ("document","script"):
  if not (a.output/p[key]).is_file():raise SystemExit("incomplete payload: "+p[key])
 print("Prepared",a.output);print("Native status: NOT_RUN")
if __name__=="__main__":main()
