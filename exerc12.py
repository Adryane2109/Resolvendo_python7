#!/usr/bin/env python3
import re
padrao = r"(S[0-9]{2}): pH ?= ?(\d[,.]?\d?);$"
lista = []

with open ("file.txt", 'r') as fh:
	for line in fh:
		line = line.rstrip()
		res = re.search(padrao, line)
		if res:
			l = [res.group(1), res.group(2)]
			lista.append(l)
print(lista)
