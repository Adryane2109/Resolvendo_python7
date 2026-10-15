#!/usr/bin/env python3
import re
identificadores = [
    "EXP2026_B03_P12", "EXP2026_B3_P12", "EXP2026_B03_P2", "exp2026_B03_P12", "EXP2026_B03_P12_extra"
]
padrao = r"^EXP\d{4}_B\d{2}_P\d{2}$"
for valor in identificadores:
	if re.fullmatch(padrao, valor):
		print(f"{valor:<25} -> valido")
	else:
		print(f"{valor:<25}-> invalido")
