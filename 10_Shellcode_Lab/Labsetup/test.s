section .text
  global _start
    _start:
      ; Store the environment on stack
      push eax          ; Use 0 to terminate the string
      push "4"
      push "=123"
      push "cccc"
      mov  ebx, esp     ; Get the string address

      push eax          ; Use 0 to terminate the string
      push "5678"
      push "bbb="
      mov  ecx, esp     ; Get the string address

      push eax          ; Use 0 to terminate the string
      push "1234"
      push "aaa="
      mov  edx, esp     ; Get the string address

      ; Construct the environment array envp[]
      push eax          ; envp[3] = 0
      push ebx          ; envp[2] = "cccc=1234"
      push ecx          ; envp[1] = "bbb=5678"
      push edx          ; envp[0] = "aaa=1234"
      mov  edx, esp     ; Get the address of envp[]

      ; Store the argument string on stack
      xor  eax, eax 
      push eax          ; Use 0 to terminate the string
      push "/env"
      push "/bin"
      push "/usr"
      mov  ebx, esp     ; Get the string address

      ; Construct the argument array argv[]
      push eax          ; argv[1] = 0
      push ebx          ; argv[0] = "/usr/bin/env"
      mov  ecx, esp     ; Get the address of argv[]

      ; Invoke execve()
      xor  eax, eax     ; eax = 0x00000000
      mov   al, 0x0b    ; eax = 0x0000000b
      int 0x80
