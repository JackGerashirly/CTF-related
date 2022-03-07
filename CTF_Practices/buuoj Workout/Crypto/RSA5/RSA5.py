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
        print "e and phi are not coprime! "
        raise e


# 写入各参数
e = 19
p = 49891
q = 18443

cipher = []

with open("rsa5.txt") as f:
    i = 0
    while True:
        temp = f.readline()
        if temp == "":
            break
        cipher.append(temp[:-1])
        i += 1


for i in range(cipher.__len__()):
    c = int(cipher[i])
    m = rsa_decrypt(e, c, p, q)
    pl = ('%x' % m).decode('hex')  # 10 进制转 chr
    sys.stdout.write(pl)
