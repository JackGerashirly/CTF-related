# Just need to find out the gcd of two of the modulus among all , then we can get p and q.
# -*-coding: utf-8 -*-
import gmpy2
import sys

e = 0
c = []
n = []
q = 0
p = 0

with open("real_RSA5.txt") as f:
    for lin in f:
        li = lin.strip()
        if li.startswith("c = "):
            c.append(int(li[4:]))
        elif li.startswith("n = "):
            n.append(int(li[4:]))
        elif li.startswith("e = "):
            e = int(li[4:])
        else:
            pass

flag = 0
for i in range(n.__len__()):
    for j in range(i + 1, n.__len__()):
        if gmpy2.gcd(n[i], n[j]) != 1:
            vn = n[i]
            p = gmpy2.gcd(n[i], n[j])
            q = vn / p
            flag = i
            break
    if flag:
        break

ol = (p - 1) * (q - 1)
d = gmpy2.invert(e, ol)
m = pow(c[flag], d, n[flag])
m = ('%x' % m).decode('hex')
sys.stdout.write(m)
