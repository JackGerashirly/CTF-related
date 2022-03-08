from fastecdsa.curve import P521 as Curve
from fastecdsa.point import Point
import hashlib
from Crypto.Util.number import long_to_bytes

P = 0x1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
Curve.p = P
Curve.a = -0x3
Curve.b = 0x51953eb9618e1c9a1f929a21a0b68540eea2da725b99b315f3b8b489918ef109e156193951ec7e937b1652c0bd3bb1bf073573df883d2c34f1ef451fd46b503f00

Gx = 0xc6858e06b70404e9cd9e3ecb662395b4429c648139053fb521f828af606b4d3dbaa14b5e77efe75928fe1dc127a2ffa8de3348b3c1856a429bf97e7e31c2e5bd66
Gy = 0x11839296a789a3bc0045c8a5fb42c7d1bd998f54449579b446817afbd17273e662c97ee72995ef42640c550b9013fad0761353c7086a272c24088be94769fd16650
G = Point(Gx, Gy, curve=Curve)
s = 41231
g = s * G

flag ='HITCTF2020{' + hashlib.md5(long_to_bytes(g.x + g.y)).hexdigest() + '}'
print(flag)
