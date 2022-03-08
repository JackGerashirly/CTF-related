# -*- coding:utf8 -*-
import base64
import random
from hashlib import *
from pwn import *

secret = "pxIALhdgqbmusNcu+3gEI3tgQlTNeX0RcVb9tbGCzt0zw5GZEBeQAbE8ybRUTtRW"
secret1 = base64.b64decode(secret)[0:16]
secret2 = base64.b64decode(secret)[16:32]
secret3 = base64.b64decode(secret)[32:]
p = remote('47.98.156.31', 5666)

# pass the first obstacle
p.recvuntil("Please find a string that md5(str + ")
salt = p.recv(4)
p.recvuntil(")[0:5] == ")
res = p.recv(5)
p.recvuntil("[>] Give me xxxxx: ")
code = ""
for i in range(1, 10000000):
    if md5(str(i) + salt).hexdigest().startswith(res):
        code = str(i)
        print "[+] MD5 has been solved"
        break
p.sendline(code)

middle = []
padding = ''

for x in xrange(1,17):
    for y in xrange(0,256):
    	ranstr = ""
    	for ran in range(16-x):
    		ranstr += chr(random.randint(0, 255)) # Calculate random string
        IV = ranstr + chr(y) + padding
        p.recvuntil("[>] Please input your option: ")
        p.sendline("d")
        p.recvuntil("[>] IV: ")
        p.sendline(base64.b64encode(IV))
        p.recvuntil("[>] Data: ")
        p.sendline(base64.b64encode(secret3))
        res = p.recvuntil("\n")
        if 'done' in res:
            middle.append(y ^ x)
            print middle
            padding = ''
            for z in middle:  # reverse
                padding = chr((x+1) ^ z) + padding
            break


flag = ""
for x,y in zip(middle,secret2[::-1]):
    # first block
    # flag += chr(x ^ ord('A'))
    # other block
    flag += chr(x ^ ord(y))
print flag[::-1]

# GWHT{5befac3acd0cc4c0e2d8021cd0fffec5}
# References: 
# 1. https://www.freebuf.com/articles/database/150606.html --> Help to Improve the Method Using Random IV(string)
# 2. https://www.freebuf.com/articles/database/151167.html
