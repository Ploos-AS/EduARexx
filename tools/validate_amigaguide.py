#!/usr/bin/env python3
"""Validate basic AmigaGuide structure."""
import argparse,re
from pathlib import Path
NODE=re.compile(r'^@node\s+(\S+)\s+"')
LINK=re.compile(r'\blink\s+(\S+)}')
def validate(path):
    lines=path.read_text(encoding="utf-8").splitlines(); errors=[]
    if not lines or not lines[0].startswith("@database "): errors.append("missing @database")
    nodes=[]; ends=0; links=[]
    for n,line in enumerate(lines,1):
        m=NODE.match(line)
        if m: nodes.append(m.group(1))
        if line.strip()=="@endnode": ends+=1
        links += [(n,m.group(1)) for m in LINK.finditer(line)]
    if len(nodes)!=len(set(nodes)): errors.append("duplicate node id")
    if len(nodes)!=ends: errors.append("node/endnode mismatch")
    known=set(nodes)
    errors += ["line %d: missing target %s"%(n,t) for n,t in links if t not in known]
    return errors
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("guide",type=Path); x=ap.parse_args()
    errors=validate(x.guide)
    if errors:
        print("\n".join("ERROR: "+e for e in errors)); raise SystemExit(1)
    print("OK:",x.guide)
if __name__=="__main__": main()
