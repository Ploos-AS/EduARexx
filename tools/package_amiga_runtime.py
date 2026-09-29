#!/usr/bin/env python3
"""Create an amiga-runtime qualification payload for EduARexx."""
import argparse, hashlib, json, shutil
from pathlib import Path

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--guide",type=Path,default=Path("build/EduARexx.guide"))
    ap.add_argument("--contract",type=Path,default=Path("qualification/amiga-runtime.json"))
    ap.add_argument("--output",type=Path,default=Path("build/amiga-runtime-payload"))
    a=ap.parse_args()
    contract=json.loads(a.contract.read_text(encoding="utf-8"))
    if contract.get("architecture")!="m68k":
        raise SystemExit("qualification contract must target m68k")
    a.output.mkdir(parents=True,exist_ok=True)
    shutil.copy2(a.guide,a.output/"EduARexx.guide")
    shutil.copy2(a.contract,a.output/"amiga-runtime.json")
    (a.output/"results").mkdir(exist_ok=True)
    meta={"artifact":"EduARexx.guide","sha256":digest(a.guide),"native_status":"NOT_RUN"}
    (a.output/"eduarexx-metadata.json").write_text(json.dumps(meta,indent=2)+"\n",encoding="utf-8")
    print("Prepared",a.output)
    print("Native status: NOT_RUN")

if __name__=="__main__":
    main()
