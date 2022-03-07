# -*-coding: utf-8 -*-
import gmpy2


def encode(s):
    return ''.join([bin(ord(c)).replace('0b', '') for c in s])


def rsa_decrypt(e, c, p, q):  # e 为公钥，c 为密文，p，q 为大质数，以上参数皆为10进制
    phi = (p - 1) * (q - 1)
    n = p * q
    try:
        d = gmpy2.invert(e, phi)  # 求e模phi的逆
        return pow(c, d, n)
    except Exception as e:
        print ("e and phi are not coprime! ")
        raise e


# 写入各参数
e = 65537
c = 118909322501472872291935  # 若密文为16进制，则使用c = int(c1, 16)将其转为10进制
p = 345678901247
q = 678901234579

m = "e4syRs4h"
print (("%r"%m).decode('hex'))


