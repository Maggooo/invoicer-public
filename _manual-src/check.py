#!/usr/bin/env python3
"""Sanity-checks every language file against the English master: same sections, same block kinds/counts, same {{tokens}}, valid keys, balanced tags."""
import importlib, json, re, sys
from html.parser import HTMLParser
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from build import LANGS, ORDER
TOK = re.compile(r"\{\{([a-z0-9_]+)\}\}")
VOID = {"br", "img", "hr"}

class Bal(HTMLParser):
    def __init__(s): super().__init__(); s.st = []; s.err = []
    def handle_starttag(s, t, a):
        if t not in VOID: s.st.append(t)
    def handle_endtag(s, t):
        if s.st and s.st[-1] == t: s.st.pop()
        else: s.err.append(t)

def flat(sec):
    title, blocks = sec
    out = []
    for kind, body in blocks:
        items = body if kind == "ul" else [body]
        out.append((kind, len(items), [TOK.findall(i) for i in items]))
    return out

en = importlib.import_module("lang.en").T
bad = 0
for code, _ in LANGS:
    T = importlib.import_module(f"lang.{code}").T
    ui = json.loads((Path(__file__).parent / "ui" / f"{code}.json").read_text())
    problems = []
    for k in en:
        if k not in T: problems.append(f"missing key {k}")
    for sid, _ in ORDER:
        if sid not in T["sections"]: problems.append(f"missing section {sid}"); continue
        a, b = flat(en["sections"][sid]), flat(T["sections"][sid])
        if [(k, n) for k, n, _ in a] != [(k, n) for k, n, _ in b]:
            problems.append(f"{sid}: block structure differs ({[(k,n) for k,n,_ in a]} vs {[(k,n) for k,n,_ in b]})"); continue
        for (k, n, ta), (_, _, tb) in zip(a, b):
            for x, y in zip(ta, tb):
                if sorted(set(x)) != sorted(set(y)): problems.append(f"{sid}: tokens differ {sorted(set(x))} vs {sorted(set(y))}")
    texts = [T["lede"], T["warn"]] + [b for s in T["sections"].values() for kind, body in s[1] for b in (body if kind == "ul" else [body])]
    for t in texts:
        for key in TOK.findall(t):
            if key not in ui: problems.append(f"unknown UI key {key}")
        p = Bal(); p.feed(t)
        if p.st or p.err: problems.append(f"unbalanced HTML in: {t[:60]}… {p.st} {p.err}")
    print(("OK   " if not problems else "FAIL ") + code, *problems[:6], sep="\n     " if problems else " ")
    bad += bool(problems)
sys.exit(1 if bad else 0)
