import tempfile, unittest
from pathlib import Path
from tools.build_amigaguide import build
from tools.validate_amigaguide import validate
class Tests(unittest.TestCase):
    def make(self,markdown):
        td=tempfile.TemporaryDirectory(); root=Path(td.name); ch=root/"01-test"; ch.mkdir()
        (ch/"README.md").write_text(markdown,encoding="utf-8"); out=root/"x.guide"
        out.write_bytes(build(root).encode("iso-8859-1")); return td,out,out.read_text(encoding="iso-8859-1")
    def test_minimal(self):
        td,out,_=self.make("# Test\n\nHello ARexx.\n")
        try:self.assertEqual(validate(out),[])
        finally:td.cleanup()
    def test_norwegian_survives_latin1(self):
        td,out,text=self.make("# ÆØÅ æøå\n\nNorsk ære, øvelse og åpenhet.\n")
        try:
            self.assertIn("ÆØÅ æøå",text); self.assertEqual(validate(out),[])
        finally:td.cleanup()
    def test_unicode_is_predictable(self):
        td,out,text=self.make("# Test → mål\n\n“ARexx” — fint…\n")
        try:
            self.assertIn("Test -> mål",text); self.assertIn('"ARexx" - fint...',text)
        finally:td.cleanup()
    def test_literal_at_is_escaped(self):
        td,out,text=self.make("# Test\n\nemail@example.invalid\n")
        try:self.assertIn("email@@example.invalid",text)
        finally:td.cleanup()
    def test_bad_link(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"x.guide"; p.write_bytes(b'@database x\n@node Main "x"\n@{"x" link Missing}\n@endnode\n')
            self.assertTrue(validate(p))
if __name__=="__main__": unittest.main()
