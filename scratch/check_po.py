import re

po_path = r"f:\Git\JoeyStickDev.github.io\Temp\Game.po"
with open(po_path, 'r', encoding='utf-8') as f:
    po_text = f.read(10000)

print(po_text[:2000])
