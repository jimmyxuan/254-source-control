#!/usr/bin/env python3
from sys import argv

fh = open(argv[1],'r')
lines = list(fh)
fh.close()

for l in lines:
	print(l, ends='')
