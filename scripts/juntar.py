import re, sys
# Empilha dois SVG (mesma largura) num so, um em cima do outro.
def ler(p):
    s = open(p, encoding="utf-8").read()
    s = re.sub(r"<\?xml[^>]*\?>", "", s).strip()
    w = float(re.search(r'<svg[^>]*\bwidth="([\d.]+)', s).group(1))
    h = float(re.search(r'<svg[^>]*\bheight="([\d.]+)', s).group(1))
    return s, w, h
a, wa, ha = ler(sys.argv[1]); b, wb, hb = ler(sys.argv[2])
b = re.sub(r"<svg\b", f'<svg y="{ha:g}"', b, count=1)
W, H = max(wa, wb), ha + hb
open(sys.argv[3], "w", encoding="utf-8").write(
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}">{a}{b}</svg>')
print(f"{W:g}x{H:g}")
