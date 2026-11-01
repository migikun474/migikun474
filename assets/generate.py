"""Generate the animated SVGs for the migikun474 profile README.

Everything is self-contained SVG (CSS keyframes + SMIL), no scripts, no
external fonts or images, so GitHub renders and animates it inside <img>.
Usage: python3 gen.py OUT_DIR
"""
import math, os, sys

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

BG, PANEL, EDGE = "#141321", "#1c1a30", "#2e2b4a"
PINK, CYAN, YEL, MUTED, TEXT, RED = "#fe428e", "#a9fef7", "#f8d847", "#8d8aae", "#e8e6f5", "#ff6b6b"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
SANS = "'Segoe UI',Ubuntu,'Helvetica Neue',Arial,sans-serif"

BASE_CSS = f"""
text{{font-family:{MONO};}}
.t{{fill:{TEXT};}} .m{{fill:{MUTED};}} .p{{fill:{PINK};}} .c{{fill:{CYAN};}} .y{{fill:{YEL};}}
.title{{font-family:{SANS};font-weight:700;font-size:17px;fill:{PINK};}}
.sub{{font-size:12px;fill:{MUTED};}}
@media (prefers-reduced-motion: reduce){{*{{animation:none!important;}}}}
"""


def svg(w, h, body, css="", label=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">
<title>{label}</title>
<style>{BASE_CSS}{css}</style>
<defs>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="softglow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
  <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="{EDGE}" stroke-width="0.6" opacity="0.55"/></pattern>
</defs>
<rect width="{w}" height="{h}" rx="16" fill="{BG}"/>
<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="16" fill="none" stroke="{EDGE}"/>
{body}
</svg>"""


def write(name, content):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(content)
    print(f"{name}: {len(content)/1024:.1f} KB")


# ---------------------------------------------------------------- hero
def hero():
    W, H = 900, 250
    lines = [
        "compilers · C-like source → TAC → MIPS",
        "low-latency C · SWAR · SSE/AVX2 · rdtsc",
        "quantum · QAOA · Trotter · Quantum++",
        "open source · Eigen · Quantum++",
    ]
    cyc, step = 16, 4  # 4 lines, 4 s each
    x0, y0, cw = 235, 150, 11.4
    sub = []
    for i, s in enumerate(lines):
        w = len(s) * cw + 4
        kt = "0;0.11;0.22;0.245;1"
        sub.append(f"""
  <clipPath id="cl{i}"><rect x="{x0}" y="{y0-18}" height="26" width="0">
    <animate attributeName="width" values="0;{w:.0f};{w:.0f};0;0" keyTimes="{kt}" dur="{cyc}s" begin="{i*step}s" repeatCount="indefinite"/></rect></clipPath>
  <text x="{x0}" y="{y0}" font-size="19" class="c" clip-path="url(#cl{i})">{s}</text>
  <rect y="{y0-16}" width="10" height="20" fill="{PINK}" opacity="0">
    <animate attributeName="x" values="{x0};{x0+w:.0f};{x0+w:.0f};{x0};{x0}" keyTimes="{kt}" dur="{cyc}s" begin="{i*step}s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;1;1;0;0" keyTimes="{kt}" dur="{cyc}s" begin="{i*step}s" repeatCount="indefinite" calcMode="discrete"/>
  </rect>""")
    # drifting glyphs
    glyphs = ["0x7f", "|ψ⟩", "mov", "SIMD", "LALR(1)", "rdtsc", "⊗", "λ", "AVX2", "t1 = a+b", "H", "β,γ", "1010", "$sp", "Σ", "O(2ᴺ)"]
    drift = []
    for i, g in enumerate(glyphs):
        x = 30 + (i * 157) % 840
        d = 9 + (i * 7) % 8
        delay = -(i * 1.7) % d
        drift.append(f'<text x="{x}" y="{H-20}" font-size="{11 + (i % 3) * 2}" class="drift" style="animation-duration:{d}s;animation-delay:{delay:.1f}s" fill="{[PINK, CYAN, YEL, MUTED][i % 4]}">{g}</text>')
    # scrolling clock + sine trace, period 90 px
    per, yb = 90, 222
    sq, sn = [], []
    for k in range(0, 2 * W // per + 2):
        x = k * per
        sq.append(f"M{x} {yb} H{x+20} V{yb-12} H{x+65} V{yb} H{x+per}")
    sine = f"M0 {yb-6}" + " ".join(f"L{x} {yb-6 + 7*math.sin(2*math.pi*x/per):.1f}" for x in range(0, 2 * W + per, 3))
    css = f"""
.name{{font-family:{SANS};font-weight:800;font-size:44px;letter-spacing:3px;fill:transparent;stroke:{PINK};stroke-width:1.2;
  stroke-dasharray:900;stroke-dashoffset:900;animation:draw 3.2s ease-out forwards, fillin 1.2s 2.6s forwards, pulse 4s 4s ease-in-out infinite;}}
@keyframes draw{{to{{stroke-dashoffset:0;}}}}
@keyframes fillin{{to{{fill:{PINK};}}}}
@keyframes pulse{{0%,100%{{filter:none;}}50%{{filter:url(#glow);}}}}
.drift{{opacity:0;animation-name:rise;animation-timing-function:linear;animation-iteration-count:infinite;}}
@keyframes rise{{0%{{transform:translateY(0);opacity:0;}}15%{{opacity:.45;}}80%{{opacity:.25;}}100%{{transform:translateY(-200px);opacity:0;}}}}
.scan{{animation:scan 6s linear infinite;}}
@keyframes scan{{from{{transform:translateY(-40px);}}to{{transform:translateY({H}px);}}}}
.wave{{animation:slide 4s linear infinite;}}
@keyframes slide{{from{{transform:translateX(0);}}to{{transform:translateX(-{per*5}px);}}}}
.dot{{animation:blink 1.6s ease-in-out infinite;}}
@keyframes blink{{50%{{opacity:.2;}}}}
.prompt{{animation:blink 1s steps(1) infinite;}}
"""
    body = f"""
<clipPath id="card"><rect width="{W}" height="{H}" rx="16"/></clipPath>
<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" fill="url(#grid)"/>
  <linearGradient id="sg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{PINK}" stop-opacity="0"/><stop offset="1" stop-color="{PINK}" stop-opacity=".10"/></linearGradient>
  <rect class="scan" width="{W}" height="40" fill="url(#sg)"/>
  {''.join(drift)}
  <g class="wave" opacity=".7">
    <path d="{' '.join(sq)}" fill="none" stroke="{CYAN}" stroke-width="1.4" opacity=".6"/>
    <path d="{sine}" fill="none" stroke="{PINK}" stroke-width="1.6"/>
  </g>
</g>
<circle cx="34" cy="32" r="5" fill="{CYAN}" class="dot"/>
<text x="48" y="37" font-size="13" class="m">IIT Roorkee · systems · compilers · quantum</text>
<text x="{W-30}" y="37" font-size="13" class="m" text-anchor="end">github.com/migikun474</text>
<text x="{W/2}" y="104" text-anchor="middle" class="name">SAI VIGNESH</text>
<text x="{x0-28}" y="{y0}" font-size="19" class="p prompt">$</text>
{''.join(sub)}
"""
    write("hero.svg", svg(W, H, body, css, "Amirishetty Sai Vignesh — systems, compilers, low-latency C and quantum computing"))


# ---------------------------------------------------------------- compiler
def compiler():
    W, H, cyc = 900, 340, 11.0
    top = [("source.c", "x = a + b * 2;"), ("preprocess", "#define, #include"), ("lexer · Flex", "ID = ID + ID * NUM"),
           ("parser · LALR(1)", "= x (+ a (* b 2))"), ("semantic", "types ✓ scopes ✓")]
    bot = [("TAC", "t1 = b * 2"), ("optimizer", "-O1 · -O2 · -O3"), ("MIPS · regalloc", "sll $t0, $a1, 1"), ("SPIM", "output == gcc ✓")]
    bw, bh, gap, ty, by = 152, 58, 19, 92, 222
    boxes = []
    for i, (a, b) in enumerate(top):
        boxes.append((22 + i * (bw + gap), ty, a, b))
    bw2, gap2 = 190, 26
    for i, (a, b) in enumerate(bot):  # right to left
        x = 22 + (3 - i) * (bw2 + gap2)
        boxes.append((x, by, a, b, bw2))
    centers = []
    rects = []
    n = len(boxes)
    travel = 0.82
    for i, bx in enumerate(boxes):
        x, y, a, b = bx[:4]
        w = bx[4] if len(bx) > 4 else bw
        cx, cy = x + w / 2, y + bh / 2
        centers.append((cx, cy))
        t = i / (n - 1) * travel * cyc
        rects.append(f"""
  <g class="stage" style="animation-delay:{t-0.25:.2f}s">
    <rect x="{x}" y="{y}" width="{w}" height="{bh}" rx="10" fill="{PANEL}" stroke="{EDGE}" stroke-width="1.5" class="box"/>
    <text x="{cx}" y="{y+23}" text-anchor="middle" font-size="13" font-weight="700" class="t lbl">{a}</text>
    <text x="{cx}" y="{y+43}" text-anchor="middle" font-size="11.5" class="m art">{b}</text>
  </g>""")
    # path through centers
    pts = centers
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    seg = [math.dist(pts[i], pts[i + 1]) for i in range(n - 1)]
    L = sum(seg)
    acc = [0.0]
    for s in seg:
        acc.append(acc[-1] + s)
    kp = ";".join(f"{a/L:.4f}" for a in acc) + ";1"
    kt = ";".join(f"{i/(n-1)*travel:.4f}" for i in range(n)) + ";1"
    packets = []
    for j, (r, op, lag) in enumerate([(7, 1, 0), (5, .55, .12), (3.5, .3, .24)]):
        packets.append(f"""<circle r="{r}" fill="{PINK}" opacity="{op}" filter="url(#glow)">
    <animateMotion dur="{cyc}s" begin="{lag}s" repeatCount="indefinite" path="{d}" keyPoints="{kp}" keyTimes="{kt}" calcMode="linear"/></circle>""")
    stage_css = f"""
.stage .box{{animation:hl {cyc}s linear infinite;animation-delay:inherit;}}
.stage .lbl{{animation:hlt {cyc}s linear infinite;animation-delay:inherit;}}
.stage .art{{animation:hla {cyc}s linear infinite;animation-delay:inherit;}}
@keyframes hl{{0%{{stroke:{EDGE};}}2%{{stroke:{PINK};fill:#2a1730;}}9%{{stroke:{PINK};fill:#2a1730;}}16%{{stroke:{EDGE};fill:{PANEL};}}100%{{stroke:{EDGE};}}}}
@keyframes hlt{{0%{{fill:{TEXT};}}2%,9%{{fill:{PINK};}}16%,100%{{fill:{TEXT};}}}}
@keyframes hla{{0%{{fill:{MUTED};}}2%,9%{{fill:{CYAN};}}16%,100%{{fill:{MUTED};}}}}
.flow{{stroke-dasharray:6 8;animation:dash 1.2s linear infinite;}}
@keyframes dash{{to{{stroke-dashoffset:-28;}}}}
.ok{{opacity:0;animation:ok {cyc}s linear infinite;}}
@keyframes ok{{0%,80%{{opacity:0;transform:translateY(6px);}}84%,96%{{opacity:1;transform:translateY(0);}}100%{{opacity:0;}}}}
"""
    body = f"""
<text x="22" y="38" class="title">COMPILER-DESIGN</text>
<text x="22" y="60" class="sub">a C-like language with classes, references and overloading — compiled all the way to MIPS · C++17 · Flex · Bison</text>
<text x="{W-22}" y="38" text-anchor="end" font-size="12" class="y">front end ✓  TAC ✓  -O3 ✓  MIPS ✓</text>
<text x="22" y="{ty-10}" font-size="10.5" class="m" letter-spacing="2">FRONT END</text>
<text x="22" y="{by-10}" font-size="10.5" class="m" letter-spacing="2">BACK END</text>
<path d="{d}" fill="none" stroke="{EDGE}" stroke-width="2"/>
<path d="{d}" fill="none" stroke="{PINK}" stroke-width="2" opacity=".55" class="flow"/>
{''.join(packets)}
{''.join(rects)}
<g class="ok"><rect x="22" y="{H-40}" width="420" height="26" rx="13" fill="#123a35" stroke="{CYAN}"/>
<text x="232" y="{H-22}" text-anchor="middle" font-size="12" class="c">✓ every test prints exactly what gcc's binary prints</text></g>
<text x="{W-22}" y="{H-22}" text-anchor="end" font-size="11" class="m">87 semantic · 34 TAC · 33 SPIM checks passing</text>
"""
    write("compiler.svg", svg(W, H, body, stage_css, "Compiler pipeline animation: source.c through lexer, LALR(1) parser, semantic analysis, TAC, optimizer and MIPS on SPIM"))


# ---------------------------------------------------------------- fastparse
def fastparse():
    W, H, cyc = 900, 310, 9.0
    digits = "12345678"
    rows = [[d for d in digits], ["12", "34", "56", "78"], ["1234", "5678"], ["12345678"]]
    ops = ["- '0'", "×10 +", "×100 +", "×10⁴ +"]
    left, top, rowh, span = 30, 92, 46, 360
    parts = []
    for r, cells in enumerate(rows):
        k = len(cells)
        cw = span / k
        appear = 0.4 + r * 1.3
        for i, c in enumerate(cells):
            x = left + i * cw
            parts.append(f"""<g class="cell" style="animation-delay:{appear + i*0.05:.2f}s">
  <rect x="{x+3:.1f}" y="{top + r*rowh}" width="{cw-6:.1f}" height="32" rx="7" fill="{PANEL}" stroke="{[MUTED, CYAN, CYAN, PINK][r]}" stroke-width="1.3"/>
  <text x="{x + cw/2:.1f}" y="{top + r*rowh + 21}" text-anchor="middle" font-size="{15 if r < 3 else 17}" class="{['t','c','c','p'][r]}" font-weight="700">{c}</text></g>""")
        parts.append(f'<text x="{left+span+16}" y="{top + r*rowh + 21}" font-size="12" class="m cell" style="animation-delay:{appear:.2f}s">{ops[r]}</text>')
    # bars
    bx, by0, bwmax = 480, 118, 330
    bars = [("reference parser", 973, MUTED), ("AVX2 · gcc", 4071, CYAN), ("AVX2 · clang", 5311, PINK)]
    vmax = 5311
    bar_svg = []
    for i, (lab, v, col) in enumerate(bars):
        y = by0 + i * 52
        w = bwmax * v / vmax
        bar_svg.append(f"""
<text x="{bx}" y="{y-8}" font-size="12" class="t">{lab}</text>
<rect x="{bx}" y="{y}" width="{bwmax}" height="16" rx="8" fill="{PANEL}"/>
<rect x="{bx}" y="{y}" width="{w:.1f}" height="16" rx="8" fill="{col}" class="bar" style="animation-delay:{0.3 + i*0.45:.2f}s"/>
<text x="{bx + w - 6 if w > 120 else bx + w + 8:.1f}" y="{y+12.5}" font-size="11.5" font-weight="700" text-anchor="{'end' if w > 120 else 'start'}" fill="{BG if w > 120 else TEXT}" class="val" style="animation-delay:{1.6 + i*0.45:.2f}s">{v:,} MB/s</text>""")
    css = f"""
.cell{{opacity:0;animation:pop {cyc}s ease-out infinite;}}
@keyframes pop{{0%{{opacity:0;transform:translateY(-10px);}}6%{{opacity:1;transform:translateY(0);}}88%{{opacity:1;}}96%,100%{{opacity:0;}}}}
.bar{{transform-box:fill-box;transform-origin:left;transform:scaleX(0);animation:grow {cyc}s cubic-bezier(.2,.8,.2,1) infinite;}}
@keyframes grow{{0%{{transform:scaleX(0);}}22%{{transform:scaleX(1);}}88%{{transform:scaleX(1);}}96%,100%{{transform:scaleX(0);}}}}
.val{{opacity:0;animation:fade {cyc}s linear infinite;}}
@keyframes fade{{0%{{opacity:0;}}6%{{opacity:1;}}70%{{opacity:1;}}78%,100%{{opacity:0;}}}}
.x{{animation:pulse2 2s ease-in-out infinite;}}
@keyframes pulse2{{50%{{opacity:.45;}}}}
"""
    body = f"""
<text x="30" y="38" class="title">fastparse</text>
<text x="30" y="60" class="sub">market-data text → fixed-point integers · naive loop → SWAR → x86-64 asm → SSE → AVX2</text>
<text x="30" y="84" font-size="11" class="m" letter-spacing="1.5">SWAR: 8 DIGITS IN 3 MULTIPLY-ADDS, NOT 8 LOOP STEPS</text>
{''.join(parts)}
<line x1="452" y1="80" x2="452" y2="{H-30}" stroke="{EDGE}"/>
<text x="{bx}" y="84" font-size="11" class="m" letter-spacing="1.5">BINANCE BTCUSDT PRICE COLUMN · 3.56M ROWS</text>
{''.join(bar_svg)}
<text x="{bx}" y="{H-26}" font-size="12" class="y x">5.5× the reference · checked against it on every PR</text>
"""
    write("fastparse.svg", svg(W, H, body, css, "fastparse animation: SWAR digit combining and AVX2 throughput up to 5,311 MB/s against a 973 MB/s reference"))


# ---------------------------------------------------------------- fasttime
def fasttime():
    W, H = 900, 300
    lanes = [("ft_now_ns() · rdtsc", 16, None, PINK), ("clock_gettime · tsc (vDSO)", 20, None, CYAN),
             ("clock_gettime · hpet", 1213, 4.0, YEL), ("clock_gettime · acpi_pm", 1966, 6.5, RED)]
    x0, x1, kx, y0, gap = 300, 820, 560, 116, 42
    out = []
    for i, (lab, ns, hold, col) in enumerate(lanes):
        y = y0 + i * gap
        out.append(f'<text x="30" y="{y+4}" font-size="12.5" class="t">{lab}</text>')
        out.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{EDGE}" stroke-width="2" stroke-linecap="round"/>')
        out.append(f'<text x="{x1+12}" y="{y+4}" font-size="12.5" font-weight="700" fill="{col}">{ns:,} ns</text>')
        if hold is None:
            dur = 1.2 * ns / 16
            for lag in (0, dur / 3, 2 * dur / 3):
                out.append(f"""<circle cy="{y}" r="4.5" fill="{col}" filter="url(#glow)"><animate attributeName="cx" values="{x0};{x1}" dur="{dur:.2f}s" begin="{lag:.2f}s" repeatCount="indefinite"/></circle>""")
        else:
            go = 0.6
            dur = 2 * go + hold
            k1, k2 = go / dur, (go + hold) / dur
            out.append(f"""<g><rect x="{kx-34}" y="{y-11}" width="68" height="22" rx="6" fill="#2b1420" stroke="{RED}" stroke-width="1">
  <animate attributeName="stroke-opacity" values="1;.35;1" dur="1s" repeatCount="indefinite"/></rect>
  <text x="{kx}" y="{y-15}" text-anchor="middle" font-size="10" fill="{RED}">syscall → kernel</text></g>""")
            out.append(f"""<circle cy="{y}" r="4.5" fill="{col}" filter="url(#glow)">
  <animate attributeName="cx" values="{x0};{kx};{kx};{x1}" keyTimes="0;{k1:.3f};{k2:.3f};1" dur="{dur:.2f}s" repeatCount="indefinite"/></circle>""")
    css = ""
    body = f"""
<text x="30" y="38" class="title">fasttime</text>
<text x="30" y="60" class="sub">is your Linux clock read secretly a system call? · p50 cost per read, bare-metal laptop</text>
<text x="{x0}" y="88" font-size="10.5" class="m" letter-spacing="1.5">EACH DOT IS ONE CLOCK READ</text>
{''.join(out)}
<text x="30" y="{H-22}" font-size="11" class="m">fast lanes run at true relative speed; the kernel waits are compressed ~18× so the dots still move</text>
"""
    write("fasttime.svg", svg(W, H, body, css, "fasttime animation: rdtsc and vDSO clock reads at 16-20 ns against hpet and acpi_pm reads that trap into the kernel"))


# ---------------------------------------------------------------- quantum (Q-peptide)
def quantum():
    W, H, cyc = 900, 320, 6.0
    nq, qy0, qg = 5, 100, 38
    xs = {"H": 70, "C1": 140, "M1": 225, "C2": 290, "M2": 375, "Z": 430}
    wires, gates = [], []
    for q in range(nq):
        y = qy0 + q * qg
        wires.append(f'<text x="28" y="{y+4}" font-size="12" class="m">q{q}</text><line x1="50" y1="{y}" x2="455" y2="{y}" stroke="{EDGE}" stroke-width="1.5"/>')

    def gate(x, y, lab, col, w=30):
        t = (x - 40) / 430 * cyc * 0.55
        return f"""<g class="gate" style="animation-delay:{t:.2f}s"><rect x="{x-w/2}" y="{y-12}" width="{w}" height="24" rx="5" fill="{PANEL}" stroke="{col}" stroke-width="1.4"/>
<text x="{x}" y="{y+4.5}" text-anchor="middle" font-size="12" fill="{col}">{lab}</text></g>"""
    for q in range(nq):
        y = qy0 + q * qg
        gates.append(gate(xs["H"], y, "H", CYAN))
        gates.append(gate(xs["M1"], y, "Rx", YEL))
        gates.append(gate(xs["M2"], y, "Rx", YEL))
        gates.append(gate(xs["Z"], y, "◩", MUTED, 26))
    for key, lab in (("C1", "γ₁"), ("C2", "γ₂")):
        x = xs[key]
        t = (x - 40) / 430 * cyc * 0.55
        gates.append(f"""<g class="gate" style="animation-delay:{t:.2f}s"><rect x="{x-31}" y="{qy0-16}" width="62" height="{(nq-1)*qg+32}" rx="8" fill="#241a35" stroke="{PINK}" stroke-width="1.4"/>
<text x="{x}" y="{qy0 + (nq-1)*qg/2 - 6}" text-anchor="middle" font-size="12" fill="{PINK}">e^-iγC</text>
<text x="{x}" y="{qy0 + (nq-1)*qg/2 + 14}" text-anchor="middle" font-size="12" class="p">{lab}</text></g>""")
    # histogram
    hx, hy, hb, nbar = 520, 268, 19.5, 16
    import random
    random.seed(7)
    base = [random.uniform(0.25, 0.6) for _ in range(nbar)]
    star = 11
    bars = []
    for i in range(nbar):
        x = hx + i * (hb + 1.5)
        final = 1.0 if i == star else base[i] * 0.35
        col = PINK if i == star else MUTED
        h0, h1 = 48, 170 * final
        bars.append(f"""<rect x="{x}" width="{hb}" rx="3" fill="{col}" opacity="{1 if i == star else .55}">
  <animate attributeName="height" values="{h0};{h0};{h1:.1f};{h1:.1f};{h0}" keyTimes="0;.45;.7;.92;1" dur="{cyc}s" repeatCount="indefinite"/>
  <animate attributeName="y" values="{hy-h0};{hy-h0};{hy-h1:.1f};{hy-h1:.1f};{hy-h0}" keyTimes="0;.45;.7;.92;1" dur="{cyc}s" repeatCount="indefinite"/></rect>""")
    sx = hx + star * (hb + 1.5) + hb / 2
    css = f"""
.sweep{{animation:sweep {cyc}s linear infinite;}}
@keyframes sweep{{0%{{transform:translateX(0);opacity:0;}}3%{{opacity:1;}}55%{{transform:translateX(420px);opacity:1;}}58%,100%{{transform:translateX(420px);opacity:0;}}}}
.gate{{animation:gl {cyc}s linear infinite;}}
@keyframes gl{{0%{{filter:none;}}3%{{filter:url(#glow);}}12%,100%{{filter:none;}}}}
.opt{{opacity:0;animation:opt {cyc}s linear infinite;}}
@keyframes opt{{0%,66%{{opacity:0;}}72%,92%{{opacity:1;}}100%{{opacity:0;}}}}
.uni{{animation:uni {cyc}s linear infinite;}}
@keyframes uni{{0%,40%{{opacity:1;}}48%,100%{{opacity:0;}}}}
"""
    body = f"""
<text x="28" y="38" class="title">Q·Peptide — QUBO → Ising → QAOA</text>
<text x="28" y="60" class="sub">which amino-acid substitutions best trade predicted activity against hemolysis? · Qiskit Fall Fest 2026</text>
{''.join(wires)}
{''.join(gates)}
<rect x="44" y="{qy0-24}" width="3" height="{(nq-1)*qg+48}" fill="{PINK}" class="sweep" filter="url(#glow)"/>
<text x="250" y="{qy0+(nq-1)*qg+40}" text-anchor="middle" font-size="11" class="m">p = 2 layers · cost γ · mixer β</text>
<line x1="490" y1="80" x2="490" y2="{H-30}" stroke="{EDGE}"/>
<text x="{hx}" y="88" font-size="11" class="m" letter-spacing="1.5">MEASURED BITSTRINGS</text>
<line x1="{hx}" y1="{hy}" x2="{hx + nbar*(hb+1.5)}" y2="{hy}" stroke="{EDGE}"/>
{''.join(bars)}
<text x="{hx}" y="{hy+20}" font-size="11" class="m uni">uniform sampling: every answer equally likely</text>
<g class="opt"><text x="{sx}" y="{hy-180}" text-anchor="middle" font-size="12" font-weight="700" class="p">optimum</text>
<text x="{hx}" y="{hy+20}" font-size="12" class="y">390× more likely than uniform  (N = 18, p = 2)</text></g>
<text x="{hx}" y="{H-14}" font-size="10.5" class="m">simulated annealing still wins — the README says so</text>
"""
    write("quantum.svg", svg(W, H, body, css, "QAOA animation: a p=2 circuit sweeps and the optimal bitstring grows to 390 times its uniform probability"))


# ---------------------------------------------------------------- rucl3 crossover
def rucl3():
    W, H, cyc = 900, 318, 8.0
    ox, oy, pw, ph = 70, 262, 430, 150
    # schematic: log cost vs N. classical ~ a + bN (exponential), quantum ~ c + d log N (polynomial)
    Ns = [i / 100 for i in range(0, 101)]
    def cl(t): return 0.05 + 0.95 * t
    def qu(t): return 0.42 + 0.22 * math.log1p(6 * t) / math.log(7) * 1.25
    pc = "M" + " L".join(f"{ox + t*pw:.1f} {oy - cl(t)*ph:.1f}" for t in Ns)
    pq = "M" + " L".join(f"{ox + t*pw:.1f} {oy - qu(t)*ph:.1f}" for t in Ns)
    # crossing
    tc = min(Ns, key=lambda t: abs(cl(t) - qu(t)))
    cx, cy = ox + tc * pw, oy - cl(tc) * ph
    css = f"""
.cl,.qu{{stroke-dasharray:700;stroke-dashoffset:700;animation:drawc {cyc}s ease-in-out infinite;}}
.qu{{animation-delay:.4s;}}
@keyframes drawc{{0%{{stroke-dashoffset:700;}}40%{{stroke-dashoffset:0;}}90%{{stroke-dashoffset:0;opacity:1;}}100%{{stroke-dashoffset:0;opacity:0;}}}}
.star{{opacity:0;animation:star {cyc}s ease-out infinite;transform-box:fill-box;transform-origin:center;}}
@keyframes star{{0%,38%{{opacity:0;transform:scale(.3);}}44%{{opacity:1;transform:scale(1.4);}}50%,88%{{opacity:1;transform:scale(1);}}100%{{opacity:0;}}}}
.ring{{opacity:0;animation:ring {cyc}s ease-out infinite;transform-box:fill-box;transform-origin:center;}}
@keyframes ring{{0%,42%{{opacity:0;transform:scale(.5);}}46%{{opacity:.9;}}62%{{opacity:0;transform:scale(3);}}100%{{opacity:0;}}}}
.li{{opacity:0;animation:li {cyc}s linear infinite;}}
@keyframes li{{0%{{opacity:0;}}8%,90%{{opacity:1;}}100%{{opacity:0;}}}}
"""
    items = [("neutron resolution dE", "fixes the accuracy both sides must hit"),
             ("classical", "exact Lanczos/Krylov + MPS baselines, timed"),
             ("quantum", "Trotter + Hadamard tests → fault-tolerant cost"),
             ("crossover N*", "where the quantum cost dips below")]
    li = []
    for i, (a, b) in enumerate(items):
        y = 112 + i * 40
        col = [YEL, CYAN, PINK, TEXT][i]
        li.append(f'<g class="li" style="animation-delay:{0.6*i:.1f}s"><text x="560" y="{y}" font-size="13" font-weight="700" fill="{col}">{a}</text><text x="560" y="{y+17}" font-size="11.5" class="m">{b}</text></g>')
    body = f"""
<text x="28" y="38" class="title">rucl3-crossover</text>
<text x="28" y="60" class="sub">when does a quantum computer beat classical simulation of α-RuCl₃'s neutron spectrum? · in progress</text>
<line x1="{ox}" y1="{oy}" x2="{ox+pw+10}" y2="{oy}" stroke="{MUTED}"/>
<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-ph-12}" stroke="{MUTED}"/>
<text x="{ox+pw}" y="{oy+18}" text-anchor="end" font-size="11" class="m">spins N →</text>
<text x="{ox+8}" y="{oy-ph-4}" font-size="11" class="m">cost (log)</text>
<path d="{pc}" fill="none" stroke="{CYAN}" stroke-width="2.4" class="cl"/>
<path d="{pq}" fill="none" stroke="{PINK}" stroke-width="2.4" class="qu"/>
<text x="{ox+pw-4}" y="{oy-cl(1)*ph-8}" text-anchor="end" font-size="11.5" class="c">classical ~ 2ᴺ</text>
<text x="{ox+pw-4}" y="{oy-qu(1)*ph+20}" text-anchor="end" font-size="11.5" class="p">quantum</text>
<circle cx="{cx:.1f}" cy="{cy:.1f}" r="8" fill="none" stroke="{YEL}" stroke-width="2" class="ring"/>
<g class="star"><circle cx="{cx:.1f}" cy="{cy:.1f}" r="5.5" fill="{YEL}" filter="url(#glow)"/></g>
<text x="{cx:.1f}" y="{oy+18}" text-anchor="middle" font-size="12" font-weight="700" class="y star">N*</text>
<line x1="{cx:.1f}" y1="{cy+8:.1f}" x2="{cx:.1f}" y2="{oy}" stroke="{YEL}" stroke-dasharray="3 4" class="star"/>
<text x="{ox}" y="{H-12}" font-size="10.5" class="m">schematic — the measured curves are in the repo</text>
{''.join(li)}
"""
    write("rucl3.svg", svg(W, H, body, css, "Schematic animation of the quantum-classical crossover point N* for simulating the neutron spectrum of alpha-RuCl3"))


hero(); compiler(); fastparse(); fasttime(); quantum(); rucl3()
