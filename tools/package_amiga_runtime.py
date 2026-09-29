#!/usr/bin/env python3
"""Create an amiga-runtime qualification payload for EduARexx."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guide", type=Path, default=Path("build/EduARexx.guide"))
    ap.add_argument("--launcher", type=Path)
    ap.add_argument("--contract", type=Path, default=ROOT / "qualification" / "amiga-runtime.json")
    ap.add_argument("--output", type=Path, default=Path("build/amiga-runtime-payload"))
    a = ap.parse_args()

    c = json.loads(a.contract.read_text(encoding="utf-8"))
    if c.get("architecture") != "m68k":
        raise SystemExit("qualification contract must target m68k")
    p = c.get("payload", {})
    if p.get("kind") != "document":
        raise SystemExit("payload.kind must be document")
    if not a.guide.is_file():
        raise SystemExit("missing guide: " + str(a.guide))

    script = ROOT / "qualification" / p["script"]
    nav = ROOT / "qualification" / "amigaguide-nav.rexx"
    for src in (script, nav):
        if not src.is_file():
            raise SystemExit("missing qualification source: " + str(src))

    if a.output.exists():
        shutil.rmtree(a.output)
    a.output.mkdir(parents=True)
    (a.output / "results").mkdir()

    shutil.copy2(a.guide, a.output / p["document"])
    shutil.copy2(script, a.output / p["script"])
    shutil.copy2(nav, a.output / "amigaguide-nav.rexx")

    meta = {
        "artifact": p["document"],
        "sha256": digest(a.guide),
        "native_status": "NOT_RUN",
        "contract_schema": c["schema"],
    }

    if a.launcher is not None:
        if not a.launcher.is_file():
            raise SystemExit("missing native launcher: " + str(a.launcher))
        shutil.copy2(a.launcher, a.output / "amigaguide-launcher")
        meta["launcher"] = {
            "artifact": "amigaguide-launcher",
            "sha256": digest(a.launcher),
            "architecture": "m68k",
            "compile_status": "EXTERNAL_EVIDENCE_REQUIRED",
        }
        p["launcher"] = "amigaguide-launcher"

    identity = dict(c.get("artifact_identity", {}))
    if identity.get("sha256_source") == "eduarexx-metadata.json":
        identity["sha256"] = meta["sha256"]
    c["artifact_identity"] = identity

    (a.output / "eduarexx-metadata.json").write_text(
        json.dumps(meta, indent=2) + "\n", encoding="utf-8"
    )
    (a.output / "amiga-runtime.json").write_text(
        json.dumps(c, indent=2) + "\n", encoding="utf-8"
    )

    for rel in (p["document"], p["script"], "amigaguide-nav.rexx", "amiga-runtime.json"):
        if not (a.output / rel).is_file():
            raise SystemExit("incomplete payload: " + rel)

    print("Prepared", a.output)
    print("Native status: NOT_RUN")
    print("Launcher:", "included" if a.launcher is not None else "not included")

if __name__ == "__main__":
    main()
