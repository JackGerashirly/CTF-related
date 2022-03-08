from Crypto.Util.number import getPrime, long_to_bytes, getStrongPrime
from hashlib import sha1
from random import randint
from secret import flag, p, q
import libnum

def gen_t(d):
    while True:
        t = getPrime(16)
        if t % 4 == 3 and libnum.gcd(d, t - 1) == 1:
            break
    return t

def sign(m, params):
    d, p, q, n, t1, t2, e1, e2 = params
    dp = d % ((p - 1) * (t1 - 1))
    dq = d % ((q - 1) * (t2 - 1))
    k = getPrime(16)
    Sp = pow(m + k, dp, p * t1)
    Sq = pow(m, dq, q * t2)
    Cp = q * t2 * libnum.invmod(q * t2, p * t1)
    Cq = p * t1 * libnum.invmod(p * t1, q * t2)
    S = (Cp * Sp + Cq * Sq) % (n * t1 * t2)
    c1 = (m - pow(S, e1, t1) + 1) % t1  # solved
    c2 = (m - pow(S, e2, t2) + 1) % t2  # solved
    return pow(S, c1 * c2, n)

e = 65537
assert p < q
assert flag == "flag{" + sha1(long_to_bytes(p)).hexdigest() + "}"

n = p*q
print(n)
d = libnum.invmod(e, (p - 1) * (q - 1)) # solved
t1 = gen_t(d) # solved
et1 = libnum.invmod(d, t1 - 1)
t2 = gen_t(d)
et2 = libnum.invmod(d, t2 - 1)
params = (d, p, q, n, t1, t2, et1, et2)
m = randint(1, n-1)
print(m)
sig = sign(m, params)
print(sig)

