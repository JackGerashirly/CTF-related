# -*- coding:utf-8 -*-
from gmpy2 import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
import sys
import base64

N = 0
e1 = 0
e2 = 0
flag = 0
ct1 = []
ct2 = []
with open("HUB1") as f1:
    for li in f1:
        if flag == 0:
            N = int(li.strip())
            flag += 1
        elif flag == 1:
            e1 = int(li.strip())
            flag += 1
        else:
            if li.strip() != "":
                ct1.append(int(li.strip()))
    f1.close()

flag = 0
with open("HUB2") as f2:
    for li in f2:
        if flag == 0:
            N = int(li.strip())
            flag += 1
        elif flag == 1:
            e2 = int(li.strip())
            flag += 1
        else:
            if li.strip() != "":
                ct2.append(int(li.strip()))
    f2.close()


s = gcdext(e1, e2)
s1 = s[1]
s2 = -s[2]
plaintext = ""
for i in range(ct1.__len__()):
    c1 = ct1[i]
    c2 = ct2[i]
    c2 = invert(c2, N)
    m = (pow(c1, s1, N) * pow(c2, s2, N)) % N
    plaintext += base64.b64decode(long_to_bytes(m))
    print plaintext
    # print '[-]m is:' + '{:x}'.format(m).decode('hex'), '\n'
print plaintext


