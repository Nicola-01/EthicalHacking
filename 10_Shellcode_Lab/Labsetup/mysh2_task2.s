section .text
	global _start
		_start:
			BITS 32
			jmp short two
		one:
			pop ebx
			xor eax, eax

			mov [ebx+12], al ; replacing * with 0x00
			mov [ebx+17], al ; replacing * with 0x00
			mov [ebx+22], al ; replacing * with 0x00
			mov [ebx+23], al ; replacing * with 0x00
			; '/usr/bin/env*a=11*b=12**AAAABBBBCCCCDDDDEEEE'

			mov [ebx+24], ebx ; replacing AAAA with ebx
			lea ecx, [ebx+24] ; ecx has to point to argv[]
			mov [ebx+28], eax ; saving 0x00 into BBBB

			mov [ebx+40], eax ; saving 0x00 into EEEE
			; '/usr/bin/env*a=11*b=12**~~~~****CCCCDDDD****'  * -> 0x00, ~ -> address

			lea edx, [ebx+13] ; loading the address of "a=11" into edx
			mov [ebx+32], edx ; saving the address of "a=11" into CCCC

			lea edx, [ebx+18] ; loading the address of "b=12" into edx
			mov [ebx+36], edx ; saving the address of "b=12" into DDDD
			
			lea edx, [ebx+32] ; edx has to point to env[]; -> old CCCC

		mov al, 0x0b
			int 0x80
		two:
			call one
			db '/usr/bin/env*a=11*b=12**AAAABBBBCCCCDDDDEEEE'