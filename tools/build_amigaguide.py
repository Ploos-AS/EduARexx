#!/usr/bin/env python3
"""Build EduARexx AmigaGuide from Markdown."""
import argparse,re,unicodedata
from datetime import date
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LINK=re.compile(r"\[([^\]]+)\]\(([^)]+)\)"); INLINE=re.compile(r"`([^`]+)`")
TRANS=str.maketrans({"–":"-","—":"-","…":"...","“":'"',"”":'"',"‘":"'","’":"'","→":"->","←":"<-","•":"*"})
def node_id(p): return "N_"+re.sub(r"[^A-Za-z0-9_]","_",p.parent.name)
def escape(s): return s.replace("@","@@")
def amiga_text(s):
 s=s.translate(TRANS)
 try:s.encode("iso-8859-1");return s
 except UnicodeEncodeError:return unicodedata.normalize("NFKD",s).encode("iso-8859-1","ignore").decode("iso-8859-1")
def inline(s): return escape(LINK.sub(lambda m:m.group(1)+" ("+m.group(2)+")",INLINE.sub(r"\1",amiga_text(s))))
def convert(line):
 if line.startswith("### "):return inline(line[4:])
 if line.startswith("## "):
  t=inline(line[3:]);return "\n"+t+"\n"+"~"*min(max(len(t),3),70)
 if re.match(r"^\s*[-*]\s+",line):return " * "+inline(re.sub(r"^\s*[-*]\s+","",line))
 m=re.match(r"^\s*(\d+)\.\s+(.*)",line)
 if m:return " "+m.group(1)+". "+inline(m.group(2))
 if line.startswith("> "):return "  "+inline(line[2:])
 return inline(line)
def build(source,version="0.1.0",build_date=None):
 chapters=sorted(source.glob("*/README.md"))
 if not chapters:raise SystemExit("No chapters found")
 build_date=build_date or date.today().strftime("%d.%m.%Y")
 nodes=[]
 for p in chapters:
  lines=p.read_text(encoding="utf-8").splitlines();title=lines[0][2:].strip() if lines and lines[0].startswith("# ") else p.parent.name;nodes.append((node_id(p),title,lines[1:]))
 out=["@database EduARexx.guide","@$VER: EduARexx.guide "+version+" ("+build_date+")",'@author "Ploos AS"','@(c) "CC BY 4.0"',"",'@node Main "EduARexx"',"EduARexx","========","","Fra SAY \"Hello\" til Amiga power user.",""]
 for nid,title,_ in nodes:out.append('@{"'+amiga_text(title).replace('"',"'")+'" link '+nid+'}')
 out+=["@endnode",""]
 for i,(nid,title,body) in enumerate(nodes):
  st=amiga_text(title).replace('"',"'");out+=['@node '+nid+' "'+st+'"',inline(title),"-"*min(max(len(st),3),70),""];code=False
  for line in body:
   if line.startswith("```"):code=not code;continue
   out.append(("  "+escape(amiga_text(line)) if line else "") if code else convert(line))
  prev=nodes[i-1][0] if i else "Main";nxt=nodes[i+1][0] if i+1<len(nodes) else "Main";out+=["",'@{"Forrige" link '+prev+'}  @{"Innhold" link Main}  @{"Neste" link '+nxt+'}',"@endnode",""]
 return "\n".join(out)
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--source",type=Path,default=ROOT/"docs"/"no");ap.add_argument("--output",type=Path,default=ROOT/"build"/"EduARexx.guide");ap.add_argument("--encoding",choices=["iso-8859-1","utf-8"],default="iso-8859-1");ap.add_argument("--version",default="0.1.0");a=ap.parse_args();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_bytes(build(a.source,a.version).encode(a.encoding));print("Wrote",a.output,a.version,a.encoding)
if __name__=="__main__":main()
