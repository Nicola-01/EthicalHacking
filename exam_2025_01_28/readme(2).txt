Why it is mandatory to avoid zeros in the attack binary?
0x00 is the string terminator in c, so if we pass a shellcode that contain the byte 0x00, when the vitim find that value it will stop te reading and the rest of the shell will not copy to the memory
