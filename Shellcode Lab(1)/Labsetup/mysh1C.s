section .text
  global _start
    _start:
      ; Store the argument string on stack
      xor  eax, eax 
      
      push eax
      mov edx, "la##"; [# # a l]
      shl edx, 16
      shr edx, 16
      push edx
      push "ls -"
      mov edx, esp 
      
      push eax
      mov ecx, "-c##"  ; [# # c -]
      shl ecx, 16
      shr ecx, 16
      push ecx
      mov ecx, esp 
         
      push eax
      push "//sh"
      push "/bin"
      mov  ebx, esp     ; Get the string address
      
      ; Construct the argument array argv[]
      push eax          ; argv[3] = 
      push edx          ; argv[2] = 
      push ecx          ; argv[1] = 
      push ebx          ; argv[0] points "/bin//sh"
      mov  ecx, esp     ; Get the address of argv[]
   
      ; For environment variable 
      xor  edx, edx     ; No env variables 

      ; Invoke execve()
      xor  eax, eax     ; eax = 0x00000000
      mov   al, 0x0b    ; eax = 0x0000000b
      int 0x80
