from fastecdsa.curve import P521 as Curve
from fastecdsa.point import Point
from Crypto.Util.number import bytes_to_long, isPrime
from os import urandom
from random import getrandbits, randint
from flag import flag
import hashlib
from Crypto.Util.number import long_to_bytes


ecc_p = Curve.p
a = Curve.a
b = Curve.b

Gx = Curve.gx
Gy = Curve.gy
G = Point(Gx, Gy, curve=Curve)
s = 41231
g = s * G

assert (flag == 'HITCTF2020{' + hashlib.md5(long_to_bytes(g.x + g.y)).hexdigest() + '}')
print("P:" + hex(ecc_p) + "\n")
print("a:" + hex(a) + "\n")
print("b:" + hex(b) + "\n")
print("g:", hex(G.x), hex(G.y))
