import re, sys
# Empilha dois SVG num so, um em cima do outro, ajustando os dois para a mesma largura (LARGURA).
# Cada servidor de stats gera uma largura diferente; escalar aqui evita card desalinhado.
LARGURA = 467.0
def ler(p):
    s = re.sub(r"<\?xml[^>]*\?>", "", open(p, encoding="utf-8").read()).strip()
    w = float(re.search(r'<svg[^>]*?\bwidth="([\d.]+)', s).group(1))
    h = float(re.search(r'<svg[^>]*?\bheight="([\d.]+)', s).group(1))
    if not re.search(r'<svg[^>]*?\bviewBox=', s):
        s = re.sub(r"<svg\b", f'<svg viewBox="0 0 {w:g} {h:g}"', s, count=1)
    h2 = h * LARGURA / w
    abre = re.search(r"<svg\b[^>]*>", s).group(0)
    nova = re.sub(r'\bwidth="[\d.]+"', f'width="{LARGURA:g}"', abre, count=1)
    nova = re.sub(r'\bheight="[\d.]+"', f'height="{h2:g}"', nova, count=1)
    return s.replace(abre, nova, 1), h2
a, ha = ler(sys.argv[1]); b, hb = ler(sys.argv[2])
b = re.sub(r"<svg\b", f'<svg y="{ha:g}"', b, count=1)
H = ha + hb
open(sys.argv[3], "w", encoding="utf-8").write(
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{LARGURA:g}" height="{H:g}" viewBox="0 0 {LARGURA:g} {H:g}">{a}{b}</svg>')
print(f"{LARGURA:g}x{H:g}")
