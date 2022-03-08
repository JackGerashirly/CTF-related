#! /usr/bin/python2
# -*-coding: utf-8 -*-
# Written by buki
from pwn import *
import string
import time
context.log_level='debug'

sh = remote('47.98.156.31', 7887)
sh.recvuntil("XXXX+")
bs = sh.recvuntil(") == ", drop=True).strip().decode()
res = sh.recvuntil("\nGive me XXXX:", drop=True).strip().decode()

dic = string.ascii_letters + string.digits

# Pass the prove
for a in dic:
    for b in dic:
        for c in dic:
            for d in dic:
                if hashlib.sha256((a+b+c+d+bs).encode()).hexdigest() == res:
                    print("  [-] Find the prove: " + a+b+c+d)
                    sh.sendline(a+b+c+d)
                    print("  [-] Pass the prove!")
                    break


sh.recvuntil("a = ")
d = int(sh.recvuntil(",", drop=True).strip().decode())
print("d: ", d)
sh.recvuntil("1\n")

x0 = 0
y0 = 0

flag = 0
# Find the first answer
for x in range(1, 10000):
    if flag:
        break

    for y in range(1, 10000):
        if x**2 - d * y ** 2 == 1:
            print("  [-] The first answer: ", x, y)
            x0 = x
            y0 = y
            flag = 1

print("  [-] Finding finished")

next = lambda xn_1, yn_1: [x0*xn_1+d*y0*yn_1, x0*yn_1+y0*xn_1]

x, y = x0, y0
for i in range(150):

    print("  [-]", i+1)
    sh.sendline(str(x).encode())
    time.sleep(1)
    sh.sendline(str(y).encode())
    time.sleep(1)
    x, y = next(x, y)
    if x**2-d*y**2 != 1:
    	print("  [-] Something wrong!")
    	break


print("  [-]  Finish")
flag = sh.recv(100).strip().decode()

print("  [-] flag: " + flag)
sh.interactive()
