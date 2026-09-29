#!/usr/bin/env python3
"""Build EduARexx AmigaGuide from Markdown.

This deliberately implements a small, predictable Markdown subset rather
than pretending AmigaGuide is HTML.
"""
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
INLINE_CODE = re.compile(r"`([^`]+)`")

def node_id(path):
    return "N_" + re.sub(r"[^A-Za-z0-9_]", "_", path.parent.name)

def escape(text):
    # @ starts AmigaGuide commands. Literal source text must not accidentally
    # become markup.
    return text.replace("@", "@@")

def inline(text):
    text = INLINE_CODE.sub(r"\1", text)
    # External/Markdown links remain readable text in M7.1. Chapter navigation
    # is generated separately from known source files.
    text = LINK.sub(lambda m: m.group(1) + " (" + m.group(2) + ")", text)
    return escape(text)

def convert_line(line):
    if line.startswith("### "):
        return inline(line[4:])
    if line.startswith("## "):
        title = inline(line[3:])
        return "\n" + title + "\n" + "~" * min(max(len(title), 3), 70)
    if re.match(r"^\s*[-*]\s+", line):
        return " * " + inline(re.sub(r"^\s*[-*]\s+", "", line))
    m = re.match(r"^\s*(\d+)\.\s+(.*)", line)
    if m:
        return " " + m.group(1) + ". " + inline(m.group(2))
    if line.startswith("> "):
        return "  " + inline(line[2:])
    return inline(line)

def build(source):
    chapters = sorted(source.glob("*/README.md"))
    if not chapters:
        raise SystemExit("No chapters found")
    nodes = []
    for path in chapters:
        lines = path.read_text(encoding="utf-8").splitlines()
        title = lines[0][2:].strip() if lines and lines[0].startswith("# ") else path.parent.name
        nodes.append((node_id(path), title, lines[1:]))

    out = [
        "@database EduARexx.guide",
        '@author "Ploos AS"',
        '@(c) "CC BY 4.0"',
        "",
        '@node Main "EduARexx"',
        "EduARexx",
        "========",
        "",
        "Fra SAY \"Hello\" til Amiga power user.",
        "",
    ]
    for nid, title, _ in nodes:
        safe_title = title.replace('"', "'")
        out.append('@{"' + safe_title + '" link ' + nid + '}')
    out += ["@endnode", ""]

    for i, (nid, title, body) in enumerate(nodes):
        safe_title = title.replace('"', "'")
        out += ['@node ' + nid + ' "' + safe_title + '"',
                inline(title), "-" * min(max(len(title), 3), 70), ""]
        in_code = False
        for line in body:
            if line.startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                # Preserve code exactly except literal @ escaping.
                out.append("  " + escape(line) if line else "")
            else:
                out.extend(convert_line(line).split("\n"))

        prev_node = nodes[i-1][0] if i else "Main"
        next_node = nodes[i+1][0] if i + 1 < len(nodes) else "Main"
        out += [
            "",
            '@{"Forrige" link ' + prev_node + '}  @{"Innhold" link Main}  @{"Neste" link ' + next_node + '}',
            "@endnode",
            "",
        ]
    return "\n".join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, default=ROOT/"docs"/"no")
    ap.add_argument("--output", type=Path, default=ROOT/"build"/"EduARexx.guide")
    args = ap.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(build(args.source), encoding="utf-8", newline="\n")
    print("Wrote", args.output)

if __name__ == "__main__":
    main()
