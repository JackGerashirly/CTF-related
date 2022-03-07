# -*- coding: utf-8 -*-
# Pollard Rho Method: Used in Two large-gap prime integers.
# Have been learned in 7th, July, 2020
from random import randint
from gmpy2 import *

n = 8
x1 = 10
x2 = 10
c = 7
y = lambda x, z, m: (x ** 2 + z) % m
start = 0

print('n =', n)
print('[+]Factorising n...', '\n')

while start == 0 or x1 != x2:
    start = 1
    x1 = y(x1, c, n)
    x2 = y(y(x2, c, n), c, n)
    fac = gcd(abs(x1 - x2), n)
    if fac > 1 and fac != n:
        print("[", fac, ",", n // fac, "]", '\n')
        break

print('[!]Done!\n')
