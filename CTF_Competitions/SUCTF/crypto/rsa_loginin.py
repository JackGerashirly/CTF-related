# -*-coding: utf-8 -*-
import gmpy2


def rsa_decrypt(e, c, p, q):  # e 为公钥，c 为密文，p，q 为大质数
    phi = (p - 1) * (q - 1)
    n = p * q
    try:
        d = gmpy2.invert(e, phi)  # 求e模phi的逆
        return pow(c, d, n)
    except Exception as e:
        print "e and phi are not coprime! "
        raise e


# 写入各参数
e = 65537
c1 = "0xad939ff59f6e70bcbfad406f2494993757eee98b91bc244184a377520d06fc35"  # 此处c1密文为16进制
c = int(c1, 16)  # 将密文转为10进制
p = 282164587459512124844245113950593348271
q = 366669102002966856876605669837014229419

m = rsa_decrypt(e, c, p, q)
print m
print ('%x' % m).decode('hex')  # 10 进制转 chr

