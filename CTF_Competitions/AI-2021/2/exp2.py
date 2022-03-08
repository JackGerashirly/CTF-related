# -*- coding:utf-8 -*-
import gmpy2
from Crypto.Util.number import long_to_bytes


def Factorize(n, e, d):
    g = 2
    while True:
        k = e * d - 1
        while not k & 1:
            k //= 2
            p = int(gmpy2.gcd(pow(g, k, n) - 1, n)) % n
            if p > 1:
                return (p, n // p)
        g = int(gmpy2.next_prime(g))



n = 0x96ed2727e4446e26c84552a9a19640c7d720c9b6e661cfcfec03463e92a9d0b228ddc9847c0daa137a19db67294626c535fe71c388f6ea3eb8cb5dbf09a84374eb021c9297a29394cf77da157c1b8be77b09a4fcbe54bf3dc93d33539e842766ad8e38369093ddc034ac32583a48e299a4d8b31b606b1729298ee136664b8b77
e1 = 0x10001
e2 = 0x3f1
d1 = 0x7d12e57b1aa157038ebe5c45b56256270671e6984b0dcdf10a2ea07ce480143240c9a3e1c60870e499306a717073f157476aa88e99a7bdf1e2a4adf8ce21025cc6c05035c4a1d7e3b6f061464872e65118384999f0154f3c1761fa68d4685126b7fc98f4c2cdc41c98aa4e099a868a89099dd2170664647efca2c8d8e06a2e49
c1 = 0x6c435db37217bc4da3f225a8f1a0501e03a97d2cbc4fa249df051ed66c1559b68885f4fa181bdd9e98242441f463dbbc1c26d1eea2c5774a0a905b366c8775bce8e52182dc32a93647c9b8842b74abc434e5b84eeae679a3b19cb7a1ef6ae8f65d22ce6ab438a16119805eee83408a68207bbdfde5181a8bd8b4794c711d33c4
c2 = 0x8cb5d8861e5838f41910d6eaf142a8d47b92e0c6b1b1e9e25896f7169644bbb726ccfdc82ba50932fbc45f00c53dda42f8efc358a5108cde8aaa9f38b493aa3417c9522924f06847ba4a3dd26f005a610f7633877fbe89e090df5cb3a7a5ebae0fbe72eabb339b21fa2ddd33844a5cb53e39491fc472721ed676ae07b33c8d6e

p,q = Factorize(n, e1, d1)
assert(p*q == n)
phi = (p - 1) * (q - 1)
d2 = gmpy2.invert(e2,phi)
m1 = pow(c1,d1,n)
m2 = pow(c2,d2,n)
print(long_to_bytes(m1))
print(long_to_bytes(m2))


