from pwn import *
import itertools
import string
from hashlib import md5

s = remote("47.98.156.31", 6226)
dic = string.ascii_letters + '_-\{\}'
print "  [-] your dic is defined: " + dic
s.recvuntil("str + ")
salt = s.recv(4)
print "  [-] salt is: " + salt
s.recvuntil("== ")
res = s.recv(5)
print "  [-] res is: " + res
s.recvuntil("[>] Give me xxxxx:")
r = ''
for i in range(10000000):
    if md5(str(i) + salt).hexdigest().startswith(res):
        r = str(i)   
        break

s.sendline(r)
print "  [-]proof sovled"
flag = 'GWH'
padd = '!.$%^&*-='
while True:
    now = flag[-2:]
    for i in dic:
        s.recvuntil("[>] Please input your option:")
        s.sendline("E")
        s.recvuntil("[>] Input your message:")
        tmp = now+i
        s.sendline(padd+tmp)
        s.recvuntil("The result is ")
        res = s.recvline().strip()
        print res
        if len(res)==96:
            flag +=i
            print flag
            break
