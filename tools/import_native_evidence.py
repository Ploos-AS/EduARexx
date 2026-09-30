#!/usr/bin/env python3
"""Import native evidence and bind it to the exact EduARexx artifact."""
import argparse,hashlib,json
from pathlib import Path
def sha256(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--guide",type=Path,default=Path("build/EduARexx.guide"));ap.add_argument("--metadata",type=Path,default=Path("build/amiga-runtime-payload/eduarexx-metadata.json"));ap.add_argument("--runtime-result",type=Path,required=True);ap.add_argument("--verification",type=Path,required=True);ap.add_argument("--output",type=Path,default=Path("build/native-qualification.json"));a=ap.parse_args()
 rr=json.loads(a.runtime_result.read_text());v=json.loads(a.verification.read_text());m=json.loads(a.metadata.read_text())
 actual=sha256(a.guide);expected=m.get("sha256")
 if not expected or expected!=actual:raise SystemExit("artifact identity mismatch: payload metadata does not match guide")
 runtime_hash=rr.get("artifact_sha256"); verification_hash=v.get("artifact_sha256")\n if not runtime_hash or not verification_hash:raise SystemExit("native evidence is not artifact-bound")\n if runtime_hash!=actual or verification_hash!=actual:raise SystemExit("artifact identity mismatch: runtime evidence belongs to another guide")\n source_revision=m.get("source_revision")\n runtime_revision=rr.get("source_revision");verification_revision=v.get("source_revision")\n if not source_revision or source_revision=="UNKNOWN":raise SystemExit("payload metadata is not source-bound")\n if not runtime_revision or not verification_revision:raise SystemExit("native evidence is not source-bound")\n if runtime_revision!=source_revision or verification_revision!=source_revision:raise SystemExit("source revision mismatch: runtime evidence belongs to another build")
 if rr.get("schema")!="amiga-runtime-result-v1":raise SystemExit("unsupported runtime result schema")
 if rr.get("runtime")!="amigaos":raise SystemExit("native qualification must use AmigaOS")
 if rr.get("status") not in ("PASS","FAIL") or v.get("status") not in ("PASS","FAIL"):raise SystemExit("invalid evidence status")
 status="PASS" if rr["status"]=="PASS" and v["status"]=="PASS" else "FAIL"
 out={"schema":1,"artifact_sha256":actual,"source_revision":source_revision,"profile":rr.get("profile",""),"emulator":rr.get("emulator",""),"status":status,"runtime_result_schema":rr["schema"],"identity":{"payload_metadata":"PASS","runtime_evidence":"PASS"},"checks":{"runtime_process":rr["status"],"required_markers":v["status"]}}
 a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2)+"\n");print("Native qualification:",status)
 if status!="PASS":raise SystemExit(1)
if __name__=="__main__":main()
