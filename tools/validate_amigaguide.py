#!/usr/bin/env python3
"""Strict static validator for generated EduARexx AmigaGuide."""
import argparse,re
from pathlib import Path
NODE=re.compile(r'^@node\s+([A-Za-z0-9_]+)\s+"[^"]*"$');LINK=re.compile(r'\blink\s+([A-Za-z0-9_]+)}');VER=re.compile(r'^@\$VER:\s+EduARexx\.guide\s+\d+\.\d+\.\d+\s+\(\d{2}\.\d{2}\.\d{4}\)$')
def validate(path,encoding="iso-8859-1"):
 raw=path.read_bytes();errors=[]
 try:text=raw.decode(encoding)
 except UnicodeDecodeError as e:return ["invalid "+encoding+" bytes: "+str(e)]
 lines=text.splitlines()
 if not lines or lines[0]!="@database EduARexx.guide":errors.append("invalid or missing @database")
 if len(lines)<2 or not VER.match(lines[1]):errors.append("invalid or missing $VER")
 nodes=[];ends=0;links=[]
 for n,line in enumerate(lines,1):
  if "\t" in line:errors.append("line %d: tab character"%n)
  if "\x00" in line:errors.append("line %d: NUL character"%n)
  if len(line)>1000:errors.append("line %d: unreasonable line length"%n)
  if line.startswith("@node "):
   m=NODE.match(line)
   if not m:errors.append("line %d: malformed @node"%n)
   else:nodes.append(m.group(1))
  if line.strip()=="@endnode":ends+=1
  links += [(n,m.group(1)) for m in LINK.finditer(line)]
 if "Main" not in nodes:errors.append("missing Main node")
 if len(nodes)!=len(set(nodes)):errors.append("duplicate node id")
 if len(nodes)!=ends:errors.append("node/endnode mismatch: %d vs %d"%(len(nodes),ends))
 known=set(nodes);errors += ["line %d: missing target %s"%(n,t) for n,t in links if t not in known]
 return errors
def main():
 ap=argparse.ArgumentParser();ap.add_argument("guide",type=Path);ap.add_argument("--encoding",default="iso-8859-1");a=ap.parse_args();e=validate(a.guide,a.encoding)
 if e:print("\n".join("ERROR: "+x for x in e));raise SystemExit(1)
 print("OK:",a.guide,"("+a.encoding+")")
if __name__=="__main__":main()
