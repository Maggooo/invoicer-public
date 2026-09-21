#!/usr/bin/env python3
"""Builds the User Manual pages (manual.html + manual-<lang>.html) from lang/<lang>.py.

Text lives in lang/*.py; button names come from ui/<lang>.json (copied from the app by
extract_ui_strings.py) through {{string_key}} tokens, so the manual always says what the app says.
Run from anywhere:  python3 _manual-src/build.py
"""
import html, importlib, json, re, sys
from pathlib import Path

HERE = Path(__file__).parent
SITE = HERE.parent
sys.path.insert(0, str(HERE))

LANGS = [  # code, native name (same order as the app's language switcher)
    ("en", "English"), ("ro", "Română"), ("de", "Deutsch"), ("fr", "Français"), ("es", "Español"),
    ("it", "Italiano"), ("pt", "Português"), ("pl", "Polski"), ("cs", "Čeština"), ("sk", "Slovenčina"),
    ("hu", "Magyar"), ("nl", "Nederlands"), ("sv", "Svenska"),
]

# id -> screenshots (files in assets/screenshots/). Same screenshots for every language.
ORDER = [
    ("home", ["home.png"]),
    ("customers", ["customers.png", "customer-form.png"]),
    ("new-invoice", ["new-invoice.png", "new-invoice-2.png"]),
    ("drafts", ["drafts.png"]),
    ("invoices", ["invoices-list.png", "invoice-actions.png"]),
    ("export", ["export.png"]),
    ("new-quote", ["new-quote.png"]),
    ("quotes", ["quotes-list.png"]),
    ("calendar", ["calendar.png"]),
    ("reports", ["reports.png"]),
    ("settings", ["settings-preferences.png", "settings-business.png"]),
    ("backup", ["backup.png"]),
    ("app-lock", ["pin-lock-setup.png"]),
    ("languages", ["language.png"]),
    ("templates", ["template-picker.png", "templates-1.png", "templates-2.png"]),
    ("free-vs-pro", []),
]

def page_name(code: str) -> str:
    return "manual.html" if code == "en" else f"manual-{code}.html"

def build(code: str) -> None:
    T = importlib.import_module(f"lang.{code}").T
    ui = json.loads((HERE / "ui" / f"{code}.json").read_text())

    def label(key: str) -> str:
        if key not in ui:
            raise KeyError(f"[{code}] unknown UI string '{key}'")
        # drop decorative leading symbols such as "➕  Add Item Details" or "‹ Back"
        return html.escape(re.sub(r"^[^\w]+", "", ui[key]), quote=False)

    def u(text: str) -> str:
        return re.sub(r"\{\{([a-z0-9_]+)\}\}", lambda m: label(m.group(1)), text)

    def block(b) -> str:
        kind, body = b
        if kind == "p":
            return f"<p>{u(body)}</p>"
        if kind == "ul":
            return "<ul>" + "".join(f"<li>{u(i)}</li>" for i in body) + "</ul>"
        if kind == "note":
            return f'<div class="note">{u(body)}</div>'
        if kind == "warn":
            return f'<div class="note warn">{u(body)}</div>'
        raise ValueError(kind)

    secs = T["sections"]
    missing = [sid for sid, _ in ORDER if sid not in secs]
    if missing:
        raise KeyError(f"[{code}] missing sections: {missing}")

    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{c}" href="{page_name(c)}">' for c, _ in LANGS
    ) + '\n<link rel="alternate" hreflang="x-default" href="manual.html">'
    langbar = " ".join(
        f'<a href="{page_name(c)}" lang="{c}" hreflang="{c}"' + (' class="current" aria-current="page"' if c == code else "") + f">{n}</a>"
        for c, n in LANGS
    )
    toc = "\n".join(f'        <li><a href="#{sid}">{html.escape(secs[sid][0])}</a></li>' for sid, _ in ORDER)

    sections = []
    for n, (sid, shots) in enumerate(ORDER, 1):
        title, blocks = secs[sid]
        figs = []
        for f in shots:
            if (SITE / "assets/screenshots" / f).exists():
                alt = html.escape(f"{T['brand_alt']} — {title}")
                figs.append(f'<figure class="shot"><img src="assets/screenshots/{f}" alt="{alt}" loading="lazy"></figure>')
            else:
                print(f"  warning: missing screenshot {f}")
        fig_html = ""
        if figs:
            fig_html = f'\n        <div class="shots">{"".join(figs)}</div>' if len(figs) > 1 else f"\n        {figs[0]}"
        sections.append(
            f'''    <section class="section" id="{sid}">
      <h2><span class="num">{n}</span> {html.escape(title)}</h2>
      <div class="section-body">
        <div>
          {chr(10).join("          " + block(b) for b in blocks).lstrip()}
        </div>{fig_html}
      </div>
    </section>
'''
        )

    out = f'''<!doctype html>
<html lang="{code}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Invoice Cove — {html.escape(T["title"])}</title>
<meta name="description" content="{html.escape(T["meta_desc"])}">
{alternates}
<link rel="icon" href="assets/icon-256.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>

<nav class="topnav">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="assets/icon-256.png" alt=""> Invoice Cove</a>
    <div class="navlinks">
      <a href="index.html">Home</a>
      <a href="manual.html" class="active">User Manual</a>
      <a href="privacy.html">Privacy Policy</a>
      <a href="terms.html">Terms of Use</a>
    </div>
  </div>
</nav>

<header class="hero" style="padding-bottom:0;">
  <div class="wrap" style="padding-bottom:36px;">
    <h1>{html.escape(T["title"])}</h1>
    <p>{html.escape(T["subtitle"])}</p>
  </div>
  <svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M0,32 C240,64 480,0 720,20 C960,40 1200,60 1440,28 L1440,60 L0,60 Z" fill="#f5f9fd"></path>
  </svg>
</header>

<main>
  <div class="wrap">

    <nav class="langbar" aria-label="{html.escape(T["lang_label"])}"><span aria-hidden="true">🌐</span> {langbar}</nav>

    <p class="lede">{u(T["lede"])}</p>
    <div class="note warn">
      {u(T["warn"])}
    </div>

    <div class="toc">
      <h2>{html.escape(T["toc"])}</h2>
      <ol>
{toc}
      </ol>
    </div>

{chr(10).join(sections)}
  </div>
</main>

<footer>
  <div class="wrap">
    <span>Invoice Cove — a <a class="accent" href="https://magotel.uk" target="_blank" rel="noopener">Magotel</a> app</span>
    <span>{html.escape(T["footer_questions"])} <a href="mailto:contact@magotel.uk">contact@magotel.uk</a></span>
  </div>
</footer>

</body>
</html>
'''
    (SITE / page_name(code)).write_text(out)
    print(f"built {page_name(code)}")

if __name__ == "__main__":
    only = sys.argv[1:] or [c for c, _ in LANGS]
    for c in only:
        build(c)
