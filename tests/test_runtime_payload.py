import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGER = ROOT / "tools" / "package_amiga_runtime.py"
CONTRACT = ROOT / "qualification" / "amiga-runtime.json"

class RuntimePayloadTests(unittest.TestCase):
    def run_packager(self, guide, output, launcher=None):
        cmd = [
            sys.executable, str(PACKAGER),
            "--guide", str(guide),
            "--contract", str(CONTRACT),
            "--output", str(output),
        ]
        if launcher is not None:
            cmd += ["--launcher", str(launcher)]
        return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)

    def test_document_payload_without_launcher(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            guide = d / "EduARexx.guide"
            guide.write_bytes(b"guide")
            out = d / "payload"
            p = self.run_packager(guide, out)
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertTrue((out / "EduARexx.guide").is_file())
            self.assertTrue((out / "amigaguide-test").is_file())
            self.assertTrue((out / "amigaguide-nav.rexx").is_file())
            self.assertFalse((out / "amigaguide-launcher").exists())
            meta = json.loads((out / "eduarexx-metadata.json").read_text())
            self.assertEqual(meta["native_status"], "NOT_RUN")
            self.assertNotIn("launcher", meta)

    def test_missing_explicit_launcher_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            guide = d / "EduARexx.guide"
            guide.write_bytes(b"guide")
            p = self.run_packager(guide, d / "payload", d / "missing-launcher")
            self.assertNotEqual(p.returncode, 0)
            self.assertIn("missing native launcher", p.stderr + p.stdout)

    def test_launcher_and_guide_hashes_are_bound(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            guide = d / "EduARexx.guide"
            launcher = d / "amigaguide-launcher"
            guide.write_bytes(b"guide-v1")
            launcher.write_bytes(b"synthetic-launcher-fixture")
            out = d / "payload"
            p = self.run_packager(guide, out, launcher)
            self.assertEqual(p.returncode, 0, p.stderr)

            meta = json.loads((out / "eduarexx-metadata.json").read_text())
            contract = json.loads((out / "amiga-runtime.json").read_text())
            guide_sha = hashlib.sha256(guide.read_bytes()).hexdigest()
            launcher_sha = hashlib.sha256(launcher.read_bytes()).hexdigest()

            self.assertEqual(meta["sha256"], guide_sha)
            self.assertEqual(meta["launcher"]["sha256"], launcher_sha)
            self.assertEqual(meta["launcher"]["architecture"], "m68k")
            self.assertEqual(contract["artifact_identity"]["sha256"], guide_sha)
            self.assertEqual(contract["payload"]["launcher"], "amigaguide-launcher")
            self.assertEqual((out / "amigaguide-launcher").read_bytes(), launcher.read_bytes())

if __name__ == "__main__":
    unittest.main()
