"""Build the German lecture Kundenbindung, Abwanderung und Share of Wallet on the WU 16:10 template (polish-slides patterns)."""
import sys
from lxml import etree
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION

TEMPLATE, OUT = sys.argv[1], sys.argv[2]
ICONS = "icons"
FOOTER = "How Brands Grow | Marketing Science"
NB = " "  # non-breaking space between numbers and units

T = MSO_THEME_COLOR
NAVY, BLUE, LIGHT, WHITE, BLACK = T.TEXT_2, T.ACCENT_1, T.BACKGROUND_2, T.BACKGROUND_1, T.TEXT_1
GREY_FILL, GREY_TEXT = RGBColor(0xF2, 0xF2, 0xF2), RGBColor(0x59, 0x59, 0x59)
HEAD = "+mj-lt"  # theme heading font (Georgia)

prs = Presentation(TEMPLATE)
for sldId in list(prs.slides._sldIdLst):          # drop the template's sample slides
    prs.part.drop_rel(sldId.rId)
    prs.slides._sldIdLst.remove(sldId)
LAY = {l.name: l for l in prs.slide_layouts}

X0, W0 = 0.5, 9.0          # content area
GAP = 0.18                 # one gap size for cards on every slide


# ------------------------------------------------------------------ helpers
def colour(fmt, c):
    if isinstance(c, RGBColor):
        fmt.rgb = c
    else:
        fmt.theme_color = c


def lang(run):
    run.font._rPr.set("lang", "en-GB")


def text(slide, x, y, w, h, paras, size=13, color=BLACK, bold=False, head=False,
         align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, name=None, space=6):
    """paras: str | list of paragraphs; paragraph: str | list of (text, opts)."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    if name:
        tb.name = name
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.04)
    tf.margin_top = tf.margin_bottom = Inches(0.02)
    tf.vertical_anchor = anchor
    for i, para in enumerate(paras if isinstance(paras, list) else [paras]):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(space)
        for seg in (para if isinstance(para, list) else [para]):
            t, o = (seg, {}) if isinstance(seg, str) else seg
            r = p.add_run()
            r.text = t
            lang(r)
            f = r.font
            f.size = Pt(o.get("size", size))
            f.bold = o.get("bold", bold)
            f.italic = o.get("italic", False)
            if o.get("head", head):
                f.name = HEAD
            colour(f.color, o.get("color", color))
            if o.get("sub"):
                f._rPr.set("baseline", "-25000")
    return tb


def rect(slide, x, y, w, h, fill=LIGHT, shape=MSO_SHAPE.RECTANGLE, name=None):
    s = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    s.fill.solid()
    colour(s.fill.fore_color, fill)
    s.line.fill.background()
    s.shadow.inherit = False
    if name:
        s.name = name
    return s


def icon(slide, name, x, y, size=0.4, tone="navy"):
    pic = slide.shapes.add_picture(f"{ICONS}/{name}-{tone}.png", Inches(x), Inches(y),
                                   Inches(size), Inches(size))
    pic.name = f"Icon {name}"
    return pic


def number(slide, x, y, n, d=0.42, fill=BLUE, size=14, name=None):
    c = rect(slide, x, y, d, d, fill=fill, shape=MSO_SHAPE.OVAL, name=name or f"Number {n}")
    tf = c.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = str(n)
    lang(r)
    r.font.size = Pt(size); r.font.bold = True; r.font.name = HEAD
    colour(r.font.color, WHITE)
    return c


def band_card(slide, x, y, w, h, head, body, icon_name=None, band=BLUE, body_size=13,
              name="Card", fill=LIGHT, body_color=BLACK):
    """Card with a solid header band (icon in its right corner) and a light body."""
    rect(slide, x, y, w, h, fill=fill, name=f"{name} body")
    rect(slide, x, y, w, 0.5, fill=band, name=f"{name} band")
    text(slide, x + 0.12, y + 0.06, w - 0.75, 0.4, head, size=15, bold=True, head=True,
         color=WHITE, anchor=MSO_ANCHOR.MIDDLE, name=f"{name} heading")
    if icon_name:
        icon(slide, icon_name, x + w - 0.47, y + 0.07, 0.36, "white")
    text(slide, x + 0.15, y + 0.62, w - 0.3, h - 0.72, body, size=body_size,
         color=body_color, name=f"{name} text", space=7)


def callout(slide, y, txt, h=0.55, name="Callout", fill=NAVY, color=WHITE, size=13):
    rect(slide, X0, y, W0, h, fill=fill, name=name)
    text(slide, X0 + 0.2, y, W0 - 0.4, h, txt, size=size, color=color,
         anchor=MSO_ANCHOR.MIDDLE, name=f"{name} text", space=0)


def caption(slide, txt, y):
    text(slide, X0, y, W0, 0.35, txt, size=10.5, color=GREY_TEXT, name="Source note", space=0)


def footer(slide):
    """Footer text and page number per slide (the template asks not to change the master)."""
    for ph in slide.slide_layout.placeholders:
        t = ph.placeholder_format.type
        if t is None:
            continue
        tn = str(t)
        if "FOOTER" in tn or "SLIDE_NUMBER" in tn:
            el = slide.shapes.clone_placeholder(ph)
    for sh in slide.placeholders:
        tn = str(sh.placeholder_format.type)
        if "FOOTER" in tn:
            sh.text_frame.text = FOOTER
            lang(sh.text_frame.paragraphs[0].runs[0])
        elif "SLIDE_NUMBER" in tn:
            p = sh.text_frame.paragraphs[0]
            r = p.add_run(); r.text = "SEITE "; lang(r)
            fld = etree.SubElement(p._p, "{http://schemas.openxmlformats.org/drawingml/2006/main}fld")
            fld.set("id", "{B6F15528-21DE-4FAA-801E-634DDDAF4B2B}")
            fld.set("type", "slidenum")
            etree.SubElement(fld, "{http://schemas.openxmlformats.org/drawingml/2006/main}rPr").set("lang", "en-GB")
            etree.SubElement(fld, "{http://schemas.openxmlformats.org/drawingml/2006/main}t").text = "‹#›"


def drop_empty(slide, keep=(0,)):
    for ph in list(slide.placeholders):
        tn = str(ph.placeholder_format.type)
        if ph.placeholder_format.idx in keep or "FOOTER" in tn or "SLIDE_NUMBER" in tn:
            continue
        if not ph.has_text_frame or not ph.text_frame.text.strip():
            ph._element.getparent().remove(ph._element)


def content(title, layout="Titel und Inhalt"):
    s = prs.slides.add_slide(LAY[layout])
    s.shapes.title.text = title
    lang(s.shapes.title.text_frame.paragraphs[0].runs[0])
    drop_empty(s)
    footer(s)
    return s


def section(n, title, line, notes_text):
    s = prs.slides.add_slide(LAY["Kapitelfolie"])
    s.shapes.title.text = title
    for ph in s.placeholders:
        if ph.placeholder_format.idx == 11:
            ph.text_frame.text = f"Part {n} of 6 · {line}"
    drop_empty(s, keep=(0, 11))
    footer(s)
    notes(s, notes_text)
    return s


def notes(slide, t):
    slide.notes_slide.notes_text_frame.text = t


def stepper(slide, labels, y=1.4, current=None, h=0.55):
    n = len(labels)
    w = (W0 + 0.12 * (n - 1)) / n
    for i, lab in enumerate(labels):
        shape = MSO_SHAPE.PENTAGON if i == 0 else MSO_SHAPE.CHEVRON
        on = current is None or i == current
        s = rect(slide, X0 + i * (w - 0.12), y, w, h, fill=NAVY if on else LIGHT, shape=shape,
                 name=f"Step {i + 1}")
        tf = s.text_frame
        tf.margin_left = Inches(0.25); tf.margin_right = Inches(0.1)
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = lab; lang(r)
        r.font.size = Pt(13); r.font.bold = True
        colour(r.font.color, WHITE if on else NAVY)
    return w

FOOTER = "Customer Loyalty, Churn and Share of Wallet"
cw = (W0 - GAP) / 2
cw3 = (W0 - 2 * GAP) / 3


def bar_chart(slide, x, y, w, h, cats, vals, title, fmt, maxv, name, horizontal=False, colors=None):
    cd = CategoryChartData()
    cd.categories = cats
    cd.add_series(title, vals)
    kind = XL_CHART_TYPE.BAR_CLUSTERED if horizontal else XL_CHART_TYPE.COLUMN_CLUSTERED
    gf = slide.shapes.add_chart(kind, Inches(x), Inches(y), Inches(w), Inches(h), cd)
    gf.name = name
    ch = gf.chart
    ch.has_title = True
    ch.chart_title.text_frame.text = title
    r = ch.chart_title.text_frame.paragraphs[0].runs[0]
    r.font.size = Pt(13); r.font.bold = True; colour(r.font.color, NAVY); lang(r)
    ch.has_legend = False
    pl = ch.plots[0]
    pl.gap_width = 60
    pl.has_data_labels = True
    dl = pl.data_labels
    dl.number_format = fmt; dl.number_format_is_linked = False
    dl.position = XL_LABEL_POSITION.OUTSIDE_END
    dl.font.size = Pt(11); colour(dl.font.color, NAVY)
    ser = pl.series[0]
    ser.format.fill.solid(); colour(ser.format.fill.fore_color, BLUE)
    for i, c in enumerate(colors or []):
        if c is not None:
            pt = ser.points[i]
            pt.format.fill.solid(); colour(pt.format.fill.fore_color, c)
    va = ch.value_axis
    va.maximum_scale = maxv; va.minimum_scale = 0
    va.major_gridlines.format.line.color.rgb = RGBColor(0xD9, 0xD9, 0xD9)
    va.tick_labels.font.size = Pt(10.5); va.tick_labels.font.color.rgb = GREY_TEXT
    va.tick_labels.number_format = fmt; va.tick_labels.number_format_is_linked = False
    va.format.line.fill.background()
    ca = ch.category_axis
    ca.tick_labels.font.size = Pt(11); ca.tick_labels.font.color.rgb = GREY_TEXT
    if horizontal:
        ca.reverse_order = True
    return gf


def stat_rows(slide, stats, y0=1.4, step=1.0, prefix="Stat"):
    for i, (fig, lab, src) in enumerate(stats):
        y = y0 + i * step
        rect(slide, X0, y + 0.08, 0.07, 0.72, fill=BLUE, name=f"{prefix} bar {i + 1}")
        text(slide, X0 + 0.2, y, 2.0, 0.85, fig, size=28, bold=True, head=True, color=NAVY,
             anchor=MSO_ANCHOR.MIDDLE, name=f"{prefix} figure {i + 1}", space=0)
        text(slide, X0 + 2.3, y + 0.05, W0 - 2.3, 0.8,
             [[(lab, {})], [(src, {"size": 10.5, "color": GREY_TEXT})]], size=13,
             name=f"{prefix} text {i + 1}", space=2)


def table(slide, rows, x, y, w, h, widths, name, size=12, first_col_dark=False, highlight=()):
    gt = slide.shapes.add_table(len(rows), len(rows[0]), Inches(x), Inches(y), Inches(w), Inches(h))
    gt.name = name
    tb = gt.table
    for c, cw_ in enumerate(widths):
        tb.columns[c].width = Inches(cw_)
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            cell = tb.cell(r, c)
            cell.text = val
            p = cell.text_frame.paragraphs[0]
            run = p.runs[0] if p.runs else p.add_run()
            lang(run)
            f = run.font; f.size = Pt(size)
            cell.fill.solid()
            if r == 0:
                colour(cell.fill.fore_color, BLUE); colour(f.color, WHITE); f.bold = True
            elif c == 0 and first_col_dark:
                colour(cell.fill.fore_color, NAVY); colour(f.color, WHITE); f.bold = True
            else:
                colour(cell.fill.fore_color, LIGHT); colour(f.color, BLACK)
            if (r, c) in highlight:
                colour(cell.fill.fore_color, T.ACCENT_6); f.bold = True
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    return tb


def stepper(slide, labels, y=1.4, current=None, h=0.55, size=13):
    n = len(labels)
    w = (W0 + 0.12 * (n - 1)) / n
    for i, lab in enumerate(labels):
        shape = MSO_SHAPE.PENTAGON if i == 0 else MSO_SHAPE.CHEVRON
        on = current is None or i == current
        s = rect(slide, X0 + i * (w - 0.12), y, w, h, fill=NAVY if on else LIGHT, shape=shape, name=f"Step {i + 1}")
        tf = s.text_frame
        tf.margin_left = Inches(0.22); tf.margin_right = Inches(0.08)
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = lab; lang(r)
        r.font.size = Pt(size); r.font.bold = True
        colour(r.font.color, WHITE if on else NAVY)
    return w

# German slide content. Appended after the helper block and the English chart/table helpers.
FOOTER = "Loyalität, Churn und Share of Wallet"


def lang(run):  # noqa: F811  German proofing language
    run.font._rPr.set("lang", "de-AT")


def section(n, title, line, notes_text):  # noqa: F811
    s = prs.slides.add_slide(LAY["Kapitelfolie"])
    s.shapes.title.text = title
    for ph in s.placeholders:
        if ph.placeholder_format.idx == 11:
            ph.text_frame.text = f"Teil {n} von 6 · {line}"
    drop_empty(s, keep=(0, 11))
    footer(s)
    notes(s, notes_text)
    return s


# ================================================================== Folien
# 1  Titel
s = prs.slides.add_slide(LAY["Titelfolie Kontakt"])
s.shapes.title.text = "Loyalität, Churn und Share of Wallet"
for ph in s.placeholders:
    if ph.placeholder_format.idx == 1:
        ph.text_frame.text = "Kennzahlen und Unternehmenserfolg"
    elif ph.placeholder_format.idx == 12:
        ph.text_frame.text = "Oktober 2026"
notes(s, "Etwa 100 Minuten in sechs Teilen: Begriffe und Kennzahlen, die Service-Profit-Chain, Ansätze, die Kunden mit "
         "dem Unternehmenswert verbinden, Abwanderung (Churn), Share of Wallet sowie Kritik mit Anwendungsteil. "
         "Kernliteratur: Heskett et al. (1994) HBR; Gupta & Zeithaml (2006) Marketing Science; Hogreve et al. (2017) "
         "Journal of Marketing; Keiningham et al. (2015) Journal of Service Management. Alle Quellen mit "
         "Zugangshinweisen stehen auf der Notion-Seite und im GitHub-Ordner zu diesem Thema.")

# 2  Zwei Sichtweisen
s = content("Zahlt sich Kundenbindung aus?")
band_card(s, X0, 1.4, cw, 2.9, "Bindung zahlt sich aus",
          [[("Service-Profit-Chain: ", {"bold": True}), "zufriedene Mitarbeitende und Kunden steigern den Gewinn"],
           [("Retention-Ökonomie: ", {"bold": True}), "5 % weniger Abwanderung, 25 % mehr Gewinn"],
           [("Customer Equity: ", {"bold": True}), "Bindung ist der stärkste Hebel auf den Firmenwert"]],
          icon_name="LuHeartHandshake", body_size=14, name="Loyalty pays")
band_card(s, X0 + cw + GAP, 1.4, cw, 2.9, "Bindung reicht nicht",
          [[("Reinartz & Kumar: ", {"bold": True}), "treue Kunden sind nicht immer profitabel"],
           [("Keiningham: ", {"bold": True}), "Zufriedenheit bewegt den Share of Wallet kaum"],
           [("Ehrenberg-Bass: ", {"bold": True}), "Wachstum kommt von mehr Käufern, nicht mehr Treue"]],
          icon_name="LuScale", band=T.ACCENT_4, body_size=14, name="Loyalty is not enough")
callout(s, 4.5, "Heute: die Kette vom Kunden zum Firmenwert verfolgen und jedes Glied an der Evidenz prüfen.",
        name="Central question")
notes(s, "Kurze Umfrage: Welcher Spalte glauben Sie? Die Praxis folgt meist der linken Spalte (Bonusprogramme, "
         "NPS-Ziele, Retention-Teams). Die rechte Spalte sammelt die wichtigsten empirischen Einwände; Teil 6 greift "
         "die Spannung wieder auf. Die Zahl 5 %/25 % stammt von Reichheld für Finanzdienstleistungen (Bain Brief "
         "2001); die oft zitierten '25 bis 95 %' stehen nicht in dieser Quelle.")

# 3  Lernziele
s = content("Lernziele")
objs = [("LuGauge", "Definieren", "Kundenbindung, Abwanderung und Share of Wallet, und jede korrekt messen"),
        ("LuLink", "Erklären", "die Service-Profit-Chain und die Satisfaction-Profit-Chain"),
        ("LuCoins", "Verbinden", "Kundenbindung und Customer Equity mit Firmenwert und Aktienrendite"),
        ("LuWallet", "Anwenden", "CLV, Churn-Targeting und die Wallet Allocation Rule auf Daten"),
        ("LuScale", "Bewerten", "wo die Kette bricht: NPS, Bonusprogramme, Double Jeopardy")]
for i, (ic, verb, rest) in enumerate(objs):
    y = 1.35 + i * 0.8
    rect(s, X0, y, W0, 0.68, name=f"Objective row {i + 1}")
    icon(s, ic, X0 + 0.22, y + 0.14, 0.4)
    text(s, X0 + 0.85, y, W0 - 1.0, 0.68, [[(verb + " ", {"bold": True, "color": NAVY}), rest]],
         size=14, anchor=MSO_ANCHOR.MIDDLE, name=f"Objective text {i + 1}", space=0)
notes(s, "Die Lernziele folgen den sechs Teilen. Das Lab in Teil 6 prüft die Ziele 1 und 4 mit Daten, die Debatte "
         "prüft Ziel 5.")

# ------------------------------------------------------------------ Teil 1
section(1, "Begriffe und Kennzahlen", "was wir messen",
        "Teil 1, etwa 15 Minuten: Definition und Messung von Kundenbindung, Abwanderung und Share of Wallet.")

# 5  Drei Ergebnisgrößen
s = content("Drei Ergebnisgrößen, drei Fragen")
cards = [("Kundenbindung", "Bleiben Kunden und bevorzugen sie uns?",
          [[("Verhalten: ", {"bold": True}), "Wiederkauf"], [("Einstellung: ", {"bold": True}), "relative Präferenz"],
           [("Echte Loyalität braucht beides ", {"bold": True}), "(Dick & Basu 1994)"]], "LuHeartHandshake"),
         ("Abwanderung", "Verlassen uns Kunden?",
          [[("Vertraglich: ", {"bold": True}), "Kündigung ist sichtbar"], [("Nicht vertraglich: ", {"bold": True}), "Kunden werden still, Abwanderung muss geschätzt werden"],
           [("Bindungsrate ", {"bold": True}), "r = 1 − Churn"]], "LuUserMinus"),
         ("Share of Wallet", "Welchen Anteil ihrer Ausgaben bekommen wir?",
          [[("SOW ", {"bold": True}), "= unser Umsatz ÷ Kategorieausgaben"], [("Braucht ", {"bold": True}), "Ausgaben bei Mitbewerbern, meist aus Befragungen"],
           [("Teilabwanderung ", {"bold": True}), "zeigt sich hier zuerst"]], "LuWallet")]
for i, (h, q, body, ic) in enumerate(cards):
    x = X0 + i * (cw3 + GAP)
    band_card(s, x, 1.4, cw3, 2.9, h, [[(q, {"bold": True, "color": NAVY})]] + body,
              icon_name=ic, band=BLUE if i != 1 else NAVY, body_size=12, name=f"Outcome {h}")
callout(s, 4.5, [[("Verbindung zum Firmenwert: ", {"bold": True}),
                  "die Bindungsrate bestimmt, wie lange Kunden zahlen, der SOW wie viel; zusammen treiben sie den CLV."]],
        h=0.6, name="Outcome callout")
notes(s, "Loyalitätstypen nach Dick & Basu (1994, JAMS): echte, latente, Schein- und keine Loyalität. Oliver (1999): "
         "kognitive, affektive, konative und Handlungsloyalität. Abwanderung: Fader & Hardie unterscheiden vertragliche "
         "und nicht vertragliche Settings; davon hängt das Modell ab (sBG bzw. BG/NBD oder Pareto/NBD). Share of "
         "Wallet: Du, Kamakura & Mela (2007) zeigen, dass der eigene Umsatz wenig über die gesamten Ausgaben eines "
         "Kunden aussagt.")

# 6  Kennzahlentabelle
s = content("Die Ergebnisgrößen messen")
rows = [["Kennzahl", "Formel", "Achtung"],
        ["Bindungsrate", "gehaltene ÷ anfängliche Kunden", "Steigt mit der Zeit, weil schwache Kunden gehen"],
        ["Erwartete Dauer", "1 ÷ Churn (nur wenn alle gleich)", "Unterschätzt die Dauer bei Heterogenität"],
        ["CLV", "m · r ÷ (1 + d − r)", "Unterstellt konstante Marge und Bindung"],
        ["Share of Wallet", "unser Umsatz ÷ Kategorieausgaben", "Kategorieausgaben nur aus Befragung oder Panel"],
        ["Net Promoter Score", "% Promotoren − % Detraktoren", "Kein besserer Wachstumsprädiktor"]]
table(s, rows, X0, 1.4, W0, 3.0, [2.1, 3.3, 3.6], "Metrics table", size=12, first_col_dark=True)
caption(s, "Fader & Hardie (2007, 2010); Hardie Notes 024, 033, 049 (brucehardie.com); Farris et al. (2021) Marketing "
           "Metrics, Kap. 2 und 5; Keiningham et al. (2007) Journal of Marketing.", 4.6)
notes(s, "Hardie Note 049: Die durchschnittliche Kundendauer ist nicht 1/Churn, sobald Kunden sich unterscheiden. Fader & "
         "Hardie (2010, Marketing Science) zeigen, dass das Ignorieren von Heterogenität den Wert des Kundenstamms "
         "unterschätzt. Die einfache CLV-Formel m·r/(1+d−r) unterstellt unendlichen Horizont, konstante Marge und "
         "konstante Bindung (Gupta & Lehmann 2005). NPS-Kritik: Keiningham et al. (2007); van Doorn et al. (2013).")

# ------------------------------------------------------------------ Teil 2
section(2, "Die Service-Profit-Chain", "von Mitarbeitenden zum Gewinn",
        "Teil 2, etwa 20 Minuten: die Kette, ihre Evidenz und die Satisfaction-Profit-Chain.")

# 8  Kette
s = content("Die Service-Profit-Chain")
w = stepper(s, ["1", "2", "3", "4", "5", "6"], h=0.5, size=14)
heads = ["Interne Qualität", "Mitarbeitende", "Servicewert", "Zufriedenheit", "Loyalität", "Gewinn"]
expl = ["Werkzeuge, Schulung, Arbeitsplatz", "Zufriedenheit, Verbleib, Produktivität",
        "Nutzen für Kunden im Verhältnis zu Kosten", "Gesamturteil der Kunden",
        "Verbleib, Wiederkauf, Empfehlungen", "Wachstum und Rentabilität"]
for i, t in enumerate(expl):
    x = X0 + i * (w - 0.12)
    rect(s, x + 0.05, 2.05, w - 0.22, 1.75, name=f"Chain box {i + 1}")
    text(s, x + 0.1, 2.2, w - 0.32, 1.2, [[(heads[i], {"bold": True, "color": NAVY, "size": 11})], [(t, {})]], size=12, name=f"Chain text {i + 1}", space=3)
callout(s, 4.05, [[("Die These: ", {"bold": True}),
                   "jedes Glied treibt das nächste; Investitionen in Mitarbeitende und Service zahlen sich im Gewinn aus."]],
        name="Chain claim")
caption(s, "Heskett, Jones, Loveman, Sasser & Schlesinger (1994) Harvard Business Review 72(2); "
           "Heskett, Sasser & Schlesinger (1997) The Service Profit Chain.", 4.75)
notes(s, "Heskett et al. (1994) entwickeln die Kette aus Fallbeispielen (Southwest, Taco Bell, Banc One). Das Buch von "
         "1997 ergänzt den 'Satisfaction Mirror': Mitarbeiter- und Kundenzufriedenheit verstärken sich gegenseitig. "
         "Deutschsprachiges Pendant: die Erfolgskette in Meffert, Bruhn & Hadwich (2018) Dienstleistungsmarketing.")

# 9  Evidenz
s = content("Evidenz: Die Kette hält, mit Bedingungen")
stat_rows(s, [
    ("Alle", "Glieder sind signifikant in einer Metaanalyse der ganzen Kette, aber die Effekte schwanken stark nach Dienstleistungsart.",
     "Hogreve, Iseke, Derfuss & Eller (2017) Journal of Marketing 81(3)"),
    ("+0,5 Pkt.", "Umsatzwachstum bei Sears aus +5 Einheiten Mitarbeitereinstellung, über +1,3 Einheiten Kundeneindruck.",
     "Rucci, Kirn & Quinn (1998) Harvard Business Review"),
    ("Verzug", "zwischen Investition, Zufriedenheit und Erfolg kann Manager zu kurzsichtigen Kürzungen verleiten.",
     "Evanschitzky, von Wangenheim & Wünderlich (2012) Journal of Retailing")], prefix="SPC")
callout(s, 4.45, [[("Aber: ", {"bold": True}),
                   "in britischen Supermärkten trieb Mitarbeiterzufriedenheit den Gewinn nicht (Silvestro 2002); das Mitarbeiterglied ist bedingt."]],
        h=0.65, fill=LIGHT, color=BLACK, name="SPC caveat")
notes(s, "Hogreve et al. (2017) zeigen auch, dass interne Servicequalität über mehr als Mitarbeiterzufriedenheit wirkt; "
         "'Mitarbeiterzufriedenheit maximieren' ist daher keine allgemeine Regel. Brown & Lam (2008, Journal of "
         "Retailing): Mitarbeiterzufriedenheit hängt mit Kundenzufriedenheit zusammen, vollständig vermittelt über die "
         "wahrgenommene Servicequalität. Hogreve, Iseke & Derfuss (2022, JSR) überarbeiten die Kette für digitale und "
         "KI-gestützte Services. Sears-Zahlen vor dem Zitieren am HBR-Original prüfen.")

# 10 Satisfaction-Profit-Chain
s = content("Zufriedenheit zahlt sich aus, aber mäßig")
bar_chart(s, X0, 1.35, 4.4, 3.4, ["Durchschnitt", "Beste Bedingungen"], [0.101, 0.349],
          "Korrelation mit dem Erfolg", "0.00", 0.4, "Chart satisfaction correlation",
          colors=[None, NAVY])
band_card(s, 5.1, 1.4, 4.4, 3.3, "Satisfaction-Profit-Chain",
          [[("Asymmetrisch: ", {"bold": True}), "ein schlechtes Erlebnis schadet mehr, als ein gutes nützt"],
           [("Nicht linear: ", {"bold": True}), "Schwellen und abnehmende Erträge"],
           [("Absicht ≠ Verhalten: ", {"bold": True}), "gleiche Bewertung, andere Wiederkaufraten"],
           [("Kostenseite: ", {"bold": True}), "sehr hohe Zufriedenheit kann mehr kosten, als sie bringt"]],
          icon_name="LuGauge", body_size=12, name="Satisfaction chain")
caption(s, "Otto, Szymanski & Varadarajan (2020) JAMS, 251 Korrelationen; Anderson & Mittal (2000) JSR; Mittal & "
           "Kamakura (2001) JMR; Guenther & Guenther (2021) IJRM; Mittal et al. (2023) Marketing Letters.", 4.95)
notes(s, "Otto et al. (2020): mittleres r = 0,101; r = 0,349 unter den günstigsten Bedingungen (passendes Setting und "
         "passende Maße). Mittal et al. (2023): 535 Korrelationen, N etwa 1,16 Mio., positive Zusammenhänge auf Kunden- "
         "und Firmenebene. Mittal & Kamakura (2001): In einem Segment hängen Zufriedenheit und Wiederkauf nicht "
         "zusammen. Guenther & Guenther (2021): Auf hohem Niveau können die Kosten weiterer Zufriedenheit den Nutzen "
         "übersteigen.")

# ------------------------------------------------------------------ Teil 3
section(3, "Vom Kunden zum Firmenwert", "alternative Ansätze",
        "Teil 3, etwa 20 Minuten: Ansätze über die Service-Profit-Chain hinaus und die Kapitalmarktevidenz.")

# 12 Ansätze
s = content("Sechs Ansätze über die Kette hinaus")
fw = [("Return on Quality", "Qualität ist eine Investition, die sich rechnen muss; man kann zu viel ausgeben.", "Rust, Zahorik & Keiningham (1995)", "LuCircleCheck"),
      ("Customer Equity", "Firmenwert = Summe der Kundenwerte; Treiber sind Wert, Marke und Bindung.", "Rust, Lemon & Zeithaml (2004); Gupta et al. (2004)", "LuCoins"),
      ("Markt-Assets", "Kundenbeziehungen beschleunigen, erhöhen und stabilisieren Cashflows.", "Srivastava, Shervani & Fahey (1998)", "LuBuilding2"),
      ("Wirkungskette", "Maßnahmen → Kundenwirkung → Marktwirkung → Finanzwirkung → Firmenwert.", "Rust et al. (2004)", "LuTrendingUp"),
      ("Beziehungen", "Vertrauen und Commitment binden Kunden; Beziehungsqualität treibt Erfolg.", "Morgan & Hunt (1994)", "LuHeartHandshake"),
      ("Engagement-Wert", "CLV plus Empfehlungs-, Einfluss- und Wissenswert eines Kunden.", "Kumar et al. (2010)", "LuUsers")]
for i, (h, b, src, ic) in enumerate(fw):
    x = X0 + (i % 3) * (cw3 + GAP)
    y = 1.35 + (i // 3) * 1.85
    band_card(s, x, y, cw3, 1.7, h, [[(b, {})], [(src, {"size": 10.5, "color": GREY_TEXT})]],
              icon_name=ic, band=BLUE if i % 2 == 0 else NAVY, body_size=11.5, name=f"Framework {i + 1}")
notes(s, "Diese Ansätze ergänzen sich. Return on Quality (1995) macht Serviceausgaben rechenschaftspflichtig. Customer "
         "Equity übersetzt Bindung und Akquisition in Firmenwert. Srivastava et al. (1998) erklären, warum: "
         "Kundenbeziehungen sind marktbasierte Vermögenswerte, die Höhe, Timing und Risiko der Cashflows beeinflussen. "
         "Rust et al. (2004) liefern die 'Chain of Marketing Productivity' als Rahmen für den ganzen Kurs. Palmatier et "
         "al. (2006): Beziehungsqualität wirkt am stärksten auf den objektiven Erfolg, Commitment am schwächsten.")

# 13 Bindung und Firmenwert
s = content("Bindung: der stärkste Werthebel")
bar_chart(s, X0, 1.35, 5.0, 3.3, ["Bindungsrate", "Marge", "Akquisitionskosten"], [5.0, 1.0, 0.1],
          "Anstieg des Firmenwerts", '0.0"%"', 6, "Chart value levers",
          horizontal=True, colors=[NAVY, None, None])
band_card(s, 5.7, 1.4, 3.8, 3.2, "Mit Vorsicht lesen",
          [[("Heterogenität: ", {"bold": True}), "eine einzige Bindungsrate unterschätzt den Effekt (Fader & Hardie 2010)"],
           [("Akquisition: ", {"bold": True}), "künftige Neukunden zählen auch; Hebel 1,55 (Schulze et al. 2012)"],
           [("Börsenwert: ", {"bold": True}), "Customer Equity sagt ihn voraus (Kumar & Shah 2009)"]],
          icon_name="LuCoins", body_size=12, name="Value caveats")
caption(s, "Effekt einer Verbesserung um 1 % je Hebel. Gupta, Lehmann & Stuart (2004) Journal of Marketing Research 41(1): "
           "fünf Firmen aus öffentlichen Daten bewertet.", 4.85)
notes(s, "Gupta, Lehmann & Stuart (2004) bewerten Amazon, Ameritrade, eBay u. a. als Summe der Kundenwerte. 1 % mehr "
         "Bindung erhöht den Firmenwert um etwa 5 %, 1 % mehr Marge um etwa 1 %, 1 % geringere Akquisitionskosten um "
         "0,1 %. Schulze, Skiera & Wiesel (2012): 10 % mehr Customer Equity gehen mit etwa 15,5 % höherem "
         "Shareholder Value einher. McCarthy, Fader & Hardie (2017) bewerten Abo-Firmen aus veröffentlichten "
         "Churn-Daten (Customer-Based Corporate Valuation).")

# 14 Kapitalmarkt
s = content("Kundenwerte und der Kapitalmarkt")
bar_chart(s, X0, 1.35, 4.6, 3.3, ["Werbung", "Marken-Assets", "Kunden-Assets"], [0.04, 0.33, 0.72],
          "Elastizität des Firmenwerts", "0.00", 0.8, "Chart elasticities",
          colors=[None, None, NAVY])
band_card(s, 5.3, 1.4, 4.2, 3.3, "Zufriedenheit und Rendite",
          [[("Cashflows: ", {"bold": True}), "mehr Wachstum, weniger Schwankung (Gruca & Rego 2005)"],
           [("Risiko: ", {"bold": True}), "geringeres systematisches Risiko (Tuli & Bharadwaj 2009)"],
           [("Rendite: ", {"bold": True}), "ACSI-Portfolio 518 % vs. S&P 31 %, 2000-2014 (Fornell et al. 2016)"],
           [("Umstritten: ", {"bold": True}), "Fehlbewertung nur bei wenigen Firmen (Jacobson & Mizik 2009)"]],
          icon_name="LuTrendingUp", body_size=12, name="Satisfaction returns")
caption(s, "Edeling & Fischer (2016) Journal of Marketing Research: 488 Elastizitäten aus 83 Studien.", 4.85)
notes(s, "Edeling & Fischer (2016): mittlere Firmenwert-Elastizität 0,04 für Werbung, 0,54 für Marketing-Assets; "
         "kundenbezogene Assets 0,72, markenbezogene 0,33. Debatte: Fornell, Mithas, Morgeson & Krishnan (2006) "
         "'High returns, low risk' und Fornell, Morgeson & Hult (2016) gegen Jacobson & Mizik (2009) und Sorescu & "
         "Sorescu (2016). Malshe, Colicev & Mittal (2020): Unzufriedenheit wiegt etwa 2,4-mal stärker als "
         "Zufriedenheit bei Überrenditen.")

# ------------------------------------------------------------------ Teil 4
section(4, "Abwanderung (Churn)", "vorhersagen, dann steuern",
        "Teil 4, etwa 15 Minuten: Churn-Rechnung, Vorhersage und warum Targeting nach Risiko scheitern kann.")

# 16 Churn-Rechnung
s = content("Kleine Churn-Änderung, große Wirkung")
rows = [["Bindung", "Churn", "CLV", "Änderung"],
        ["70 %", "30 %", "175", "Basis"],
        ["80 %", "20 %", "267", "+52 %"],
        ["90 %", "10 %", "450", "+157 %"]]
table(s, rows, X0, 1.4, 5.4, 2.2, [1.2, 1.0, 1.9, 1.3], "CLV table", size=13, highlight=((3, 2), (3, 3)))
band_card(s, 6.1, 1.4, 3.4, 2.2, "Warum so steil?",
          [[("Jeder Churn-Punkt ", {"bold": True}), "nimmt einen Teil der Marge jedes künftigen Jahres weg"],
           [("Die Kundendauer ", {"bold": True}), "steigt stark, wenn Churn sinkt"]],
          icon_name="LuCalculator", body_size=13, name="Churn why")
callout(s, 3.85, [[("Formel: ", {"bold": True}), "CLV = m · r ÷ (1 + d − r), mit Marge m = 100 und Diskontsatz d = 10 %."]],
        fill=LIGHT, color=BLACK, name="CLV formula")
caption(s, "Gupta & Lehmann (2005) Managing Customers as Investments; Hardie Note 024 zu CLV-Formeln.", 4.55)
notes(s, "Rechenbeispiel mit Marge 100 pro Jahr und 10 % Diskontsatz: r = 0,7 ergibt 100 × 0,7 / 0,4 = 175; r = 0,8 "
         "ergibt 80 / 0,3 = 267; r = 0,9 ergibt 90 / 0,2 = 450. Studierende rechnen r = 0,95 (950). Dann die Annahmen "
         "diskutieren: konstante Bindung ignoriert Heterogenität (Fader & Hardie 2007, sBG-Modell), daher steigen "
         "Kohorten-Bindungsraten über die Zeit.")

# 17 Vorhersagen vs. steuern
s = content("Vorhersagen ist nicht Steuern")
band_card(s, X0, 1.4, cw, 2.75, "Vorhersagen: Wer geht?",
          [[("Methoden zählen: ", {"bold": True}), "im Churn-Turnier lagen Hunderttausende Dollar pro Kampagne zwischen den Modellen"],
           [("Bäume und Boosting ", {"bold": True}), "schlagen einfache Logit-Modelle"],
           [("Nach Gewinn beurteilen, ", {"bold": True}), "nicht nur nach AUC"]],
          icon_name="LuSearch", band=NAVY, body_size=13, name="Predict churn")
band_card(s, X0 + cw + GAP, 1.4, cw, 2.75, "Steuern: Wen ansprechen?",
          [[("Retention Futility: ", {"bold": True}), "die riskantesten Kunden reagieren nicht am stärksten"],
           [("Nach Uplift zielen, ", {"bold": True}), "also nach der Wirkung des Angebots je Kunde"],
           [("Angebote können schaden: ", {"bold": True}), "Churn stieg von 6 % auf 10 % nach Tarifempfehlungen"]],
          icon_name="LuTarget", body_size=13, name="Manage churn")
callout(s, 4.35, [[("Regel: ", {"bold": True}), "Kunden ansprechen, deren Verhalten das Angebot ändert, gewichtet mit ihrem CLV."]],
        name="Churn rule")
caption(s, "Neslin et al. (2006) JMR; Lemmens & Croux (2006) JMR; Verbeke et al. (2012) EJOR; Ascarza (2018) JMR; "
           "Ascarza, Iyengar & Schleicher (2016) JMR; Lemmens & Gupta (2020) Marketing Science.", 5.0)
notes(s, "Ascarza (2018, 'Retention futility', Feldexperimente bei einem Mobilfunkanbieter und einer "
         "Mitgliederorganisation): Targeting nach geschätztem Treatment-Effekt schlägt Targeting nach Churn-Risiko. "
         "Ascarza, Iyengar & Schleicher (2016): Empfehlungen günstigerer Tarife erhöhten den Churn von 6 % auf 10 %, "
         "weil träge Kunden aufgeweckt wurden. Gegenbeispiel: Gattermann-Itschert & Thonemann (2022) finden, dass "
         "Risiko-Targeting in einer B2B-Feldstudie wirkt. Übung: HBS 'Managing Customer Retention at Teleko' (Ascarza, "
         "kostenloses Online-Tool).")

# ------------------------------------------------------------------ Teil 5
section(5, "Share of Wallet", "Rang schlägt Bewertung",
        "Teil 5, etwa 15 Minuten: Zufriedenheit und Share of Wallet, die Wallet Allocation Rule, Bonusprogramme.")

# 19 SOW-Evidenz
s = content("Der Share of Wallet folgt dem Rang")
bar_chart(s, X0, 1.35, 4.4, 3.3, ["Absolute Zufriedenheit", "Rang (WAR)"], [9, 55],
          "Erklärte Varianz", '0"%"', 60, "Chart SOW variance", colors=[None, NAVY])
stats = [("≈" + NB + "0,1", "Korrelation der Änderungen von Zufriedenheit oder NPS mit Änderungen im Share of Wallet", "Keiningham et al. (2011) HBR"),
         ("10×", "Verschiebungen der Ausgaben können bis zu zehnmal mehr wert sein als Komplettabwanderung", "Coyles & Gokey (2005)")]
for i, (fig, lab, src) in enumerate(stats):
    y = 1.45 + i * 1.6
    rect(s, 5.1, y, 4.4, 1.4, name=f"SOW stat box {i + 1}")
    text(s, 5.25, y + 0.08, 1.4, 1.2, fig, size=26, bold=True, head=True, color=NAVY,
         anchor=MSO_ANCHOR.MIDDLE, name=f"SOW figure {i + 1}", space=0)
    text(s, 6.65, y + 0.1, 2.75, 1.2, [[(lab, {})], [(src, {"size": 10.5, "color": GREY_TEXT})]],
         size=12, name=f"SOW text {i + 1}", space=2)
caption(s, "Anteil an den Einlagen. Aksoy (2014) International Journal of Bank Marketing, 4.712 Bankkunden; Cooil et al. (2007) Journal of "
           "Marketing; Keiningham et al. (2015) Journal of Service Management.", 4.85)
notes(s, "Cooil et al. (2007): 4.319 kanadische Bankhaushalte über fünf Jahre; Änderungen der Zufriedenheit hängen "
         "positiv, aber schwach mit Änderungen des Share of Wallet zusammen. Keiningham et al. (2015): 79.543 "
         "Konsumenten, über 650 Marken, 20 Branchen; die Rangposition hängt viel stärker mit dem Share of Wallet "
         "zusammen. Coyles & Gokey (2005, McKinsey): 1.200 Haushalte, 16 Branchen.")

# 20 WAR-Übung
s = content("Die Wallet Allocation Rule im Hörsaal")
rect(s, X0, 1.4, 4.3, 1.3, fill=NAVY, name="WAR formula box")
text(s, X0 + 0.2, 1.48, 3.9, 0.4, "Wallet Allocation Rule", size=13, bold=True, color=T.ACCENT_6, name="WAR label")
text(s, X0 + 0.2, 1.88, 3.9, 0.7, "SOW = (1 − Rang ÷ (n + 1)) × 2 ÷ n", size=19, bold=True, head=True,
     color=WHITE, name="WAR formula")
rows = [["Rang unter 3 Marken", "Erwarteter Anteil"], ["1.", "50 %"], ["2.", "33 %"], ["3.", "17 %"]]
table(s, rows, X0, 2.9, 4.3, 1.6, [2.4, 1.9], "WAR table", size=13, highlight=((1, 1),))
steps = ["Alle notieren die Supermärkte, in denen sie letzten Monat eingekauft haben",
         "Diese nach Präferenz reihen",
         "Die tatsächliche Aufteilung der Ausgaben schätzen",
         "Erwartete und tatsächliche Anteile im Streudiagramm vergleichen"]
for i, t in enumerate(steps):
    y = 1.4 + i * 0.78
    number(s, 5.1, y + 0.12, i + 1, d=0.4, size=12, name=f"WAR step number {i + 1}")
    text(s, 5.65, y, 3.85, 0.65, t, size=12.5, anchor=MSO_ANCHOR.MIDDLE, name=f"WAR step {i + 1}", space=0)
callout(s, 4.7, "Mehr Anteil gewinnt, wer seinen Rang gegenüber den anderen genutzten Marken verbessert.", h=0.5, name="WAR callout")
notes(s, "Keiningham, Aksoy, Buoye & Cooil (2011, HBR) und das Buch The Wallet Allocation Rule (Wiley 2015). n = Zahl "
         "der Marken, die ein Kunde nutzt. Bei drei Marken: Rang 1 = (1 − 1/4) × 2/3 = 50 %, Rang 2 = 33 %, Rang 3 = "
         "17 %. Dauert mit einer Online-Umfrage etwa 10 Minuten. Bezug zur Debatte: Buoye et al. (2016) verbinden WAR "
         "mit Double Jeopardy.")

# 21 Bonusprogramme
s = content("Bonusprogramme: kleinere Effekte")
stat_rows(s, [
    ("7×", "kleinerer Programmeffekt auf den Share of Wallet, wenn die Selbstselektion von Vielkäufern kontrolliert wird.",
     "Leenheer, van Heerde, Bijmolt & Smidts (2007) IJRM"),
    ("6-9", "Monate, bis die Verhaltensänderung nach dem Beitritt wieder verblasst.",
     "Meyer-Waarden & Benavent (2009) JAMS"),
    ("4,4 %", "Jahreswachstum bei hohen Bonusausgaben vs. 5,5 % bei niedrigen, 55 börsennotierte Firmen.",
     "McKinsey (2013) Making loyalty pay")], prefix="LP")
callout(s, 4.45, [[("Lokale Fälle: ", {"bold": True}),
                   "jö Bonus Club (4,5 bis 4,7 Mio. Mitglieder) und Payback; Starbucks-Mitglieder bringen 57 bis 60 % des US-Umsatzes."]],
        h=0.65, fill=LIGHT, color=BLACK, name="LP cases")
notes(s, "Belli et al. (2022, JAMS), Metaanalyse mit 429 Effekten: Programme erhöhen die Verhaltensloyalität, die "
         "Einstellungsloyalität kaum. Liu (2007, JM): Wenig- und Mittelkäufer ändern ihr Verhalten, Vielkäufer lösen "
         "nur ein. Frage: Geben Starbucks-Mitglieder wegen des Programms mehr aus, oder sind Vielkäufer beigetreten? "
         "jö-Zahlen sind Eigenangaben (Presse, 2025); die Billa-'-25 %'-Pickerl gibt es seit Juli 2025 nur für "
         "Mitglieder.")

# ------------------------------------------------------------------ Teil 6
section(6, "Kritik und Anwendung", "wo die Kette bricht",
        "Teil 6, etwa 15 Minuten: Loyalität versus Profitabilität, Grenzen, Lab und Fallstudien.")

# 23 Raster
s = content("Loyalität ist nicht gleich Profitabilität")
gx, gy, gw2, gh = 2.1, 1.35, 6.4, 3.6
quads = [("Barnacles", "Treu, aber unprofitabel: Share of Wallet erhöhen oder Servicekosten senken", 0, 0, LIGHT, BLACK, NAVY),
         ("True Friends", "Treu und profitabel: halten, belohnen, pflegen", 1, 0, NAVY, WHITE, WHITE),
         ("Strangers", "Weder noch: nicht investieren", 0, 1, LIGHT, BLACK, NAVY),
         ("Butterflies", "Profitabel, aber kurzlebig: abschöpfen, nicht um Treue werben", 1, 1, BLUE, WHITE, WHITE)]
qw, qh = (gw2 - 0.1) / 2, (gh - 0.1) / 2
for h, b, cx, cy, fill, col, hcol in quads:
    x, y = gx + cx * (qw + 0.1), gy + cy * (qh + 0.1)
    rect(s, x, y, qw, qh, fill=fill, name=f"Quadrant {h}")
    text(s, x + 0.15, y + 0.1, qw - 0.3, 0.45, h, size=15, bold=True, head=True, color=hcol, name=f"Quadrant heading {h}")
    text(s, x + 0.15, y + 0.6, qw - 0.3, qh - 0.7, b, size=13, color=col, name=f"Quadrant text {h}")
text(s, X0, gy + gh / 2 - 0.5, 1.5, 1.0, "Loyalität: erwartete Beziehungsdauer", size=11,
     color=GREY_TEXT, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE, name="Axis loyalty")
text(s, gx, gy + gh + 0.05, gw2, 0.3, "Profitabilität →", size=11, color=GREY_TEXT, align=PP_ALIGN.CENTER,
     name="Axis profit")
text(s, X0, gy, 1.5, 0.3, "lang", size=11, color=GREY_TEXT, align=PP_ALIGN.RIGHT, name="Axis long")
text(s, X0, gy + gh - 0.3, 1.5, 0.3, "kurz", size=11, color=GREY_TEXT, align=PP_ALIGN.RIGHT, name="Axis short")
caption(s, "Reinartz & Kumar (2002) Harvard Business Review; Reinartz & Kumar (2000) Journal of Marketing.", gy + gh + 0.4)
notes(s, "Reinartz & Kumar (2002), 16.000 Kunden in vier Firmen: keine Bestätigung, dass treue Kunden weniger kosten, "
         "mehr zahlen oder mehr empfehlen. Die englischen Segmentnamen sind die Originalbegriffe. Shah et al. (2012, "
         "JM): 10 bis 35 % der Cross-Buyer sind unprofitabel und verursachen 39 bis 88 % der Verluste aus Kunden. "
         "Studierende ordnen ihre eigenen Handy-, Bank- und Supermarktbeziehungen aus Firmensicht ein.")

# 24 Wo die Kette bricht
s = content("Wo die Kette bricht")
devs = [("NPS", "Sagt Wachstum nicht besser voraus als Zufriedenheit", "Keiningham et al. (2007); van Doorn et al. (2013)"),
        ("Penetration", "Marken wachsen vor allem durch Neukunden; Loyalität folgt der Größe", "Ehrenberg et al. (1990); Riebe et al. (2014)"),
        ("Cross-Buying", "Mehr Share of Wallet kann unprofitable Käufer anziehen", "Shah et al. (2012)"),
        ("Zufriedenheitskosten", "Sehr hohe Zufriedenheit kann die Aktienrendite senken", "Guenther & Guenther (2021)"),
        ("Mitarbeitende", "Mitarbeiterzufriedenheit hebt den Gewinn nicht immer", "Silvestro (2002)"),
        ("Lock-in", "Wechselbarrieren halten nur, solange das Erlebnis schlecht ist", "Gao, Melero-Polo & Sese (2022)")]
for i, (h, b, src) in enumerate(devs):
    x = X0 + (i % 2) * (cw + GAP)
    y = 1.35 + (i // 2) * 1.32
    rect(s, x, y, cw, 1.18, name=f"Break {i + 1}")
    rect(s, x, y + 0.12, 0.07, 0.94, fill=BLUE, name=f"Break bar {i + 1}")
    text(s, x + 0.2, y + 0.05, cw - 0.3, 1.1,
         [[(h, {"bold": True, "color": NAVY, "head": True, "size": 14})], [(b, {})],
          [(src, {"size": 10.5, "color": GREY_TEXT})]], size=12, name=f"Break text {i + 1}", space=2)
notes(s, "Debatte (10 Minuten): 'Firmen sollten ihr Bonusbudget stattdessen in Neukundengewinnung stecken.' Eine "
         "Hälfte argumentiert mit Heskett/Reichheld, die andere mit Sharp/Reinartz. Gao et al. (2022): Lock-in senkt "
         "den Churn vor allem bei Erlebniswerten unter 5 von 10 und spielt über 7 keine Rolle mehr. ACSI (Q1 2026) "
         "warnt vor 'aufgestauter Abwanderung': unzufriedene Kunden, die mangels Alternativen bleiben.")

# 25 Lab
s = content("Lab: Churn und CLV mit echten Daten")
stepper(s, ["Daten", "Beschreiben", "Modellieren", "Bewerten", "Entscheiden"], size=10.5)
band_card(s, X0, 2.15, 3.6, 2.45, "Daten und Tools",
          [[("IBM Telco: ", {"bold": True}), f"7.043{NB}Kunden, Churn-Flag"],
           [("CDNOW: ", {"bold": True}), f"Stichprobe mit 2.357{NB}Kunden, Käufe"],
           [("R: ", {"bold": True}), "CLVTools, BTYDplus (WU), survival"],
           [("Python: ", {"bold": True}), "PyMC-Marketing, lifelines"]],
          icon_name="LuDatabase", body_size=12, name="Lab data")
tasks = ["Bindungskurven nach Vertragsart (Kaplan-Meier)",
         "Logit-Churn-Modell schätzen; Lift-Tabelle nach Dezilen",
         "BG/NBD auf CDNOW; P(alive) und 12-Monats-CLV",
         "Kundenstamm bewerten: Wem lohnt ein Halteangebot?"]
for i, t in enumerate(tasks):
    y = 2.15 + i * 0.62
    number(s, 4.35, y + 0.05, i + 1, d=0.38, size=12, name=f"Task number {i + 1}")
    text(s, 4.85, y, 4.65, 0.55, t, size=12, anchor=MSO_ANCHOR.MIDDLE, name=f"Task {i + 1}", space=0)
callout(s, 4.75, "Abgabe: Bindungsgrafik, CLV-Tabelle und eine halbe Seite zur Zielgruppe.",
        h=0.5, name="Deliverable")
caption(s, "Daten: Kaggle (IBM Telco Customer Churn); brucehardie.com/datasets (CDNOW). Methode: Fader, Hardie & Lee (2005) Marketing Science.", 5.3)
notes(s, "IBM Telco ist der Standarddatensatz für Churn in der Lehre (Vertragsdauer und Churn-Flag erlauben "
         "Überlebenszeitanalyse). CDNOW ist in CLVTools, BTYD und PyMC-Marketing enthalten. Das Python-Paket lifetimes "
         "wird nicht mehr gepflegt; PyMC-Marketing verwenden. BTYDplus stammt von Michael Platzer und Thomas Reutterer "
         "(WU): Pareto/GGG- und MBG/CNBD-k-Modelle, die die Regelmäßigkeit von Käufen nutzen.")

# 26 Fallstudien
s = content("Fallstudien für die Lehre")
items = [("Pilgrim Bank", "Fälle (A) und (B), Kundendaten: Sind Online-Kunden profitabler und treuer?",
          "Gewinn, Bindung, Selektionseffekt", "HBS 602104 / 602095"),
         ("Teleko", "Wen mit einem Halteangebot ansprechen: nach Churn-Risiko oder Uplift?",
          "Churn-Management", "HBS 523005, kostenloses Online-Tool"),
         ("Harrah's", "Total Rewards erhöhte den Anteil an einem Spielbudget, der bei 36 % lag.",
          "Share of Wallet, Bonusdaten", "HBS 502011; Loveman (2003) HBR")]
for i, (h, facts, lesson, src) in enumerate(items):
    x = X0 + i * (cw3 + GAP)
    band_card(s, x, 1.35, cw3, 2.85, h,
              [[(facts, {})], [(lesson, {"bold": True, "color": NAVY})], [(src, {"size": 10.5, "color": GREY_TEXT})]],
              body_size=13, name=f"Case {h}")
callout(s, 4.4, [[("Außerdem: ", {"bold": True}), "Sears (Service-Profit-Chain), Starbucks: Delivering Customer Service, Netflix (Darden, CLV und Bewertung)."]],
        h=0.6, name="More cases")
notes(s, "Pilgrim Bank (Frei & Campbell, HBS 2001) enthält Daten zu etwa 30.000 Kunden; (B) ergänzt ein zweites Jahr "
         "für ein Bindungsmodell. Teleko (Ascarza, HBS 2022) ist eine zweiseitige Übung mit kostenlosem Online-Tool. "
         "Harrah's (Lal, HBS 2001) und Lovemans 'Diamonds in the Data Mine' (HBR 2003). Starbucks (Moon & Quelch, HBS) "
         "fragt, ob sich eine Serviceinvestition von 40 Mio. USD lohnt. Alle Fälle sind englischsprachig.")

# 27 Literatur
s = content("Literatur")
rw = cw3
band_card(s, X0, 1.35, rw, 3.35, "Kernliteratur",
          [[("Heskett et al. (1994) ", {"bold": True}), "Putting the service-profit chain to work, HBR"],
           [("Gupta & Zeithaml (2006) ", {"bold": True}), "Customer metrics, Marketing Science"],
           [("Hogreve et al. (2017) ", {"bold": True}), "SPC-Metaanalyse, JM"],
           [("Gupta et al. (2004) ", {"bold": True}), "Valuing customers, JMR"],
           [("Keiningham et al. (2015) ", {"bold": True}), "Perceptions are relative, JOSM"]],
          icon_name="LuGraduationCap", body_size=11, name="References core")
band_card(s, X0 + rw + GAP, 1.35, rw, 3.35, "Ansätze",
          [[("Srivastava et al. (1998) ", {"bold": True}), "Market-based assets, JM"],
           [("Rust et al. (2004) ", {"bold": True}), "Return on marketing, JM"],
           [("Reinartz & Kumar (2002) ", {"bold": True}), "Mismanagement of loyalty, HBR"],
           [("Otto et al. (2020) ", {"bold": True}), "Zufriedenheits-Metaanalyse, JAMS"],
           [("Bruhn & Homburg (2017) ", {"bold": True}), "Handbuch Kundenbindungsmanagement"]],
          icon_name="LuLibrary", body_size=11, name="References frameworks")
band_card(s, X0 + 2 * (rw + GAP), 1.35, rw, 3.35, "Churn, Methoden",
          [[("Ascarza (2018) ", {"bold": True}), "Retention futility, JMR"],
           [("Neslin et al. (2006) ", {"bold": True}), "Defection detection, JMR"],
           [("Fader et al. (2005) ", {"bold": True}), "BG/NBD, Marketing Science"],
           [("McCarthy et al. (2017) ", {"bold": True}), "Valuing subscription firms, JM"],
           [("Platzer & Reutterer (2016) ", {"bold": True}), "Pareto/GGG, Marketing Science"]],
          icon_name="LuChartColumn", body_size=11, name="References methods")
notes(s, "Über 380 weitere Quellen mit Zugangshinweisen: Notion-Seite und GitHub-Ordner 'Customer Loyalty, Churn and "
         "Share of Wallet (Service-Profit Chain)' (github.com/arnefloh-wu/search-teaching-materials). Deutschsprachig: "
         "Bruhn & Homburg (2017) Handbuch Kundenbindungsmanagement, 9. Aufl.; Homburg (2016) Kundenzufriedenheit; "
         "Meffert, Bruhn & Hadwich (2018) Dienstleistungsmarketing; Bruhn (2022) Relationship Marketing. Die meisten "
         "Zeitschriftenartikel sind kostenpflichtig; WU-Zugang prüfen.")

# 28 Fazit
s = content("Kernaussagen")
tk = [("Kennzahlen: ", "Kundenbindung, Abwanderung und Share of Wallet getrennt messen."),
      ("Service-Profit-Chain: ", "jedes Glied hält im Schnitt, die Stärke hängt vom Setting ab."),
      ("Zufriedenheit: ", "hängt mit dem Erfolg zusammen, mäßig und nicht linear."),
      ("Bindung: ", "ist der stärkste Hebel der Customer Equity und zeigt sich im Firmenwert."),
      ("Share of Wallet: ", "folgt dem Rang, nicht dem Zufriedenheitswert."),
      ("Grenzen: ", "Loyalität ist nicht Gewinn; Halteangebote nach Uplift und CLV steuern.")]
for i, (lead, rest) in enumerate(tk):
    y = 1.35 + i * 0.58
    rect(s, X0, y, W0, 0.5, name=f"Takeaway row {i + 1}")
    number(s, X0 + 0.12, y + 0.06, i + 1, d=0.38, size=13, name=f"Takeaway number {i + 1}")
    text(s, X0 + 0.7, y, W0 - 0.85, 0.5, [[(lead, {"bold": True, "color": NAVY}), rest]], size=13,
         anchor=MSO_ANCHOR.MIDDLE, name=f"Takeaway text {i + 1}", space=0)
callout(s, 4.95, [[("Nächstes Mal: ", {"bold": True}), "das Churn- und CLV-Lab. Bitte Laptop mit R oder Python mitbringen."]],
        h=0.5, name="Next")
notes(s, "Zurück zu Folie 2: Welche Aussagen der linken Spalte haben die Evidenz überstanden, welche brauchen Bedingungen?")

# 29 Abschluss
s = prs.slides.add_slide(LAY["Abschlussfolie Kontakt"])
drop_empty(s, keep=())
footer(s)
notes(s, "Fragen und Diskussion.")

prs.save(OUT)
print("saved", OUT, len(prs.slides), "slides")
