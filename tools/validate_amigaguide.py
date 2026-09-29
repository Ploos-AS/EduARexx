#!/usr/bin/env python3
"""Validate AmigaGuide structure and classic-output byte contract."""
import argparse,re
from pathlib import Path
NODE=re.compile(r'^@node\s+(\S+)\s+"'); LINK=re.compile(r'\blink\s+(\S+)}')
def validate(path,encoding="iso-8859-1"):
    raw=path.read_bytes(); errors=[]
    try: text=raw.decode(encoding)
    except UnicodeDecodeError as e: return ["invalid "+encoding+" bytes: "+str(e)]
    lines=text.splitlines()
    if not lines or not lines[0].startswith("@database "): errors.append("missing @database")
    nodes=[]; ends=0; links=[]
    for n,line in enumerate(lines,1):
        m=NODE.match(line)
        if m: nodes.append(m.group(1))
        if line.strip()=="@endnode": ends+=1
        links += [(n,m.group(1)) for m in LINK.finditer(line)]
        if "\t" in line: errors.append("line %d: tab character"%n)
    if len(nodes)!=len(set(nodes)): errors.append("duplicate node id")
    if len(nodes)!=ends: errors.append("node/endnode mismatch: %d vs %d"%(len(nodes),ends))
    known=set(nodes); errors += ["line %d: missing target %s"%(n,t) for n,t in links if t not in known]
    return errors
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("guide",type=Path); ap.add_argument("--encoding",default="iso-8859-1"); a=ap.parse_args(); errors=validate(a.guide,a.encoding)
    if errors: print("\n".join("ERROR: "+e for e in errors)); raise SystemExit(1)
    print("OK:",a.guide,"("+a.encoding+")")
if __name__=="__main__": main()
