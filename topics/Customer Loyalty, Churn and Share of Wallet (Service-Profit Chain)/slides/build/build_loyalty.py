"""Build the lecture Customer Loyalty, Churn and Share of Wallet on the WU 16:10 template (polish-slides patterns)."""
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
            r = p.add_run(); r.text = "PAGE "; lang(r)
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

# Slides for the lecture 'Customer Loyalty, Churn and Share of Wallet'.
# Appended to the helper block of build_hbg.py by make_loyalty.sh (same template, same patterns).
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


# ================================================================== slides
# 1  Title
s = prs.slides.add_slide(LAY["Titelfolie Kontakt"])
s.shapes.title.text = "Loyalty, Churn and Share of Wallet"
for ph in s.placeholders:
    if ph.placeholder_format.idx == 1:
        ph.text_frame.text = "Customer metrics and firm performance"
    elif ph.placeholder_format.idx == 12:
        ph.text_frame.text = "October 2026"
notes(s, "About 100 minutes in six parts: concepts and metrics, the service-profit chain, frameworks that link "
         "customers to firm value, churn, share of wallet, and critiques with a hands-on part. Core reading: "
         "Heskett et al. (1994) HBR; Gupta & Zeithaml (2006) Marketing Science; Hogreve et al. (2017) Journal of "
         "Marketing; Keiningham et al. (2015) Journal of Service Management. All sources with access notes are on "
         "the Notion page and in the GitHub folder for this topic.")

# 2  Two views
s = content("Does customer loyalty pay? Two answers")
band_card(s, X0, 1.4, cw, 2.9, "Loyalty pays",
          [[("Service-profit chain: ", {"bold": True}), "satisfied employees and customers drive profit"],
           [("Retention economics: ", {"bold": True}), "5% fewer defections, 25% or more profit"],
           [("Customer equity: ", {"bold": True}), "retention is the strongest lever on firm value"]],
          icon_name="LuHeartHandshake", body_size=14, name="Loyalty pays")
band_card(s, X0 + cw + GAP, 1.4, cw, 2.9, "Loyalty is not enough",
          [[("Reinartz & Kumar: ", {"bold": True}), "loyal customers are not always profitable"],
           [("Keiningham: ", {"bold": True}), "satisfaction barely moves share of wallet"],
           [("Ehrenberg-Bass: ", {"bold": True}), "growth comes from more buyers, not more loyalty"]],
          icon_name="LuScale", band=T.ACCENT_4, body_size=14, name="Loyalty is not enough")
callout(s, 4.5, "Today: follow the chain from customers to firm value, and test each link against the evidence.",
        name="Central question")
notes(s, "Quick poll: which column do you believe? Practice largely follows the left column (loyalty programmes, "
         "NPS targets, retention teams). The right column collects the main empirical challenges. Part 6 returns "
         "to the tension. The 5%/25% figure is Reichheld's for financial services (Bain brief 2001); the often "
         "quoted '25 to 95%' is not in that source.")

# 3  Objectives
s = content("Learning objectives")
objs = [("LuGauge", "Define", "loyalty, churn and share of wallet, and measure each correctly"),
        ("LuLink", "Explain", "the service-profit chain and the satisfaction-profit chain"),
        ("LuCoins", "Connect", "retention and customer equity to firm value and stock returns"),
        ("LuWallet", "Apply", "CLV, churn targeting and the Wallet Allocation Rule to data"),
        ("LuScale", "Evaluate", "where the chain breaks: NPS, loyalty programmes, Double Jeopardy")]
for i, (ic, verb, rest) in enumerate(objs):
    y = 1.35 + i * 0.8
    rect(s, X0, y, W0, 0.68, name=f"Objective row {i + 1}")
    icon(s, ic, X0 + 0.22, y + 0.14, 0.4)
    text(s, X0 + 0.85, y, W0 - 1.0, 0.68, [[(verb + " ", {"bold": True, "color": NAVY}), rest]],
         size=14, anchor=MSO_ANCHOR.MIDDLE, name=f"Objective text {i + 1}", space=0)
notes(s, "The objectives map onto the six parts. The lab in Part 6 tests objectives 1 and 4 with data; the "
         "debate tests objective 5.")

# ------------------------------------------------------------------ Part 1
section(1, "Concepts and metrics", "what we measure",
        "Part 1, about 15 minutes: definitions and measurement of loyalty, churn and share of wallet.")

# 5  Three outcomes
s = content("Three customer outcomes, three questions")
cards = [("Loyalty", "Do customers stay and prefer us?",
          [[("Behavioural: ", {"bold": True}), "repeat buying"], [("Attitudinal: ", {"bold": True}), "relative preference"],
           [("True loyalty needs both ", {"bold": True}), "(Dick & Basu 1994)"]], "LuHeartHandshake"),
         ("Churn", "Do customers leave?",
          [[("Contractual: ", {"bold": True}), "cancellation is observed"], [("Non-contractual: ", {"bold": True}), "silence, so churn must be inferred"],
           [("Retention rate ", {"bold": True}), "r = 1 − churn"]], "LuUserMinus"),
         ("Share of wallet", "How much of their spending do we get?",
          [[("SOW ", {"bold": True}), "= our sales ÷ customer's category spend"], [("Needs ", {"bold": True}), "competitor spend, usually from surveys"],
           [("Partial defection ", {"bold": True}), "shows here first"]], "LuWallet")]
for i, (h, q, body, ic) in enumerate(cards):
    x = X0 + i * (cw3 + GAP)
    band_card(s, x, 1.4, cw3, 2.9, h, [[(q, {"bold": True, "color": NAVY})]] + body,
              icon_name=ic, band=BLUE if i != 1 else NAVY, body_size=12, name=f"Outcome {h}")
callout(s, 4.5, [[("Link to firm value: ", {"bold": True}),
                  "retention sets how long customers pay, SOW sets how much; together they drive CLV."]],
        h=0.6, name="Outcome callout")
notes(s, "Loyalty typology: Dick & Basu (1994, JAMS): true, latent, spurious, no loyalty. Oliver (1999): "
         "cognitive, affective, conative, action loyalty. Churn: Fader & Hardie distinguish contractual vs "
         "non-contractual settings, which decides the model (sBG vs BG/NBD or Pareto/NBD). Share of wallet: Du, "
         "Kamakura & Mela (2007) show internal spend says little about the size of a customer's total wallet.")

# 6  Metrics table
s = content("Measuring the outcomes")
rows = [["Metric", "Formula", "Watch out for"],
        ["Retention rate", "customers kept ÷ customers at start", "Rises over time as weak customers leave"],
        ["Expected lifetime", "1 ÷ churn (only if all equal)", "Underestimates lifetime with heterogeneity"],
        ["CLV", "m · r ÷ (1 + d − r)", "Assumes constant margin and retention"],
        ["Share of wallet", "our spend ÷ category spend", "Category spend needs survey or panel data"],
        ["Net Promoter Score", "% promoters − % detractors", "Not a better growth predictor"]]
table(s, rows, X0, 1.4, W0, 3.0, [2.1, 3.3, 3.6], "Metrics table", size=12, first_col_dark=True)
caption(s, "Fader & Hardie (2007, 2010); Hardie notes 024, 033, 049 (brucehardie.com); Farris et al. (2021) Marketing "
           "Metrics, ch. 2 and 5; Keiningham et al. (2007) Journal of Marketing.", 4.6)
notes(s, "Hardie note 049: 'average lifetime is not 1/churn' once customers differ. Fader & Hardie (2010, "
         "Marketing Science) show that ignoring heterogeneity understates the value of a customer base. The "
         "simple CLV formula m·r/(1+d−r) assumes an infinite horizon, constant margin and constant retention "
         "(Gupta & Lehmann 2005). NPS critique: Keiningham et al. (2007); van Doorn et al. (2013).")

# ------------------------------------------------------------------ Part 2
section(2, "The service-profit chain", "from employees to profit",
        "Part 2, about 20 minutes: the chain, its evidence and the satisfaction-profit chain.")

# 8  SPC stepper
s = content("The service-profit chain")
w = stepper(s, ["1", "2", "3", "4", "5", "6"], h=0.5, size=14)
heads = ["Internal quality", "Employees", "Service value", "Satisfaction", "Loyalty", "Profit"]
expl = ["Tools, training, workplace design", "Satisfaction, retention, productivity",
        "Results for customers relative to cost", "Customers' overall judgement",
        "Retention, repeat buying, referrals", "Revenue growth and profitability"]
for i, t in enumerate(expl):
    x = X0 + i * (w - 0.12)
    rect(s, x + 0.05, 2.05, w - 0.22, 1.75, name=f"Chain box {i + 1}")
    text(s, x + 0.1, 2.2, w - 0.32, 1.2, [[(heads[i], {"bold": True, "color": NAVY, "size": 11})], [(t, {})]], size=12, name=f"Chain text {i + 1}", space=3)
callout(s, 4.05, [[("The claim: ", {"bold": True}),
                   "each link drives the next, so investing in employees and service pays off in profit."]],
        name="Chain claim")
caption(s, "Heskett, Jones, Loveman, Sasser & Schlesinger (1994) Harvard Business Review 72(2); "
           "Heskett, Sasser & Schlesinger (1997) The Service Profit Chain.", 4.75)
notes(s, "Heskett et al. (1994) build the chain from cases (Southwest, Taco Bell, Banc One). The 1997 book adds "
         "the 'satisfaction mirror': employee and customer satisfaction reinforce each other. German "
         "counterpart: the Erfolgskette in Meffert, Bruhn & Hadwich (2018) Dienstleistungsmarketing.")

# 9  SPC evidence
s = content("Evidence: the chain holds, with conditions")
stat_rows(s, [
    ("All links", "significant in a meta-analysis of the full chain, but effect sizes vary strongly by type of service.",
     "Hogreve, Iseke, Derfuss & Eller (2017) Journal of Marketing 81(3)"),
    ("+0.5 pts", "revenue growth at Sears from +5 units employee attitude, via +1.3 units customer impression.",
     "Rucci, Kirn & Quinn (1998) Harvard Business Review"),
    ("Time lags", "between investment, satisfaction and performance can push managers into myopic cuts.",
     "Evanschitzky, von Wangenheim & Wünderlich (2012) Journal of Retailing")], prefix="SPC")
callout(s, 4.45, [[("But: ", {"bold": True}),
                   "in UK grocery stores employee satisfaction did not drive profit (Silvestro 2002), so the employee link is contingent."]],
        h=0.65, fill=LIGHT, color=BLACK, name="SPC caveat")
notes(s, "Hogreve et al. (2017) also find that internal service quality works through more than employee "
         "satisfaction, so 'maximise employee satisfaction' is not a universal rule. Brown & Lam (2008, Journal of "
         "Retailing) meta-analysis: employee satisfaction relates to customer satisfaction, fully mediated by "
         "perceived service quality. Hogreve, Iseke & Derfuss (2022, JSR) revise the chain for digital and AI-based "
         "service. Check the Sears numbers against the original HBR article before quoting them.")

# 10 Satisfaction-profit chain
s = content("Satisfaction pays, but modestly")
bar_chart(s, X0, 1.35, 4.4, 3.4, ["Average", "Best conditions"], [0.101, 0.349],
          "Correlation: satisfaction and firm performance", "0.00", 0.4, "Chart satisfaction correlation",
          colors=[None, NAVY])
band_card(s, 5.1, 1.4, 4.4, 3.3, "The satisfaction-profit chain",
          [[("Asymmetric: ", {"bold": True}), "a bad experience hurts more than a good one helps"],
           [("Nonlinear: ", {"bold": True}), "thresholds and diminishing returns"],
           [("Intentions ≠ behaviour: ", {"bold": True}), "same rating, different repurchase rates"],
           [("Cost side: ", {"bold": True}), "very high satisfaction can cost more than it earns"]],
          icon_name="LuGauge", body_size=12, name="Satisfaction chain")
caption(s, "Otto, Szymanski & Varadarajan (2020) JAMS, 251 correlations; Anderson & Mittal (2000) JSR; Mittal & "
           "Kamakura (2001) JMR; Guenther & Guenther (2021) IJRM; Mittal et al. (2023) Marketing Letters.", 4.95)
notes(s, "Otto et al. (2020): average r = .101; r = .349 under the most favourable contingencies (right setting "
         "and measures). Mittal et al. (2023): 535 correlations, N about 1.16 million, positive links at customer "
         "and firm level. Mittal & Kamakura (2001): in one segment satisfaction and repurchase are uncorrelated. "
         "Guenther & Guenther (2021): at high levels, costs of further satisfaction gains can exceed the benefits.")

# ------------------------------------------------------------------ Part 3
section(3, "From customers to firm value", "alternative frameworks",
        "Part 3, about 20 minutes: frameworks beyond the service-profit chain, and the capital-market evidence.")

# 12 Framework grid
s = content("Six frameworks beyond the chain")
fw = [("Return on quality", "Quality is an investment that must pay back; it is possible to overspend.", "Rust, Zahorik & Keiningham (1995)", "LuCircleCheck"),
      ("Customer equity", "Firm value = sum of customer lifetime values; drivers are value, brand and retention.", "Rust, Lemon & Zeithaml (2004); Gupta et al. (2004)", "LuCoins"),
      ("Market assets", "Customer relationships speed up, raise and stabilise cash flows.", "Srivastava, Shervani & Fahey (1998)", "LuBuilding2"),
      ("Productivity chain", "Actions → customer impact → market impact → financial impact → firm value.", "Rust et al. (2004)", "LuTrendingUp"),
      ("Relationships", "Trust and commitment keep relationships; relationship quality drives performance.", "Morgan & Hunt (1994); Palmatier et al. (2006)", "LuHeartHandshake"),
      ("Engagement value", "CLV plus referral, influence and knowledge value of a customer.", "Kumar et al. (2010)", "LuUsers")]
for i, (h, b, src, ic) in enumerate(fw):
    x = X0 + (i % 3) * (cw3 + GAP)
    y = 1.35 + (i // 3) * 1.85
    band_card(s, x, y, cw3, 1.7, h, [[(b, {})], [(src, {"size": 10.5, "color": GREY_TEXT})]],
              icon_name=ic, band=BLUE if i % 2 == 0 else NAVY, body_size=11.5, name=f"Framework {i + 1}")
notes(s, "These frameworks are complements, not rivals. Return on quality (1995) makes service spending "
         "accountable. Customer equity turns retention and acquisition into firm value. Srivastava et al. (1998) "
         "explain why: customer relationships are market-based assets that affect the level, timing and risk of "
         "cash flows. Rust et al. (2004) give the 'chain of marketing productivity' that frames the whole course. "
         "Palmatier et al. (2006): relationship quality affects objective performance most, commitment least.")

# 13 Retention and firm value
s = content("Retention: the strongest value lever")
bar_chart(s, X0, 1.35, 5.0, 3.3, ["Retention rate", "Margin", "Acquisition cost"], [5.0, 1.0, 0.1],
          "Gain in firm value", '0.0"%"', 6, "Chart value levers",
          horizontal=True, colors=[NAVY, None, None])
band_card(s, 5.7, 1.4, 3.8, 3.2, "Read with care",
          [[("Heterogeneity: ", {"bold": True}), "a single retention rate understates the effect (Fader & Hardie 2010)"],
           [("Acquisition: ", {"bold": True}), "future new customers matter too; leverage 1.55 (Schulze et al. 2012)"],
           [("Market cap: ", {"bold": True}), "customer equity predicts it (Kumar & Shah 2009)"]],
          icon_name="LuCoins", body_size=12, name="Value caveats")
caption(s, "Effect of a 1% improvement in each lever. Gupta, Lehmann & Stuart (2004) Journal of Marketing Research 41(1): five firms valued from public data.", 4.85)
notes(s, "Gupta, Lehmann & Stuart (2004) value Amazon, Ameritrade, eBay and others as the sum of customer "
         "lifetime values. A 1% gain in retention raises firm value by about 5%, against about 1% for margin "
         "and 0.1% for acquisition cost. Schulze, Skiera & Wiesel (2012): a 10% rise in customer equity goes "
         "with about 15.5% higher shareholder value. McCarthy, Fader & Hardie (2017) build customer-based "
         "corporate valuation for subscription firms from disclosed churn data.")

# 14 Capital markets
s = content("Customer assets and the stock market")
bar_chart(s, X0, 1.35, 4.6, 3.3, ["Advertising", "Brand assets", "Customer assets"], [0.04, 0.33, 0.72],
          "Firm value elasticity", "0.00", 0.8, "Chart elasticities",
          colors=[None, None, NAVY])
band_card(s, 5.3, 1.4, 4.2, 3.3, "Satisfaction and returns",
          [[("Cash flows: ", {"bold": True}), "more growth, less volatility (Gruca & Rego 2005)"],
           [("Risk: ", {"bold": True}), "lower systematic risk (Tuli & Bharadwaj 2009)"],
           [("Returns: ", {"bold": True}), "high-ACSI portfolio 518% vs S&P 31%, 2000-2014 (Fornell et al. 2016)"],
           [("Contested: ", {"bold": True}), "mispricing limited to few firms (Jacobson & Mizik 2009)"]],
          icon_name="LuTrendingUp", body_size=12, name="Satisfaction returns")
caption(s, "Edeling & Fischer (2016) Journal of Marketing Research: 488 elasticities from 83 studies.", 4.85)
notes(s, "Edeling & Fischer (2016): mean firm-value elasticity .04 for advertising, .54 for marketing assets; "
         "customer-related assets .72 vs brand-related assets .33. Debate pair: Fornell, Mithas, Morgeson & "
         "Krishnan (2006) 'High returns, low risk' and Fornell, Morgeson & Hult (2016) versus Jacobson & Mizik "
         "(2009) and Sorescu & Sorescu (2016). Malshe, Colicev & Mittal (2020): dissatisfaction weighs about "
         "2.4 times more than satisfaction on abnormal returns.")

# ------------------------------------------------------------------ Part 4
section(4, "Churn", "predict, then manage",
        "Part 4, about 15 minutes: churn arithmetic, prediction and why targeting by risk can fail.")

# 16 Churn arithmetic
s = content("Small churn changes, large value changes")
rows = [["Retention", "Churn", "CLV", "Change"],
        ["70%", "30%", "175", "base"],
        ["80%", "20%", "267", "+52%"],
        ["90%", "10%", "450", "+157%"]]
table(s, rows, X0, 1.4, 5.4, 2.2, [1.3, 1.0, 2.0, 1.1], "CLV table", size=13, highlight=((3, 2), (3, 3)))
band_card(s, 6.1, 1.4, 3.4, 2.2, "Why so steep?",
          [[("Each point of churn ", {"bold": True}), "removes a share of every future year's margin"],
           [("Lifetime ", {"bold": True}), "rises sharply as churn falls"]],
          icon_name="LuCalculator", body_size=13, name="Churn why")
callout(s, 3.85, [[("Formula: ", {"bold": True}), "CLV = m · r ÷ (1 + d − r), with margin m = 100 and discount rate d = 10%."]],
        fill=LIGHT, color=BLACK, name="CLV formula")
caption(s, "Gupta & Lehmann (2005) Managing Customers as Investments; Hardie note 024 on CLV formulas.", 4.55)
notes(s, "Worked example with margin 100 per year and 10% discount rate: r = .7 gives 100 × .7 / .4 = 175; "
         "r = .8 gives 80 / .3 = 267; r = .9 gives 90 / .2 = 450. Ask students to compute r = .95 (950). Then "
         "discuss the assumptions: constant retention ignores heterogeneity (Fader & Hardie 2007, sBG model), so "
         "cohort retention rates rise over time.")

# 17 Predict vs manage
s = content("Predicting churn is not managing churn")
band_card(s, X0, 1.4, cw, 2.75, "Predict: who will leave?",
          [[("Methods matter: ", {"bold": True}), "the churn tournament found gaps worth hundreds of thousands of dollars per campaign"],
           [("Trees and boosting ", {"bold": True}), "beat plain logit"],
           [("Judge by profit, ", {"bold": True}), "not only AUC"]],
          icon_name="LuSearch", band=NAVY, body_size=13, name="Predict churn")
band_card(s, X0 + cw + GAP, 1.4, cw, 2.75, "Manage: whom to contact?",
          [[("Retention futility: ", {"bold": True}), "the riskiest customers are not the most responsive"],
           [("Target by uplift, ", {"bold": True}), "the effect of the offer on each customer"],
           [("Offers can backfire: ", {"bold": True}), "churn rose from 6% to 10% after plan recommendations"]],
          icon_name="LuTarget", body_size=13, name="Manage churn")
callout(s, 4.35, [[("Rule: ", {"bold": True}), "target customers whose behaviour the offer changes, weighted by their CLV."]],
        name="Churn rule")
caption(s, "Neslin et al. (2006) JMR; Lemmens & Croux (2006) JMR; Verbeke et al. (2012) EJOR; Ascarza (2018) JMR; "
           "Ascarza, Iyengar & Schleicher (2016) JMR; Lemmens & Gupta (2020) Marketing Science.", 5.0)
notes(s, "Ascarza (2018, 'Retention futility', field experiments at a mobile operator and a membership "
         "organisation): targeting by predicted treatment effect beats targeting by churn risk. Ascarza, Iyengar "
         "& Schleicher (2016): recommending cheaper plans raised churn from 6% to 10% by waking up inert "
         "customers. Counterpoint: Gattermann-Itschert & Thonemann (2022) find risk targeting works in a B2B "
         "field study. Classroom exercise: HBS 'Managing Customer Retention at Teleko' (Ascarza, free online tool).")

# ------------------------------------------------------------------ Part 5
section(5, "Share of wallet", "rank beats rating",
        "Part 5, about 15 minutes: satisfaction and share of wallet, the Wallet Allocation Rule, loyalty programmes.")

# 19 SOW evidence
s = content("Share of wallet follows rank")
bar_chart(s, X0, 1.35, 4.4, 3.3, ["Absolute satisfaction", "Rank (WAR)"], [9, 55],
          "Variance in share of deposits explained", '0"%"', 60, "Chart SOW variance", colors=[None, NAVY])
stats = [("≈" + NB + "0.1", "correlation of changes in satisfaction or NPS with changes in share of wallet", "Keiningham et al. (2011) HBR"),
         ("10×", "spending shifts can be worth up to ten times more than outright defections", "Coyles & Gokey (2005)")]
for i, (fig, lab, src) in enumerate(stats):
    y = 1.45 + i * 1.6
    rect(s, 5.1, y, 4.4, 1.4, name=f"SOW stat box {i + 1}")
    text(s, 5.25, y + 0.08, 1.4, 1.2, fig, size=26, bold=True, head=True, color=NAVY,
         anchor=MSO_ANCHOR.MIDDLE, name=f"SOW figure {i + 1}", space=0)
    text(s, 6.65, y + 0.1, 2.75, 1.2, [[(lab, {})], [(src, {"size": 10.5, "color": GREY_TEXT})]],
         size=12, name=f"SOW text {i + 1}", space=2)
caption(s, "Aksoy (2014) International Journal of Bank Marketing, 4,712 bank customers; Cooil et al. (2007) Journal "
           "of Marketing; Keiningham et al. (2015) Journal of Service Management.", 4.85)
notes(s, "Cooil et al. (2007): 4,319 Canadian bank households over five years; changes in satisfaction relate "
         "positively but weakly to changes in share of wallet. Keiningham et al. (2015): 79,543 consumers, 650+ "
         "brands, 20 industries; ranked satisfaction links far more strongly to share of wallet. Coyles & Gokey "
         "(2005, McKinsey): 1,200 households, 16 industries.")

# 20 WAR exercise
s = content("The Wallet Allocation Rule in class")
rect(s, X0, 1.4, 4.3, 1.3, fill=NAVY, name="WAR formula box")
text(s, X0 + 0.2, 1.48, 3.9, 0.4, "Wallet Allocation Rule", size=13, bold=True, color=T.ACCENT_6, name="WAR label")
text(s, X0 + 0.2, 1.88, 3.9, 0.7, "SOW = (1 − rank ÷ (n + 1)) × 2 ÷ n", size=20, bold=True, head=True,
     color=WHITE, name="WAR formula")
rows = [["Rank among 3 brands", "Predicted share"], ["1st", "50%"], ["2nd", "33%"], ["3rd", "17%"]]
table(s, rows, X0, 2.9, 4.3, 1.6, [2.6, 1.7], "WAR table", size=13, highlight=((1, 1),))
steps = ["Each student lists the supermarkets they used last month",
         "Rank them from most to least preferred",
         "Estimate the actual split of spending",
         "Compare predicted and actual shares in a scatter plot"]
for i, t in enumerate(steps):
    y = 1.4 + i * 0.78
    number(s, 5.1, y + 0.12, i + 1, d=0.4, size=12, name=f"WAR step number {i + 1}")
    text(s, 5.65, y, 3.85, 0.65, t, size=13, anchor=MSO_ANCHOR.MIDDLE, name=f"WAR step {i + 1}", space=0)
callout(s, 4.7, "To grow share, improve your rank against the brands customers also use.", h=0.5, name="WAR callout")
notes(s, "Keiningham, Aksoy, Buoye & Cooil (2011, HBR) and the book The Wallet Allocation Rule (Wiley 2015). n = "
         "number of brands the customer uses. With three brands: rank 1 = (1 − 1/4) × 2/3 = 50%, rank 2 = 33%, "
         "rank 3 = 17%. Takes about 10 minutes with an online poll. Debate link: Buoye et al. (2016) reconcile WAR "
         "with Double Jeopardy.")

# 21 Loyalty programmes
s = content("Loyalty programmes: smaller effects")
stat_rows(s, [
    ("7×", "smaller programme effect on share of wallet once self-selection of heavy buyers is controlled.",
     "Leenheer, van Heerde, Bijmolt & Smidts (2007) IJRM"),
    ("6-9", "months until the behaviour change after joining fades again.",
     "Meyer-Waarden & Benavent (2009) JAMS"),
    ("4.4%", "annual growth for high loyalty spenders vs 5.5% for low spenders, 55 listed firms.",
     "McKinsey (2013) Making loyalty pay")], prefix="LP")
callout(s, 4.45, [[("Local cases: ", {"bold": True}),
                   "jö Bonus Club (4.5 to 4.7m members) and Payback; Starbucks members bring 57 to 60% of US tender."]],
        h=0.65, fill=LIGHT, color=BLACK, name="LP cases")
notes(s, "Belli et al. (2022, JAMS) meta-analysis of 429 effects: programmes raise behavioural loyalty, attitudinal "
         "loyalty barely moves. Liu (2007, JM): light and moderate buyers change, heavy buyers only redeem. Ask: "
         "do Starbucks members spend more because of the programme, or did heavy buyers join? jö figures are "
         "self-reported (press, 2025); Billa '-25%' stickers became member-only in July 2025.")

# ------------------------------------------------------------------ Part 6
section(6, "Critiques and application", "where the chain breaks",
        "Part 6, about 15 minutes: loyalty versus profitability, boundary conditions, lab and cases.")

# 23 Loyalty x profitability grid
s = content("Loyalty is not the same as profitability")
gx, gy, gw2, gh = 2.1, 1.35, 6.4, 3.6
quads = [("Barnacles", "Loyal but unprofitable: raise share of wallet or cut cost to serve", 0, 0, LIGHT, BLACK, NAVY),
         ("True friends", "Loyal and profitable: keep, reward, nurture", 1, 0, NAVY, WHITE, WHITE),
         ("Strangers", "Neither: do not invest", 0, 1, LIGHT, BLACK, NAVY),
         ("Butterflies", "Profitable but short-lived: harvest, do not chase loyalty", 1, 1, BLUE, WHITE, WHITE)]
qw, qh = (gw2 - 0.1) / 2, (gh - 0.1) / 2
for h, b, cx, cy, fill, col, hcol in quads:
    x, y = gx + cx * (qw + 0.1), gy + cy * (qh + 0.1)
    rect(s, x, y, qw, qh, fill=fill, name=f"Quadrant {h}")
    text(s, x + 0.15, y + 0.1, qw - 0.3, 0.45, h, size=15, bold=True, head=True, color=hcol, name=f"Quadrant heading {h}")
    text(s, x + 0.15, y + 0.6, qw - 0.3, qh - 0.7, b, size=13, color=col, name=f"Quadrant text {h}")
text(s, X0, gy + gh / 2 - 0.5, 1.5, 1.0, "Loyalty: expected relationship length", size=11,
     color=GREY_TEXT, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE, name="Axis loyalty")
text(s, gx, gy + gh + 0.05, gw2, 0.3, "Profitability →", size=11, color=GREY_TEXT, align=PP_ALIGN.CENTER,
     name="Axis profit")
text(s, X0, gy, 1.5, 0.3, "long", size=11, color=GREY_TEXT, align=PP_ALIGN.RIGHT, name="Axis long")
text(s, X0, gy + gh - 0.3, 1.5, 0.3, "short", size=11, color=GREY_TEXT, align=PP_ALIGN.RIGHT, name="Axis short")
caption(s, "Reinartz & Kumar (2002) Harvard Business Review; Reinartz & Kumar (2000) Journal of Marketing.", gy + gh + 0.4)
notes(s, "Reinartz & Kumar (2002), 16,000 customers in four firms: no support that loyal customers cost less, pay "
         "more or recommend more. Shah et al. (2012, JM): 10 to 35% of cross-buyers are unprofitable and cause 39 "
         "to 88% of the losses from customers. Ask students to place their own phone, bank and supermarket "
         "relationships in the grid from the firm's point of view.")

# 24 Where the chain breaks
s = content("Where the chain breaks")
devs = [("NPS", "No better at predicting growth than satisfaction", "Keiningham et al. (2007); van Doorn et al. (2013)"),
        ("Penetration", "Brands grow mainly by acquisition; loyalty follows size", "Ehrenberg et al. (1990); Riebe et al. (2014)"),
        ("Cross-buying", "Growing wallet share can attract unprofitable buyers", "Shah et al. (2012)"),
        ("Satisfaction cost", "Very high satisfaction can lower shareholder returns", "Guenther & Guenther (2021)"),
        ("Employees", "Employee satisfaction does not always lift profit", "Silvestro (2002)"),
        ("Lock-in", "Switching barriers retain only while experience is poor", "Gao, Melero-Polo & Sese (2022)")]
for i, (h, b, src) in enumerate(devs):
    x = X0 + (i % 2) * (cw + GAP)
    y = 1.35 + (i // 2) * 1.32
    rect(s, x, y, cw, 1.18, name=f"Break {i + 1}")
    rect(s, x, y + 0.12, 0.07, 0.94, fill=BLUE, name=f"Break bar {i + 1}")
    text(s, x + 0.2, y + 0.05, cw - 0.3, 1.1,
         [[(h, {"bold": True, "color": NAVY, "head": True, "size": 14})], [(b, {})],
          [(src, {"size": 10.5, "color": GREY_TEXT})]], size=12, name=f"Break text {i + 1}", space=2)
notes(s, "Debate motion (10 minutes): 'Firms should spend their loyalty budget on acquisition instead.' Half the "
         "room argues Heskett/Reichheld, half Sharp/Reinartz. Gao et al. (2022): lock-in reduces churn mainly when "
         "experience scores are below 5 of 10 and stops mattering above 7. ACSI (Q1 2026) warns of 'pent-up "
         "defection': dissatisfied customers who stay for lack of alternatives.")

# 25 Lab
s = content("Lab: churn and CLV in real data")
stepper(s, ["Data", "Describe", "Model", "Value", "Decide"])
band_card(s, X0, 2.15, 3.6, 2.45, "Data and tools",
          [[("IBM Telco: ", {"bold": True}), f"7,043{NB}customers, churn flag"],
           [("CDNOW: ", {"bold": True}), f"2,357{NB}customer sample, purchases"],
           [("R: ", {"bold": True}), "CLVTools, BTYDplus (WU), survival"],
           [("Python: ", {"bold": True}), "PyMC-Marketing, lifelines"]],
          icon_name="LuDatabase", body_size=12, name="Lab data")
tasks = ["Plot retention curves by contract type (Kaplan-Meier)",
         "Fit a logit churn model; build a decile lift table",
         "Fit BG/NBD on CDNOW; compute P(alive) and annual CLV",
         "Value the base: who is worth a retention offer?"]
for i, t in enumerate(tasks):
    y = 2.15 + i * 0.62
    number(s, 4.35, y + 0.05, i + 1, d=0.38, size=12, name=f"Task number {i + 1}")
    text(s, 4.85, y, 4.65, 0.55, t, size=12, anchor=MSO_ANCHOR.MIDDLE, name=f"Task {i + 1}", space=0)
callout(s, 4.75, "Deliverable: one retention chart, one CLV table, half a page on whom to target and why.",
        h=0.5, name="Deliverable")
caption(s, "Data: Kaggle (IBM Telco Customer Churn); brucehardie.com/datasets (CDNOW). Method: Fader, Hardie & Lee (2005) Marketing Science.", 5.3)
notes(s, "IBM Telco is the standard churn teaching set (tenure and churn flag allow survival analysis). CDNOW ships "
         "with CLVTools, BTYD and PyMC-Marketing. The Python package lifetimes is no longer maintained; use "
         "PyMC-Marketing. BTYDplus is by Michael Platzer and Thomas Reutterer (WU): Pareto/GGG and MBG/CNBD-k "
         "models that use purchase regularity.")

# 26 Cases
s = content("Teaching cases")
items = [("Pilgrim Bank", "Cases (A) and (B), customer-level data: are online customers more profitable and better retained?",
          "Profit, retention, selection bias", "HBS 602104 / 602095"),
         ("Teleko", "Choose whom to target with a retention offer: churn risk or uplift?",
          "Churn management", "HBS 523005, free online tool"),
         ("Harrah's", "Total Rewards raised share of a gaming budget that started at 36%.",
          "Share of wallet, loyalty data", "HBS 502011; Loveman (2003) HBR")]
for i, (h, facts, lesson, src) in enumerate(items):
    x = X0 + i * (cw3 + GAP)
    band_card(s, x, 1.35, cw3, 2.85, h,
              [[(facts, {})], [(lesson, {"bold": True, "color": NAVY})], [(src, {"size": 10.5, "color": GREY_TEXT})]],
              body_size=13, name=f"Case {h}")
callout(s, 4.4, [[("Also: ", {"bold": True}), "Sears (service-profit chain), Starbucks: Delivering Customer Service, Netflix (Darden, CLV and valuation)."]],
        h=0.6, name="More cases")
notes(s, "Pilgrim Bank (Frei & Campbell, HBS 2001) comes with data for about 30,000 customers; (B) adds a second "
         "year for a retention model. Teleko (Ascarza, HBS 2022) is a two-page exercise with a free online tool. "
         "Harrah's (Lal, HBS 2001) and Loveman's 'Diamonds in the Data Mine' (HBR 2003). Starbucks (Moon & "
         "Quelch, HBS) asks whether a USD 40m service investment pays off.")

# 27 References
s = content("References")
rw = cw3
band_card(s, X0, 1.35, rw, 3.35, "Core reading",
          [[("Heskett et al. (1994) ", {"bold": True}), "Putting the service-profit chain to work, HBR"],
           [("Gupta & Zeithaml (2006) ", {"bold": True}), "Customer metrics, Marketing Science"],
           [("Hogreve et al. (2017) ", {"bold": True}), "SPC meta-analysis, JM"],
           [("Gupta et al. (2004) ", {"bold": True}), "Valuing customers, JMR"],
           [("Keiningham et al. (2015) ", {"bold": True}), "Perceptions are relative, JOSM"]],
          icon_name="LuGraduationCap", body_size=11, name="References core")
band_card(s, X0 + rw + GAP, 1.35, rw, 3.35, "Frameworks",
          [[("Srivastava et al. (1998) ", {"bold": True}), "Market-based assets, JM"],
           [("Rust et al. (2004) ", {"bold": True}), "Return on marketing, JM"],
           [("Reinartz & Kumar (2002) ", {"bold": True}), "Mismanagement of loyalty, HBR"],
           [("Otto et al. (2020) ", {"bold": True}), "Satisfaction meta-analysis, JAMS"],
           [("Edeling & Fischer (2016) ", {"bold": True}), "Firm value meta-analysis, JMR"]],
          icon_name="LuLibrary", body_size=11, name="References frameworks")
band_card(s, X0 + 2 * (rw + GAP), 1.35, rw, 3.35, "Churn, methods",
          [[("Ascarza (2018) ", {"bold": True}), "Retention futility, JMR"],
           [("Neslin et al. (2006) ", {"bold": True}), "Defection detection, JMR"],
           [("Fader et al. (2005) ", {"bold": True}), "BG/NBD, Marketing Science"],
           [("McCarthy et al. (2017) ", {"bold": True}), "Valuing subscription firms, JM"],
           [("Platzer & Reutterer (2016) ", {"bold": True}), "Pareto/GGG, Marketing Science"]],
          icon_name="LuChartColumn", body_size=11, name="References methods")
notes(s, "381 further sources with access notes: Notion page and GitHub folder 'Customer Loyalty, Churn and Share "
         "of Wallet (Service-Profit Chain)' (github.com/arnefloh-wu/search-teaching-materials). Most journal "
         "articles are paywalled; check WU access. Free: Wirtz (2017) Managing Customer Relationships and Building "
         "Loyalty (78-page PDF on jochenwirtz.com), Hardie's notes (brucehardie.com/notes), Aksoy et al. (2009) "
         "NIM Marketing Intelligence Review.")

# 28 Takeaways
s = content("Key takeaways")
tk = [("Metrics: ", "measure loyalty, churn and share of wallet separately."),
      ("Service-profit chain: ", "every link holds on average, but effects depend on the setting."),
      ("Satisfaction: ", "relates to performance, modestly and nonlinearly."),
      ("Retention: ", "is the strongest lever in customer equity and shows up in firm value."),
      ("Share of wallet: ", "follows a brand's rank against competitors, not its satisfaction score."),
      ("Limits: ", "loyalty is not profit; target churn offers by uplift and CLV.")]
for i, (lead, rest) in enumerate(tk):
    y = 1.35 + i * 0.58
    rect(s, X0, y, W0, 0.5, name=f"Takeaway row {i + 1}")
    number(s, X0 + 0.12, y + 0.06, i + 1, d=0.38, size=13, name=f"Takeaway number {i + 1}")
    text(s, X0 + 0.7, y, W0 - 0.85, 0.5, [[(lead, {"bold": True, "color": NAVY}), rest]], size=13,
         anchor=MSO_ANCHOR.MIDDLE, name=f"Takeaway text {i + 1}", space=0)
callout(s, 4.95, [[("Next: ", {"bold": True}), "the churn and CLV lab. Bring a laptop with R or Python installed."]],
        h=0.5, name="Next")
notes(s, "Return to slide 2: which claims in the left column survived the evidence, and which need conditions?")

# 29 Closing
s = prs.slides.add_slide(LAY["Abschlussfolie Kontakt"])
drop_empty(s, keep=())
footer(s)
notes(s, "Questions and discussion.")

prs.save(OUT)
print("saved", OUT, len(prs.slides), "slides")
