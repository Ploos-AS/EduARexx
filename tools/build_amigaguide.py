#!/usr/bin/env python3
"""Build EduARexx AmigaGuide from Markdown."""
import argparse, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def node_id(p): return "N_"+re.sub(r"[^A-Za-z0-9_]","_",p.parent.name)
def convert(line):
    if line.startswith("## "): return line[3:].upper()
    line=re.sub(r"\[([^\]]+)\]\([^)]+\)",r"\1",line)
    return line.replace(chr(96),"")
def build(source):
    chapters=sorted(source.glob("*/README.md"))
    if not chapters: raise SystemExit("No chapters found")
    nodes=[]
    for p in chapters:
        lines=p.read_text(encoding="utf-8").splitlines()
        title=lines[0][2:].strip() if lines and lines[0].startswith("# ") else p.parent.name
        nodes.append((node_id(p),title,lines[1:]))
    out=["@database EduARexx.guide",'@author "Ploos AS"','@(c) "CC BY 4.0"',"",'@node Main "EduARexx"',"EduARexx","========",""]
    out += ['@{"'+title.replace('"',"'")+'" link '+nid+'}' for nid,title,_ in nodes]
    out += ["@endnode",""]
    for i,(nid,title,body) in enumerate(nodes):
        out += ['@node '+nid+' "'+title.replace('"',"'")+'"',title,"-"*min(max(len(title),3),70),""]
        code=False
        for line in body:
            if line.startswith(chr(96)*3): code=not code; continue
            out.append(("  "+line) if code and line else convert(line))
        prev=nodes[i-1][0] if i else "Main"
        nxt=nodes[i+1][0] if i+1<len(nodes) else "Main"
        out += ["",'@{"Forrige" link '+prev+'}  @{"Neste" link '+nxt+'}',"@endnode",""]
    return "\n".join(out)
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",type=Path,default=ROOT/"docs"/"no")
    ap.add_argument("--output",type=Path,default=ROOT/"build"/"EduARexx.guide")
    x=ap.parse_args(); x.output.parent.mkdir(parents=True,exist_ok=True)
    x.output.write_text(build(x.source),encoding="utf-8",newline="\n"); print("Wrote",x.output)
if __name__=="__main__": main()
