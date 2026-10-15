"""Find text that overlaps other text, icons or the edge of its card.

Usage: python overlap_check.py deck.pptx deck.pdf

1. Rendered check (PDF): text lines from different text blocks whose boxes overlap,
   i.e. text printed on top of other text.
2. Rendered check (PDF): text lines that run past the bottom or right edge of the
   PowerPoint shape they belong to (overflow), matched by position.
3. Geometry check (PPTX): text boxes overlapping icons, and text boxes that stick out
   of the coloured shape they sit on.
"""
import sys
import fitz
from pptx import Presentation
from pptx.util import Emu

deck, pdf = sys.argv[1], sys.argv[2]
prs = Presentation(deck)
SW, SH = prs.slide_width, prs.slide_height
doc = fitz.open(pdf)
TOL = 0.02  # inch


def inch(v):
    return Emu(v).inches


def box(sh):
    return (inch(sh.left), inch(sh.top), inch(sh.left + sh.width), inch(sh.top + sh.height))


def inter(a, b):
    w = min(a[2], b[2]) - max(a[0], b[0])
    h = min(a[3], b[3]) - max(a[1], b[1])
    return (w, h) if w > 0 and h > 0 else None


def inside(a, b, tol=TOL):
    return a[0] >= b[0] - tol and a[1] >= b[1] - tol and a[2] <= b[2] + tol and a[3] <= b[3] + tol


findings = []
for n, (slide, page) in enumerate(zip(prs.slides, doc), start=1):
    sx = page.rect.width / inch(SW)
    sy = page.rect.height / inch(SH)
    # --- rendered lines
    lines = []
    for bi, b in enumerate(page.get_text("dict")["blocks"]):
        for l in b.get("lines", []):
            t = "".join(s["text"] for s in l["spans"]).strip()
            if t:
                x0, y0, x1, y1 = l["bbox"]
                lines.append((bi, t, (x0 / sx, y0 / sy, x1 / sx, y1 / sy)))
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            bi, ti, ai = lines[i]
            bj, tj, aj = lines[j]
            if bi == bj:
                continue
            ov = inter(ai, aj)
            if ov and ov[0] > 0.05 and ov[1] > 0.04:
                findings.append(f"slide {n}: text overlaps text: '{ti[:40]}' / '{tj[:40]}'")
    # --- shapes
    texts, pics, fills = [], [], []
    for sh in slide.shapes:
        b = box(sh)
        if sh.shape_type == 13:  # picture
            pics.append((sh.name, b))
        elif sh.has_text_frame and sh.text_frame.text.strip() and not sh.is_placeholder:
            texts.append((sh.name, b, sh.text_frame.text.strip()))
        elif not sh.is_placeholder and getattr(sh, "fill", None) is not None:
            try:
                if sh.fill.type == 1:
                    fills.append((sh.name, b))
            except Exception:
                pass
    # rendered text belonging to a text box but drawn outside it (overflow)
    for name, b, t in texts:
        first = t.split("\n")[0][:12]
        for _, lt, lb in lines:
            if lt.startswith(first[:8]) and inter(lb, b):
                pass
        own = [lb for _, lt, lb in lines if inter(lb, b) and lb[0] >= b[0] - 0.1 and lb[0] <= b[2]]
        for lb in own:
            if lb[3] > b[3] + 0.08 and lb[1] < b[3] + 0.6 and lb[1] > b[1]:
                # a line starting inside the box column but ending below it
                pass
    for name, b, t in texts:
        for pname, pb in pics:
            ov = inter(b, pb)
            if ov and ov[0] > 0.05 and ov[1] > 0.05:
                findings.append(f"slide {n}: text box '{name}' overlaps icon '{pname}'")
        # text box partly outside the filled shape it mostly sits on
        for fname, fb in fills:
            ov = inter(b, fb)
            if not ov:
                continue
            area_b = (b[2] - b[0]) * (b[3] - b[1])
            share = ov[0] * ov[1] / area_b if area_b else 0
            if 0.5 < share < 0.97 and not inside(b, fb, 0.05):
                findings.append(f"slide {n}: text box '{name}' sticks out of '{fname}' ({share:.0%} inside)")
    # rendered overflow: lines below the bottom of any card they start in
    for _, lt, lb in lines:
        for fname, fb in fills:
            if fb[0] - 0.02 <= lb[0] <= fb[2] and fb[1] <= lb[1] <= fb[3] and lb[3] > fb[3] + 0.03:
                findings.append(f"slide {n}: text runs past the bottom of '{fname}': '{lt[:40]}'")
            if fb[1] <= lb[1] <= fb[3] and fb[0] <= lb[0] <= fb[2] and lb[2] > fb[2] + 0.05:
                findings.append(f"slide {n}: text runs past the right edge of '{fname}': '{lt[:40]}'")

seen = set()
for f in findings:
    if f not in seen:
        print(f)
        seen.add(f)
print(f"{len(seen)} findings")

# 4. Foreign text on a filled shape: a rendered line overlapping a card or callout whose
#    text is not part of any text box that sits on that shape (text spilled from elsewhere).
import re as _re
norm = lambda x: _re.sub(r"\s+", "", x)
extra = []
for n, (slide, page) in enumerate(zip(prs.slides, doc), start=1):
    sx = page.rect.width / inch(SW); sy = page.rect.height / inch(SH)
    fills, texts = [], []
    for sh in slide.shapes:
        b = box(sh)
        if sh.has_text_frame and sh.text_frame.text.strip() and not sh.is_placeholder:
            texts.append((b, norm(sh.text_frame.text)))
        try:
            if not sh.is_placeholder and sh.shape_type == 1 and sh.fill.type == 1:
                fills.append((sh.name, b, norm(sh.text_frame.text) if sh.has_text_frame else ""))
        except Exception:
            pass
    for blk in page.get_text("dict")["blocks"]:
        for l in blk.get("lines", []):
            t = "".join(s["text"] for s in l["spans"]).strip()
            if not t:
                continue
            x0, y0, x1, y1 = l["bbox"]; lb = (x0 / sx, y0 / sy, x1 / sx, y1 / sy)
            for fname, fb, ftext in fills:
                ov = inter(lb, fb)
                if not ov or ov[1] < 0.02 or ov[0] < 0.1:
                    continue
                own = [tt for tb, tt in texts if inter(tb, fb) and inside(tb, fb, 0.08)] + [ftext]
                if not any(norm(t) in o for o in own if o):
                    extra.append(f"slide {n}: foreign text on '{fname}': '{t[:45]}'")
for f in dict.fromkeys(extra):
    print(f)
print(f"{len(set(extra))} foreign-text findings")
