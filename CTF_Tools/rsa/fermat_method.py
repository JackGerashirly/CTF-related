# -*- coding:utf-8 -*-
# Fermat Method: Used in two close-gap integers
from gmpy2 import *


def fermat(n):
    a = isqrt_rem(n)[0] + 1
    b = a ** 2 - n
    while 1:
        q = isqrt_rem(b)
        if q[1] == 0:
            fac = a - q[0]
            p = n / fac
            return fac, p
        a += 1
        b = a ** 2 - n


n = 65537 * next_prime(65537)
print('n =', n)
print('[+]Factorising n...\n')
print(fermat(n), '\n')
print('[!]Done!\n')
