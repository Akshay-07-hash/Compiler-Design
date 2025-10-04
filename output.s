section .text
	global _main
_main:
	push rbp
	mov rbp, rsp
	mov eax, 42
	pop rbp
	ret