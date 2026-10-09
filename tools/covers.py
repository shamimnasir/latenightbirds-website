#!/usr/bin/env python3
"""Generates a unique 720x480 cover image for each new article.

Run from the repo root:  python3 tools/covers.py
Writes blog/img/cover-<slug>.svg. Each cover has its own palette and a motif that matches the topic.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "blog" / "img"

# Motifs are drawn on a 200x200 grid, then placed with a transform.
MOTIFS = {
    # magnifying glass with a spark: search
    "what-is-ai-seo-and-how-to-do-it": '''
      <circle cx="88" cy="88" r="52" fill="none" stroke="{fg}" stroke-width="16"/>
      <path d="M126 126l48 48" stroke="{fg}" stroke-width="18" stroke-linecap="round"/>
      <path d="M88 60l6 22 22 6-22 6-6 22-6-22-22-6 22-6z" fill="{accent}"/>''',
    # speech bubbles: being quoted
    "how-to-get-cited-by-chatgpt-claude-and-perplexity": '''
      <rect x="20" y="36" width="112" height="72" rx="20" fill="{fg}"/>
      <path d="M50 108l-14 26 34-26z" fill="{fg}"/>
      <rect x="70" y="92" width="112" height="72" rx="20" fill="{accent}"/>
      <path d="M160 164l14 26-34-26z" fill="{accent}"/>
      <circle cx="56" cy="72" r="7" fill="{bg}"/><circle cx="76" cy="72" r="7" fill="{bg}"/><circle cx="96" cy="72" r="7" fill="{bg}"/>''',
    # two chain links: backlinks
    "ethical-link-building-guide": '''
      <rect x="22" y="74" width="92" height="52" rx="26" fill="none" stroke="{fg}" stroke-width="14" transform="rotate(-20 68 100)"/>
      <rect x="86" y="74" width="92" height="52" rx="26" fill="none" stroke="{accent}" stroke-width="14" transform="rotate(-20 132 100)"/>''',
    # gears with circular arrows: automation
    "what-is-marketing-automation-small-business-guide": '''
      <g fill="{fg}"><circle cx="78" cy="100" r="36"/></g>
      <circle cx="78" cy="100" r="14" fill="{bg}"/>
      <g stroke="{fg}" stroke-width="12" stroke-linecap="square"><path d="M78 52v-14M78 148v14M30 100H16M126 100h14M45 67l-10-10M111 133l10 10M111 67l10-10M45 133l-10 10"/></g>
      <circle cx="136" cy="128" r="26" fill="{accent}"/>
      <circle cx="136" cy="128" r="9" fill="{bg}"/>''',
    # calendar with rising bars: timelines and growth
    "how-long-does-seo-take": '''
      <rect x="24" y="44" width="152" height="130" rx="18" fill="{fg}"/>
      <rect x="24" y="44" width="152" height="34" rx="18" fill="{accent}"/>
      <rect x="44" y="104" width="20" height="46" rx="4" fill="{bg}"/>
      <rect x="76" y="90" width="20" height="60" rx="4" fill="{bg}"/>
      <rect x="108" y="76" width="20" height="74" rx="4" fill="{bg}"/>
      <rect x="140" y="60" width="20" height="90" rx="4" fill="{bg}"/>''',
    # stacked pages with pen: content strategy
    "content-marketing-strategy-step-by-step": '''
      <rect x="30" y="60" width="110" height="100" rx="12" fill="{fg}" opacity=".45"/>
      <rect x="50" y="44" width="110" height="100" rx="12" fill="{fg}" opacity=".75"/>
      <rect x="70" y="28" width="110" height="100" rx="12" fill="{fg}"/>
      <path d="M92 60h66M92 80h50M92 100h60" stroke="{bg}" stroke-width="7" stroke-linecap="round"/>
      <path d="M150 170l24-44 10 6-24 44-14 4z" fill="{accent}"/>''',
    # rocket with checklist: launch
    "website-launch-marketing-checklist": '''
      <path d="M100 18c30 22 40 60 36 96H64c-4-36 6-74 36-96z" fill="{fg}"/>
      <circle cx="100" cy="82" r="13" fill="{bg}"/>
      <path d="M64 96L40 124v26l24-18zM136 96l24 28v26l-24-18z" fill="{accent}"/>
      <path d="M86 118l-10 40 14-10 10 14 10-30z" fill="{accent}" opacity=".9"/>''',
    # toolbox with sparkles: AI tools
    "best-ai-tools-for-content-marketing": '''
      <rect x="26" y="86" width="148" height="88" rx="14" fill="{fg}"/>
      <path d="M70 86V66a14 14 0 0 1 14-14h32a14 14 0 0 1 14 14v20" fill="none" stroke="{fg}" stroke-width="12"/>
      <rect x="26" y="116" width="148" height="10" fill="{bg}" opacity=".5"/>
      <path d="M150 28l5 12 12 5-12 5-5 12-5-12-12-5 12-5z" fill="{accent}"/>
      <path d="M42 30l3 7 7 3-7 3-3 7-3-7-7-3 7-3z" fill="{accent}"/>''',
    # document with check and cross: quality vs thin content
    "does-ai-generated-content-hurt-seo": '''
      <rect x="28" y="22" width="104" height="136" rx="14" fill="{fg}"/>
      <path d="M50 58h60M50 80h60M50 102h40" stroke="{bg}" stroke-width="7" stroke-linecap="round"/>
      <circle cx="140" cy="132" r="32" fill="{accent}"/>
      <path d="M126 132l10 10 20-22" fill="none" stroke="{bg}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>''',
    # envelope with lightning: email automation
    "email-automation-workflows-every-business-needs": '''
      <rect x="20" y="58" width="128" height="92" rx="12" fill="{fg}"/>
      <path d="M26 66l58 46 58-46" fill="none" stroke="{bg}" stroke-width="8" stroke-linejoin="round"/>
      <path d="M150 34l-18 34h16l-10 30 28-40h-16l10-24z" fill="{accent}"/>''',
    # terminal window with a prompt: Claude prompts
    "how-to-automate-seo-with-claude": '''
      <rect x="14" y="36" width="172" height="128" rx="14" fill="{fg}"/>
      <rect x="14" y="36" width="172" height="26" rx="12" fill="{accent}"/>
      <circle cx="32" cy="49" r="5" fill="{bg}"/><circle cx="48" cy="49" r="5" fill="{bg}"/><circle cx="64" cy="49" r="5" fill="{bg}"/>
      <path d="M36 88l20 14-20 14" fill="none" stroke="{bg}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
      <rect x="70" y="112" width="60" height="9" rx="4" fill="{bg}"/>''',
}

# Palettes: (sky top, sky bottom, foreground, accent, background used inside motif)
PALETTES = {
    "what-is-ai-seo-and-how-to-do-it": ("#1d2a5e", "#4b6cb7", "#ffffff", "#f6d58e", "#1d2a5e"),
    "how-to-get-cited-by-chatgpt-claude-and-perplexity": ("#2a1f55", "#7b5ea7", "#fffefd", "#f3b9c8", "#2a1f55"),
    "ethical-link-building-guide": ("#0f3d3e", "#2c8c86", "#fffefd", "#f6d58e", "#0f3d3e"),
    "what-is-marketing-automation-small-business-guide": ("#2b1d3f", "#8a4f7d", "#fffefd", "#ffb36b", "#2b1d3f"),
    "how-long-does-seo-take": ("#152a3f", "#3f7b9c", "#fffefd", "#ffd166", "#152a3f"),
    "content-marketing-strategy-step-by-step": ("#3a1f2b", "#b65c6e", "#fffefd", "#ffe08a", "#3a1f2b"),
    "website-launch-marketing-checklist": ("#101a3a", "#2e4f8f", "#fffefd", "#ff9f5a", "#101a3a"),
    "best-ai-tools-for-content-marketing": ("#1c1f2e", "#5b4bb7", "#fffefd", "#7fe0c4", "#1c1f2e"),
    "does-ai-generated-content-hurt-seo": ("#2a2a3d", "#6e6a9a", "#fffefd", "#ffb4a2", "#2a2a3d"),
    "email-automation-workflows-every-business-needs": ("#14283a", "#2f6f8f", "#fffefd", "#f6d58e", "#14283a"),
    "how-to-automate-seo-with-claude": ("#0d1f2d", "#2a6f97", "#fffefd", "#f6d58e", "#0d1f2d"),
}

# A few stars per cover, placed differently so each sky looks distinct.
STARS = [(40, 40), (250, 60), (300, 180), (560, 50), (640, 130), (520, 300), (120, 260), (680, 330), (300, 420), (420, 30)]


def cover(slug):
    top, bottom, fg, accent, bg = PALETTES[slug]
    motif = MOTIFS[slug].format(fg=fg, accent=accent, bg=bg)
    stars = "".join(f'<circle cx="{x}" cy="{y}" r="{1.4 + (i % 3) * 0.5}" fill="#fffefd" opacity=".85"/>'
                    for i, (x, y) in enumerate(STARS) if (i + len(slug)) % 2 == 0 or i % 3 == 0)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 480" preserveAspectRatio="xMidYMid slice">
  <defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/></linearGradient>
  <radialGradient id="glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{accent}" stop-opacity=".35"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient></defs>
  <rect width="720" height="480" fill="url(#g)"/>
  <circle cx="360" cy="240" r="260" fill="url(#glow)"/>
  {stars}
  <g transform="translate(260 120) scale(1.4)">{motif}
  </g>
  <rect y="430" width="720" height="50" fill="#0c0e22" opacity=".35"/>
</svg>
'''


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for slug in PALETTES:
        (OUT / f"cover-{slug}.svg").write_text(cover(slug), encoding="utf-8")
    print(f"wrote {len(PALETTES)} covers to {OUT}")


if __name__ == "__main__":
    main()
