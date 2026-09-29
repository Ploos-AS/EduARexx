#!/usr/bin/env python3
"""Import and verify native amiga-runtime evidence without manufacturing PASS."""
import argparse,hashlib,json
from pathlib import Path

def sha256(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
 ap=argparse.ArgumentParser();ap.add_argument("--guide",type=Path,default=Path("build/EduARexx.guide"));ap.add_argument("--runtime-result",type=Path,required=True);ap.add_argument("--verification",type=Path,required=True);ap.add_argument("--output",type=Path,default=Path("build/native-qualification.json"));a=ap.parse_args()
 rr=json.loads(a.runtime_result.read_text());v=json.loads(a.verification.read_text())
 if rr.get("schema")!="amiga-runtime-result-v1":raise SystemExit("unsupported runtime result schema")
 if rr.get("runtime")!="amigaos":raise SystemExit("native qualification must use AmigaOS")
 if rr.get("status") not in ("PASS","FAIL"):raise SystemExit("invalid runtime status")
 if v.get("status") not in ("PASS","FAIL"):raise SystemExit("invalid verification status")
 status="PASS" if rr["status"]=="PASS" and v["status"]=="PASS" else "FAIL"
 out={"schema":1,"artifact_sha256":sha256(a.guide),"profile":rr.get("profile",""),"emulator":rr.get("emulator",""),"status":status,"runtime_result_schema":rr["schema"],"checks":{"runtime_process":rr["status"],"required_markers":v["status"]}}
 a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2)+"\n")
 print("Native qualification:",status)
 if status!="PASS":raise SystemExit(1)
if __name__=="__main__":main()
