# -*-coding: utf-8 -*-
import gmpy2
import sys


def rsa_decrypt(e, c, p, q):  # e 为公钥，c 为密文，p，q 为大质数，以上参数皆为10进制
    phi = (p - 1) * (q - 1)
    n = p * q
    try:
        d = gmpy2.invert(e, phi)  # 求e模phi的逆
        return pow(c, d, n)
    except Exception as e:
        print("e and phi are not coprime! ")
        raise e


# 写入各参数
e = 17
p = 100000463
q = 1000000007
c = []
m = 0
with open("secret.txt") as f:
        text = f.read()
        t = text.split('\n')
        c = t

for i in range(0, len(c)):
    m = rsa_decrypt(17, int(c[i]), 100000463, 1000000007)
    sys.stdout.write(('%x' % m).decode('hex'))  # 10 进制转 chr
