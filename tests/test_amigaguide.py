import tempfile, unittest
from pathlib import Path
from tools.build_amigaguide import build
from tools.validate_amigaguide import validate

class Tests(unittest.TestCase):
    def make(self, markdown):
        td=tempfile.TemporaryDirectory()
        root=Path(td.name); ch=root/"01-test"; ch.mkdir()
        (ch/"README.md").write_text(markdown,encoding="utf-8")
        out=root/"x.guide"; out.write_text(build(root),encoding="utf-8")
        return td,out,out.read_text(encoding="utf-8")

    def test_minimal(self):
        td,out,_=self.make("# Test\n\nHello ARexx.\n")
        try: self.assertEqual(validate(out),[])
        finally: td.cleanup()

    def test_markdown_structures(self):
        td,out,text=self.make("# Test\n\n## Del\n\n- one\n- two\n\n1. first\n\n\`\`\`rexx\nsay 'hi'\n\`\`\`\n")
        try:
            self.assertIn(" * one",text)
            self.assertIn(" 1. first",text)
            self.assertIn("  say 'hi'",text)
            self.assertEqual(validate(out),[])
        finally: td.cleanup()

    def test_literal_at_is_escaped(self):
        td,out,text=self.make("# Test\n\nemail@example.invalid\n")
        try:
            self.assertIn("email@@example.invalid",text)
            self.assertEqual(validate(out),[])
        finally: td.cleanup()

    def test_bad_link(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"x.guide"
            p.write_text('@database x\n@node Main "x"\n@{"x" link Missing}\n@endnode\n',encoding="utf-8")
            self.assertTrue(validate(p))

if __name__=="__main__": unittest.main()
