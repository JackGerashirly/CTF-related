from secret import *
from Crypto.Util.number import *
flag = bytes_to_long(flag) 
ranges = int(log(flag,3))
pri = next_prime(ZZ.random_element(3^16, 3^17))
it = 5
N = pri^120

P.<x> = PolynomialRing(Zmod(N), implementation='NTL')
poly = 0
for c in range(it):
    poly += ZZ.random_element(3^ranges, 3^(ranges+1))*x^c
poly = poly - poly(flag)
print(pri)
print(poly)

