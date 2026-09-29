import tempfile, unittest
from pathlib import Path
from tools.build_amigaguide import build
from tools.validate_amigaguide import validate
class Tests(unittest.TestCase):
    def test_minimal(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); ch=root/"01-test"; ch.mkdir()
            (ch/"README.md").write_text("# Test\n\nHello ARexx.\n",encoding="utf-8")
            out=root/"x.guide"; out.write_text(build(root),encoding="utf-8")
            self.assertEqual(validate(out),[])
    def test_bad_link(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"x.guide"
            p.write_text('@database x\n@node Main "x"\n@{"x" link Missing}\n@endnode\n',encoding="utf-8")
            self.assertTrue(validate(p))
if __name__=="__main__": unittest.main()
