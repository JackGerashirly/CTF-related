# -*-coding: utf-8 -*-
# wp:https://github.com/ctfs/write-ups-2014/tree/master/tinyctf-2014/wtc-rsa-bbq
import gmpy2


def isqrt(n):  # 求 N 的根号（根据 16进制多位 ff 的性质判断 p, q 可能为 N 的根号）
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def rsa_decrypt(e, c, p, q):  # e 为公钥，c 为密文，p，q 为大质数，以上参数皆为10进制
    phi = (p - 1) * (q - 1)
    n = p * q
    try:
        d = gmpy2.invert(e, phi)  # 求e模phi的逆
        return pow(c, d, n)
    except Exception as e:
        print "e and phi are not coprime! "
        raise e


def find_prime(i, n):
    while True:
        if n - (i * (n / i)) == 0:
            return i, n / i
        else:
            i += 1
            print i


# 将 N(模数) 从16进制转换为10进制
s = "0x062d3d61c92452630147e89670ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
s = int(s, 16)

# 写入各参数
e = 65537
c = open('cipher.bin', 'rb').read().encode('hex')  # 打开 .bin 文件
c1 = int(c, 16)  # 将字符串转为十进制数字

i = isqrt(s)
p, q = find_prime(i, s)  # 求大质数 q ,p

# print rsa_decrypt(65537, 242094131279916, 23781539, 13574881)  # 脚本检验样本
m = rsa_decrypt(e, c1, p, q)
print m
print ('%x' % m).decode('hex')  # 直接获得字符文本 10 -> chr
