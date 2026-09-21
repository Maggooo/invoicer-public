#!/usr/bin/env python3
"""Copies the app's UI texts (one JSON per language) so the manual can quote button names exactly as the app shows them.

Run after the app's strings change:  python3 extract_ui_strings.py [path/to/app/src/main/res]
"""
import json, re, sys, xml.etree.ElementTree as ET
from pathlib import Path

RES = Path(sys.argv[1] if len(sys.argv) > 1 else Path.home() / "Desktop/proiecte/invoicer/app/src/main/res")
LANGS = {"en": "values", **{l: f"values-{l}" for l in "ro de es fr it pt pl cs sk hu nl sv".split()}}

def clean(text: str) -> str:
    text = (text or "").replace("\\'", "'").replace('\\"', '"').replace("\\n", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text

for lang, folder in LANGS.items():
    root = ET.parse(RES / folder / "strings.xml").getroot()
    out = {s.get("name"): clean("".join(s.itertext())) for s in root.findall("string")}
    (Path(__file__).parent / "ui" / f"{lang}.json").write_text(json.dumps(out, ensure_ascii=False, indent=0, sort_keys=True))
    print(lang, len(out))
