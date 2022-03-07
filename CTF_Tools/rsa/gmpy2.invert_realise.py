# -*-coding:utf8-*-
import gmpy2


def egcd(a, c):
    if c == 0:
        return 1, 0, a
    else:
        x, y, q = egcd(c, a % c)  # q = GCD(a , b) = GCD(b, a % b)
        print x, y, q  # 出栈过程
        x, y = y, (x - (a // c) * y)
        return x, y, q


def mod_inv(a, c):
    return egcd(a, c)[0] % c  # 求a模c的逆元


print (mod_inv(47, 30))

print (gmpy2.invert(47,30))  # 对比invert 函数
