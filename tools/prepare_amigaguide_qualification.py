#!/usr/bin/env python3
"""Prepare, but never claim, a native AmigaGuide qualification run."""
import argparse, hashlib, json
from pathlib import Path

def sha256(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(65536),b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--artifact",type=Path,default=Path("build/EduARexx.guide"))
    ap.add_argument("--manifest",type=Path,default=Path("qualification/amigaguide.json"))
    ap.add_argument("--output",type=Path,default=Path("build/qualification-request.json"))
    a=ap.parse_args()
    manifest=json.loads(a.manifest.read_text(encoding="utf-8"))
    if manifest.get("status")!="NOT_RUN":
        raise SystemExit("manifest baseline must remain NOT_RUN")
    request={
        "schema":1,
        "artifact":a.artifact.name,
        "artifact_sha256":sha256(a.artifact),
        "platform":manifest["platform"],
        "application":manifest["application"],
        "profiles":manifest["profiles"],
        "emulators":manifest["emulators"],
        "checks":manifest["checks"],
        "requested_status":"NOT_RUN"
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(request,indent=2)+"\n",encoding="utf-8")
    print("Prepared",a.output)
    print("Native status: NOT_RUN")

if __name__=="__main__":
    main()
