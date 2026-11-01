"""Generate the animated SVGs for the migikun474 profile README.

Design: "silicon wafer". Oxide-blue ground, a die grid with scribe lines,
thin-film interference colours on the name, gold for whatever is active.
Type: Bricolage Grotesque for words, IBM Plex Mono only for real code.

Everything is self-contained SVG (CSS keyframes + SMIL). Fonts are subset to
the characters each file uses and embedded as WOFF2 data URIs, so GitHub
shows the real typefaces inside <img>.

Usage: python3 generate.py OUT_DIR FONT_DIR
FONT_DIR holds the @fontsource WOFF2 files (bricolage-grotesque-latin-*,
ibm-plex-mono-latin-*).
"""
import base64, io, math, os, random, re, sys
from fontTools import subset
from fontTools.ttLib import TTFont

OUT, FONTS = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)

# ---- tokens ---------------------------------------------------------------
OXIDE, DIE, SCRIBE = "#172036", "#1e2a45", "#2e3d60"
INK, HAZE = "#edf0f7", "#8e9bbb"
GOLD, TEAL, VIOLET, CORAL = "#f0b84f", "#57d3bd", "#a58cf5", "#ff8266"
ACTIVE_FILL = "#27365a"
FILM = ["#a58cf5", "#6b8cf0", "#57d3bd", "#f0b84f", "#e86aa6", "#a58cf5"]  # oxide interference order

FACES = [("Brico", 500, "bricolage-grotesque-latin-500-normal.woff2"),
         ("Brico", 700, "bricolage-grotesque-latin-700-normal.woff2"),
         ("Brico", 800, "bricolage-grotesque-latin-800-normal.woff2"),
         ("Plex", 400, "ibm-plex-mono-latin-400-normal.woff2"),
         ("Plex", 600, "ibm-plex-mono-latin-600-normal.woff2")]
SANS = "Brico,'Segoe UI',Ubuntu,Arial,sans-serif"
MONO = "Plex,ui-monospace,Menlo,Consolas,monospace"

BASE_CSS = f"""
text{{font-family:{SANS};font-weight:500;}}
:where(text:not([fill])){{fill:{INK};}}
.code{{font-family:{MONO};font-weight:400;}}
.haze{{fill:{HAZE};}} .gold{{fill:{GOLD};}} .teal{{fill:{TEAL};}} .violet{{fill:{VIOLET};}} .coral{{fill:{CORAL};}}
.title{{font-weight:800;font-size:21px;letter-spacing:-0.2px;}}
.sub{{font-size:13.5px;fill:{HAZE};}}
.label{{font-weight:700;font-size:12.5px;fill:{HAZE};}}
@media (prefers-reduced-motion: reduce){{*{{animation:none!important;}}}}
"""


def font_faces(svg_text):
    """@font-face rules for only the faces and characters this SVG uses."""
    chars = set("".join(re.findall(r">([^<]+)<", svg_text)))
    chars |= set(" 0123456789")
    rules = []
    for fam, wt, fn in FACES:
        is_mono = fam == "Plex"
        used = ('class="code' in svg_text or "code " in svg_text) if is_mono else True
        if not used:
            continue
        f = TTFont(os.path.join(FONTS, fn))
        opts = subset.Options()
        opts.flavor = "woff2"
        opts.layout_features = ["kern", "liga", "calt", "tnum"]
        opts.name_IDs = []
        s = subset.Subsetter(opts)
        s.populate(text="".join(chars))
        s.subset(f)
        buf = io.BytesIO()
        f.flavor = "woff2"
        f.save(buf)
        b64 = base64.b64encode(buf.getvalue()).decode()
        rules.append(f"@font-face{{font-family:{fam};font-weight:{wt};src:url(data:font/woff2;base64,{b64}) format('woff2');}}")
    return "\n".join(rules)


def svg(w, h, body, css="", label="", defs=""):
    doc = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">
<title>{label}</title>
<style>/*FONTS*/{BASE_CSS}{css}</style>
<defs>
  <pattern id="dies" width="64" height="48" patternUnits="userSpaceOnUse"><rect x="2" y="2" width="60" height="44" rx="2" fill="none" stroke="{SCRIBE}" stroke-width="0.8"/></pattern>
  {defs}
</defs>
<rect width="{w}" height="{h}" rx="14" fill="{OXIDE}"/>
<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="14" fill="none" stroke="{SCRIBE}"/>
{body}
</svg>"""
    return doc.replace("/*FONTS*/", font_faces(doc))


def write(name, content):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(content)
    print(f"{name}: {len(content)/1024:.1f} KB")


def halo(cx_anim, r, col):
    """A crisp dot with a soft, flat halo (no blur filters)."""
    return f'<circle r="{r*2.4}" fill="{col}" opacity=".18">{cx_anim}</circle><circle r="{r}" fill="{col}">{cx_anim}</circle>'


# ---------------------------------------------------------------- hero
def hero():
    W, H = 900, 260
    lines = [
        "compiling C-like source → TAC → MIPS",
        "parsing market data with SWAR and AVX2",
        "reading the clock without a syscall",
        "simulating quantum magnets and QAOA",
    ]
    cyc, step = 16, 4
    x0, y0, cw = 232, 184, 10.25
    sub = []
    for i, s in enumerate(lines):
        w = len(s) * cw + 6
        kt = "0;0.11;0.22;0.245;1"
        sub.append(f"""
  <clipPath id="cl{i}"><rect x="{x0}" y="{y0-18}" height="26" width="0">
    <animate attributeName="width" values="0;{w:.0f};{w:.0f};0;0" keyTimes="{kt}" dur="{cyc}s" begin="{i*step}s" repeatCount="indefinite"/></rect></clipPath>
  <text x="{x0}" y="{y0}" font-size="17" class="code teal" clip-path="url(#cl{i})">{s}</text>
  <rect y="{y0-15}" width="9" height="19" fill="{GOLD}" opacity="0">
    <animate attributeName="x" values="{x0};{x0+w:.0f};{x0+w:.0f};{x0};{x0}" keyTimes="{kt}" dur="{cyc}s" begin="{i*step}s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;1;1;0;0" keyTimes="{kt}" dur="{cyc}s" begin="{i*step}s" repeatCount="indefinite" calcMode="discrete"/>
  </rect>""")
    stops = "".join(f'<stop offset="{i/(len(FILM)-1):.2f}" stop-color="{c}"/>' for i, c in enumerate(FILM))
    defs = f"""<linearGradient id="film" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="520" y2="60" spreadMethod="repeat">{stops}
    <animateTransform attributeName="gradientTransform" type="translate" values="0 0;520 0" dur="7s" repeatCount="indefinite"/></linearGradient>
  <linearGradient id="sheen" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{INK}" stop-opacity="0"/><stop offset=".5" stop-color="{INK}" stop-opacity=".07"/><stop offset="1" stop-color="{INK}" stop-opacity="0"/></linearGradient>
  <radialGradient id="vig" cx=".5" cy=".55" r=".75"><stop offset=".55" stop-color="{OXIDE}" stop-opacity="0"/><stop offset="1" stop-color="{OXIDE}" stop-opacity=".95"/></radialGradient>
  <clipPath id="card"><rect width="{W}" height="{H}" rx="14"/></clipPath>"""
    per, yb = 80, 236
    sq = " ".join(f"M{k*per} {yb} H{k*per+18} V{yb-9} H{k*per+58} V{yb} H{(k+1)*per}" for k in range(0, 2 * W // per + 2))
    css = f"""
.name{{font-weight:800;font-size:70px;letter-spacing:-1.5px;}}
.sheen{{animation:sheen 9s ease-in-out infinite;}}
@keyframes sheen{{0%{{transform:translateX(-420px) skewX(-20deg);}}60%,100%{{transform:translateX({W+200}px) skewX(-20deg);}}}}
.clock{{animation:slide 5s linear infinite;}}
@keyframes slide{{from{{transform:translateX(0);}}to{{transform:translateX(-{per*5}px);}}}}
.prompt{{animation:blink 1.1s steps(1) infinite;}}
@keyframes blink{{50%{{opacity:0;}}}}
.rise{{opacity:0;animation:rise 1.4s .2s cubic-bezier(.2,.8,.2,1) forwards;}}
@keyframes rise{{from{{opacity:0;transform:translateY(14px);}}to{{opacity:1;transform:translateY(0);}}}}
"""
    body = f"""
<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" fill="url(#dies)" opacity=".38"/>
  <rect width="{W}" height="{H}" fill="url(#vig)"/>
  <rect class="sheen" x="0" y="-40" width="260" height="{H+80}" fill="url(#sheen)"/>
  <path class="clock" d="{sq}" fill="none" stroke="{SCRIBE}" stroke-width="1.4"/>
</g>
<text x="40" y="44" font-size="14" class="haze">IIT Roorkee</text>
<text x="{W-40}" y="44" font-size="14" class="haze" text-anchor="end">github.com/migikun474</text>
<g class="rise">
  <text x="{W/2}" y="74" text-anchor="middle" font-size="15" class="haze">Amirishetty</text>
  <text x="{W/2}" y="138" text-anchor="middle" class="name" fill="url(#film)">Sai Vignesh</text>
</g>
<text x="{x0-24}" y="{y0}" font-size="17" class="code haze prompt">$</text>
{''.join(sub)}
"""
    write("hero.svg", svg(W, H, body, css, "Amirishetty Sai Vignesh: compilers, low-latency C and quantum computing", defs))


# ---------------------------------------------------------------- compiler
def compiler():
    W, H, cyc = 900, 350, 11.0
    top = [("source.c", "x = a + b * 2;"), ("Preprocess", "#define, #include"), ("Lexer (Flex)", "ID = ID + ID * NUM"),
           ("Parser, LALR(1)", "= x (+ a (* b 2))"), ("Semantics", "types, scopes ✓")]
    bot = [("Three Address Code", "t1 = b * 2"), ("Optimizer", "-O1  -O2  -O3"), ("MIPS + regalloc", "sll $t0, $a1, 1"), ("SPIM", "output == gcc ✓")]
    bw, bh, gap, ty, by = 152, 60, 19, 100, 232
    boxes = [(22 + i * (bw + gap), ty, a, b, bw) for i, (a, b) in enumerate(top)]
    bw2, gap2 = 190, 26
    boxes += [(22 + (3 - i) * (bw2 + gap2), by, a, b, bw2) for i, (a, b) in enumerate(bot)]
    n, travel = len(boxes), 0.82
    centers, rects = [], []
    for i, (x, y, a, b, w) in enumerate(boxes):
        cx, cy = x + w / 2, y + bh / 2
        centers.append((cx, cy))
        t = i / (n - 1) * travel * cyc
        rects.append(f"""
  <g class="stage" style="animation-delay:{t-0.25:.2f}s">
    <rect x="{x}" y="{y}" width="{w}" height="{bh}" rx="8" fill="{DIE}" stroke="{SCRIBE}" stroke-width="1.5" class="box"/>
    <text x="{cx}" y="{y+25}" text-anchor="middle" font-size="14.5" font-weight="700" class="lbl">{a}</text>
    <text x="{cx}" y="{y+45}" text-anchor="middle" font-size="12" class="code haze art">{b}</text>
  </g>""")
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in centers)
    seg = [math.dist(centers[i], centers[i + 1]) for i in range(n - 1)]
    L, acc = sum(seg), [0.0]
    for s_ in seg:
        acc.append(acc[-1] + s_)
    kp = ";".join(f"{a/L:.4f}" for a in acc) + ";1"
    kt = ";".join(f"{i/(n-1)*travel:.4f}" for i in range(n)) + ";1"
    motion = f'<animateMotion dur="{cyc}s" repeatCount="indefinite" path="{d}" keyPoints="{kp}" keyTimes="{kt}" calcMode="linear"/>'
    packet = f'<circle r="15" fill="{GOLD}" opacity=".16">{motion}</circle><circle r="6.5" fill="{GOLD}">{motion}</circle>'
    css = f"""
.stage .box{{animation:hl {cyc}s linear infinite;animation-delay:inherit;}}
.stage .lbl{{animation:hlt {cyc}s linear infinite;animation-delay:inherit;}}
.stage .art{{animation:hla {cyc}s linear infinite;animation-delay:inherit;}}
@keyframes hl{{0%{{stroke:{SCRIBE};fill:{DIE};}}2%,9%{{stroke:{GOLD};fill:{ACTIVE_FILL};}}16%,100%{{stroke:{SCRIBE};fill:{DIE};}}}}
@keyframes hlt{{0%{{fill:{INK};}}2%,9%{{fill:{GOLD};}}16%,100%{{fill:{INK};}}}}
@keyframes hla{{0%{{fill:{HAZE};}}2%,9%{{fill:{TEAL};}}16%,100%{{fill:{HAZE};}}}}
.flow{{stroke-dasharray:5 9;animation:dash 1.4s linear infinite;}}
@keyframes dash{{to{{stroke-dashoffset:-28;}}}}
.ok{{opacity:0;animation:ok {cyc}s linear infinite;}}
@keyframes ok{{0%,80%{{opacity:0;}}84%,96%{{opacity:1;}}100%{{opacity:0;}}}}
"""
    body = f"""
<text x="22" y="42" class="title">COMPILER-DESIGN</text>
<text x="22" y="66" class="sub">A C-like language with classes, references and overloading, compiled to MIPS. C++17, Flex and Bison.</text>
<text x="22" y="{ty-10}" class="label">Front end</text>
<text x="22" y="{by-10}" class="label">Back end</text>
<path d="{d}" fill="none" stroke="{SCRIBE}" stroke-width="2"/>
<path d="{d}" fill="none" stroke="{GOLD}" stroke-width="2" opacity=".45" class="flow"/>
{packet}
{''.join(rects)}
<g class="ok"><rect x="22" y="{H-44}" width="400" height="28" rx="14" fill="#173a3e" stroke="{TEAL}"/>
<text x="222" y="{H-25}" text-anchor="middle" font-size="13" class="teal">Every test prints exactly what gcc's binary prints</text></g>
<text x="{W-22}" y="{H-25}" text-anchor="end" font-size="13" class="haze">87 semantic, 34 TAC and 33 SPIM checks pass</text>
"""
    write("compiler.svg", svg(W, H, body, css, "Compiler pipeline: source.c through the lexer, LALR(1) parser, semantic analysis, TAC, optimizer and MIPS on SPIM"))


# ---------------------------------------------------------------- fastparse
def fastparse():
    W, H, cyc = 900, 320, 9.0
    rows = [list("12345678"), ["12", "34", "56", "78"], ["1234", "5678"], ["12345678"]]
    ops = ["− '0'", "× 10 +", "× 100 +", "× 10⁴ +"]
    left, top, rowh, span = 30, 104, 46, 350
    strokes = [SCRIBE, TEAL, TEAL, GOLD]
    fills = ["", "teal", "teal", "gold"]
    parts = []
    for r, cells in enumerate(rows):
        k = len(cells)
        cw = span / k
        appear = 0.4 + r * 1.3
        for i, c in enumerate(cells):
            x = left + i * cw
            parts.append(f"""<g class="cell" style="animation-delay:{appear + i*0.05:.2f}s">
  <rect x="{x+3:.1f}" y="{top + r*rowh}" width="{cw-6:.1f}" height="32" rx="6" fill="{DIE}" stroke="{strokes[r]}" stroke-width="1.3"/>
  <text x="{x + cw/2:.1f}" y="{top + r*rowh + 21}" text-anchor="middle" font-size="{15 if r < 3 else 17}" font-weight="600" class="code {fills[r]}">{c}</text></g>""")
        parts.append(f'<text x="{left+span+14}" y="{top + r*rowh + 21}" font-size="13" class="code haze cell" style="animation-delay:{appear:.2f}s">{ops[r]}</text>')
    bx, by0, bwmax = 486, 132, 340
    bars = [("Reference parser", 973, HAZE), ("AVX2, gcc", 4071, TEAL), ("AVX2, clang", 5311, GOLD)]
    out = []
    for i, (lab, v, col) in enumerate(bars):
        y = by0 + i * 54
        w = bwmax * v / 5311
        inside = w > 130
        out.append(f"""
<text x="{bx}" y="{y-9}" font-size="13.5">{lab}</text>
<rect x="{bx}" y="{y}" width="{bwmax}" height="18" rx="9" fill="{DIE}"/>
<rect x="{bx}" y="{y}" width="{w:.1f}" height="18" rx="9" fill="{col}" class="bar" style="animation-delay:{0.3 + i*0.45:.2f}s"/>
<text x="{bx + w - 8 if inside else bx + w + 8:.1f}" y="{y+13.5}" font-size="12" font-weight="600" text-anchor="{'end' if inside else 'start'}" fill="{OXIDE if inside else INK}" class="code val" style="animation-delay:{1.6 + i*0.45:.2f}s">{v:,} MB/s</text>""")
    css = f"""
.cell{{opacity:0;animation:pop {cyc}s ease-out infinite;}}
@keyframes pop{{0%{{opacity:0;transform:translateY(-8px);}}6%{{opacity:1;transform:translateY(0);}}88%{{opacity:1;}}96%,100%{{opacity:0;}}}}
.bar{{transform-box:fill-box;transform-origin:left;transform:scaleX(0);animation:grow {cyc}s cubic-bezier(.2,.8,.2,1) infinite;}}
@keyframes grow{{0%{{transform:scaleX(0);}}22%,88%{{transform:scaleX(1);}}96%,100%{{transform:scaleX(0);}}}}
.val{{opacity:0;animation:fade {cyc}s linear infinite;}}
@keyframes fade{{0%{{opacity:0;}}6%,70%{{opacity:1;}}78%,100%{{opacity:0;}}}}
"""
    body = f"""
<text x="30" y="42" class="title">fastparse</text>
<text x="30" y="66" class="sub">Market-data text to fixed-point integers. One parser, five ways: loop, SWAR, x86-64 asm, SSE, AVX2.</text>
<text x="30" y="94" class="label">SWAR: eight digits in three multiply-adds</text>
{''.join(parts)}
<line x1="456" y1="84" x2="456" y2="{H-30}" stroke="{SCRIBE}"/>
<text x="{bx}" y="94" class="label">Binance BTCUSDT price column, 3.56M rows</text>
{''.join(out)}
<text x="{bx}" y="{H-26}" font-size="13.5" class="gold">5.5× the reference, and checked against it on every PR</text>
"""
    write("fastparse.svg", svg(W, H, body, css, "fastparse: SWAR digit combining and AVX2 throughput up to 5,311 MB/s against a 973 MB/s reference"))


# ---------------------------------------------------------------- fasttime
def fasttime():
    W, H = 900, 310
    lanes = [("ft_now_ns()  rdtsc", 16, None, GOLD), ("clock_gettime  tsc, vDSO", 20, None, TEAL),
             ("clock_gettime  hpet", 1213, 4.0, VIOLET), ("clock_gettime  acpi_pm", 1966, 6.5, CORAL)]
    x0, x1, kx, y0, gap = 310, 815, 565, 124, 44
    out = []
    for i, (lab, ns, hold, col) in enumerate(lanes):
        y = y0 + i * gap
        out.append(f'<text x="30" y="{y+4.5}" font-size="13" class="code">{lab}</text>')
        out.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{SCRIBE}" stroke-width="2" stroke-linecap="round"/>')
        out.append(f'<text x="{x1+14}" y="{y+4.5}" font-size="13" font-weight="600" class="code" fill="{col}">{ns:,} ns</text>')
        if hold is None:
            dur = 1.2 * ns / 16
            for lag in (0, dur / 3, 2 * dur / 3):
                a = f'<animate attributeName="cx" values="{x0};{x1}" dur="{dur:.2f}s" begin="{lag:.2f}s" repeatCount="indefinite"/>'
                out.append(f'<circle cy="{y}" r="11" fill="{col}" opacity=".16">{a}</circle><circle cy="{y}" r="4.5" fill="{col}">{a}</circle>')
        else:
            go = 0.6
            dur = 2 * go + hold
            k1, k2 = go / dur, (go + hold) / dur
            out.append(f"""<rect x="{kx-34}" y="{y-12}" width="68" height="24" rx="6" fill="#3a2230" stroke="{CORAL}" stroke-width="1">
  <animate attributeName="stroke-opacity" values="1;.3;1" dur="1.2s" repeatCount="indefinite"/></rect>
<text x="{kx}" y="{y-17}" text-anchor="middle" font-size="11.5" class="coral">syscall into the kernel</text>""")
            a = f'<animate attributeName="cx" values="{x0};{kx};{kx};{x1}" keyTimes="0;{k1:.3f};{k2:.3f};1" dur="{dur:.2f}s" repeatCount="indefinite"/>'
            out.append(f'<circle cy="{y}" r="4.5" fill="{col}">{a}</circle>')
    body = f"""
<text x="30" y="42" class="title">fasttime</text>
<text x="30" y="66" class="sub">Is your Linux clock read secretly a system call? Median cost per read on a bare-metal laptop.</text>
<text x="{x0}" y="94" class="label">Each dot is one clock read</text>
{''.join(out)}
<text x="30" y="{H-20}" font-size="12.5" class="haze">The fast lanes run at true relative speed. Kernel waits are shortened about 18× so those dots still move.</text>
"""
    write("fasttime.svg", svg(W, H, body, "", "fasttime: rdtsc and vDSO clock reads take 16 to 20 ns; hpet and acpi_pm reads trap into the kernel"))


# ---------------------------------------------------------------- quantum (Q-peptide)
def quantum():
    W, H, cyc = 900, 330, 6.0
    nq, qy0, qg = 5, 108, 38
    xs = {"H": 74, "C1": 146, "M1": 228, "C2": 296, "M2": 378, "Z": 432}
    wires, gates = [], []
    for q in range(nq):
        y = qy0 + q * qg
        wires.append(f'<text x="28" y="{y+4.5}" font-size="12.5" class="code haze">q{q}</text><line x1="52" y1="{y}" x2="458" y2="{y}" stroke="{SCRIBE}" stroke-width="1.5"/>')

    def delay(x):
        return (x - 44) / 420 * cyc * 0.55

    def gate(x, y, lab, col, w=30):
        return f"""<g class="gate" style="animation-delay:{delay(x):.2f}s"><rect x="{x-w/2}" y="{y-12}" width="{w}" height="24" rx="5" fill="{DIE}" stroke="{col}" stroke-width="1.4"/>
<text x="{x}" y="{y+4.5}" text-anchor="middle" font-size="12.5" class="code" fill="{col}">{lab}</text></g>"""
    for q in range(nq):
        y = qy0 + q * qg
        gates += [gate(xs["H"], y, "H", TEAL), gate(xs["M1"], y, "Rx", GOLD), gate(xs["M2"], y, "Rx", GOLD), gate(xs["Z"], y, "M", HAZE, 26)]
    for key, lab in (("C1", "γ₁"), ("C2", "γ₂")):
        x = xs[key]
        gates.append(f"""<g class="gate" style="animation-delay:{delay(x):.2f}s"><rect x="{x-31}" y="{qy0-16}" width="62" height="{(nq-1)*qg+32}" rx="8" fill="#262046" stroke="{VIOLET}" stroke-width="1.4"/>
<text x="{x}" y="{qy0 + (nq-1)*qg/2 - 4}" text-anchor="middle" font-size="12.5" class="code violet">cost</text>
<text x="{x}" y="{qy0 + (nq-1)*qg/2 + 16}" text-anchor="middle" font-size="13" class="violet">{lab}</text></g>""")
    hx, hy, hb, nbar, star = 524, 276, 19.5, 16, 11
    random.seed(7)
    base = [random.uniform(0.25, 0.6) for _ in range(nbar)]
    bars = []
    for i in range(nbar):
        x = hx + i * (hb + 1.5)
        h1 = 170 * (1.0 if i == star else base[i] * 0.35)
        h0 = 48
        col, op = (VIOLET, 1) if i == star else (HAZE, .45)
        bars.append(f"""<rect x="{x}" width="{hb}" rx="3" fill="{col}" opacity="{op}">
  <animate attributeName="height" values="{h0};{h0};{h1:.1f};{h1:.1f};{h0}" keyTimes="0;.45;.7;.92;1" dur="{cyc}s" repeatCount="indefinite"/>
  <animate attributeName="y" values="{hy-h0};{hy-h0};{hy-h1:.1f};{hy-h1:.1f};{hy-h0}" keyTimes="0;.45;.7;.92;1" dur="{cyc}s" repeatCount="indefinite"/></rect>""")
    sx = hx + star * (hb + 1.5) + hb / 2
    css = f"""
.sweep{{animation:sweep {cyc}s linear infinite;}}
@keyframes sweep{{0%{{transform:translateX(0);opacity:0;}}3%{{opacity:1;}}55%{{transform:translateX(420px);opacity:1;}}58%,100%{{transform:translateX(420px);opacity:0;}}}}
.gate rect{{animation:gl {cyc}s linear infinite;animation-delay:inherit;}}
@keyframes gl{{0%{{fill:{DIE};}}3%{{fill:{ACTIVE_FILL};}}12%,100%{{fill:{DIE};}}}}
.opt{{opacity:0;animation:opt {cyc}s linear infinite;}}
@keyframes opt{{0%,66%{{opacity:0;}}72%,92%{{opacity:1;}}100%{{opacity:0;}}}}
.uni{{animation:uni {cyc}s linear infinite;}}
@keyframes uni{{0%,40%{{opacity:1;}}48%,100%{{opacity:0;}}}}
"""
    body = f"""
<text x="28" y="42" class="title">Q·Peptide: QUBO → Ising → QAOA</text>
<text x="28" y="66" class="sub">Which amino-acid substitutions best trade predicted activity against hemolysis? Qiskit Fall Fest 2026.</text>
{''.join(wires)}
{''.join(gates)}
<rect x="44" y="{qy0-26}" width="2.5" height="{(nq-1)*qg+52}" fill="{VIOLET}" class="sweep"/>
<text x="254" y="{qy0+(nq-1)*qg+42}" text-anchor="middle" font-size="12.5" class="haze">Two layers, each a cost step γ and a mixer step β</text>
<line x1="494" y1="84" x2="494" y2="{H-30}" stroke="{SCRIBE}"/>
<text x="{hx}" y="94" class="label">Measured bitstrings</text>
<line x1="{hx}" y1="{hy}" x2="{hx + nbar*(hb+1.5)}" y2="{hy}" stroke="{SCRIBE}"/>
{''.join(bars)}
<text x="{hx}" y="{hy+22}" font-size="13" class="haze uni">Uniform sampling: every answer equally likely</text>
<g class="opt"><text x="{sx}" y="{hy-180}" text-anchor="middle" font-size="13" font-weight="700" class="violet">optimum</text>
<text x="{hx}" y="{hy+22}" font-size="13" class="gold">390× more likely than uniform (N = 18, p = 2)</text></g>
<text x="{hx}" y="{H-14}" font-size="12" class="haze">Simulated annealing still wins, and the README says so</text>
"""
    write("quantum.svg", svg(W, H, body, css, "QAOA: a two-layer circuit makes the optimal bitstring 390 times more likely than uniform sampling"))


# ---------------------------------------------------------------- rucl3 crossover
def rucl3():
    W, H, cyc = 900, 320, 8.0
    ox, oy, pw, ph = 70, 262, 430, 150
    Ns = [i / 100 for i in range(101)]
    def cl(t): return 0.05 + 0.95 * t
    def qu(t): return 0.42 + 0.275 * math.log1p(6 * t) / math.log(7)
    pc = "M" + " L".join(f"{ox + t*pw:.1f} {oy - cl(t)*ph:.1f}" for t in Ns)
    pq = "M" + " L".join(f"{ox + t*pw:.1f} {oy - qu(t)*ph:.1f}" for t in Ns)
    tc = min(Ns, key=lambda t: abs(cl(t) - qu(t)))
    cx, cy = ox + tc * pw, oy - cl(tc) * ph
    css = f"""
.cl,.qu{{stroke-dasharray:700;stroke-dashoffset:700;animation:drawc {cyc}s ease-in-out infinite;}}
.qu{{animation-delay:.4s;}}
@keyframes drawc{{0%{{stroke-dashoffset:700;}}40%,90%{{stroke-dashoffset:0;opacity:1;}}100%{{stroke-dashoffset:0;opacity:0;}}}}
.star{{opacity:0;animation:star {cyc}s ease-out infinite;transform-box:fill-box;transform-origin:center;}}
@keyframes star{{0%,38%{{opacity:0;transform:scale(.3);}}44%{{opacity:1;transform:scale(1.4);}}50%,88%{{opacity:1;transform:scale(1);}}100%{{opacity:0;}}}}
.ring{{opacity:0;animation:ring {cyc}s ease-out infinite;transform-box:fill-box;transform-origin:center;}}
@keyframes ring{{0%,42%{{opacity:0;transform:scale(.5);}}46%{{opacity:.9;}}62%,100%{{opacity:0;transform:scale(3);}}}}
.li{{opacity:0;animation:li {cyc}s linear infinite;}}
@keyframes li{{0%{{opacity:0;}}8%,90%{{opacity:1;}}100%{{opacity:0;}}}}
"""
    items = [("Neutron resolution dE", "sets the accuracy both sides must reach", GOLD),
             ("Classical", "exact Lanczos/Krylov and MPS, timed", TEAL),
             ("Quantum", "Trotter circuits, fault-tolerant cost", VIOLET),
             ("Crossover N*", "where quantum becomes cheaper", INK)]
    li = []
    for i, (a, b, col) in enumerate(items):
        y = 116 + i * 42
        li.append(f'<g class="li" style="animation-delay:{0.6*i:.1f}s"><text x="566" y="{y}" font-size="14.5" font-weight="700" fill="{col}">{a}</text><text x="566" y="{y+18}" font-size="13" class="haze">{b}</text></g>')
    body = f"""
<text x="28" y="42" class="title">rucl3-crossover</text>
<text x="28" y="66" class="sub">When does a quantum computer beat classical simulation of α-RuCl₃'s neutron spectrum? In progress.</text>
<line x1="{ox}" y1="{oy}" x2="{ox+pw+10}" y2="{oy}" stroke="{HAZE}"/>
<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-ph-12}" stroke="{HAZE}"/>
<text x="{ox+pw}" y="{oy+20}" text-anchor="end" font-size="12.5" class="haze">spins N</text>
<text x="{ox+8}" y="{oy-ph-4}" font-size="12.5" class="haze">cost, log scale</text>
<path d="{pc}" fill="none" stroke="{TEAL}" stroke-width="2.5" class="cl"/>
<path d="{pq}" fill="none" stroke="{VIOLET}" stroke-width="2.5" class="qu"/>
<text x="{ox+pw-4}" y="{oy-cl(1)*ph-9}" text-anchor="end" font-size="13" class="teal">classical, about 2ᴺ</text>
<text x="{ox+pw-4}" y="{oy-qu(1)*ph+22}" text-anchor="end" font-size="13" class="violet">quantum</text>
<circle cx="{cx:.1f}" cy="{cy:.1f}" r="8" fill="none" stroke="{GOLD}" stroke-width="2" class="ring"/>
<circle cx="{cx:.1f}" cy="{cy:.1f}" r="6" fill="{GOLD}" class="star"/>
<text x="{cx:.1f}" y="{oy+20}" text-anchor="middle" font-size="13" font-weight="700" class="gold star">N*</text>
<line x1="{cx:.1f}" y1="{cy+8:.1f}" x2="{cx:.1f}" y2="{oy}" stroke="{GOLD}" stroke-dasharray="3 4" class="star"/>
<text x="{ox}" y="{H-14}" font-size="12" class="haze">Schematic. The measured curves are in the repo.</text>
{''.join(li)}
"""
    write("rucl3.svg", svg(W, H, body, css, "Schematic of the quantum-classical crossover point N* for simulating the neutron spectrum of alpha-RuCl3"))


hero(); compiler(); fastparse(); fasttime(); quantum(); rucl3()
