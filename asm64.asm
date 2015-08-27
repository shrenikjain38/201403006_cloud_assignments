[bits 64]

global _start
section .text

_start:
	mov rax, 0x4
	mov ebx, 0x1
	mov ecx, message
	mov rdx, mlen
	int 0x80

	mov rax, 0x1
	mov ebx, 0x5
	int 0x80




section .data

	message: db "Hello World!"
	mlen	equ 	$-message
