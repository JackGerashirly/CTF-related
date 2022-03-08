#! /usr/bin/python2
# -*-coding: utf-8 -*-
# Written by buki
from pwn import *
import string
import time
#context.log_level='debug'

sh = remote('183.129.189.61', 53800)
sh.recvuntil("XXXX+")
bs = sh.recvuntil(") == ", drop=True).strip().decode()
res = sh.recvuntil("\nGive me XXXX:", drop=True).strip().decode()
dic = string.ascii_letters + string.digits

# pass the prove
for a in dic:
    for b in dic:
        for c in dic:
            for d in dic:
                if hashlib.sha256((a+b+c+d+bs).encode()).hexdigest() == res:
                    print("  [-] Find the prove: " + a+b+c+d)
                    sh.sendline(a+b+c+d)
                    print("  [-] Pass the prove!")
                    break
sh.interactive()
"""
for x in range(1,17):
    for y in range(0,256):
        ranstr = ""
        """