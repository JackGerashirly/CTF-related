import random
from pwn import *

def USR(x, shift):
    res = x
    for i in range(32):  # Take more times to ensure that the res is origin answer
        res = x ^ res >> shift
    return res

def USL(x, shift, mask):
    res = x
    for i in range(32):  # Take more times to ensure that the res is origin answer
        res = x ^ (res << shift & mask)
    return res

def randomnum_to_MT(v):
    v = USR(v, 18)
    v = USL(v, 15, 0xefc60000)
    v = USL(v, 7, 0x9d2c5680)
    v = USR(v, 11)
    return v

def MT_to_randomnum(y):
    y = y ^ (y >> 11)
    y = y ^ ((y << 7) & (0x9d2c5680))
    y = y ^ ((y << 15) & (0xefc60000))
    y = y ^ (y >> 18)
    return y

def solve(a, b):
    res = []
    MT_iadd1, MT_iadd397 = randomnum_to_MT(a), randomnum_to_MT(b)
    for msb in range(2):
        y = (msb * 0x80000000) + (MT_iadd1 & 0x7fffffff)
        MT_i = MT_iadd397 ^ (y >> 1)
        if (y % 2) != 0:
            MT_i = MT_i ^ 0x9908b0df
        res.append(MT_to_randomnum(MT_i))
    return res

while True:
    s = remote("47.98.156.31", 7667)
    s.sendline("1396")
    s.sendline("1792")
    guess = []
    for _ in range(2019):
        a = s.recvline().strip()
        if "Nope" not in a:
            guess.append(int(a))

    res = solve(*guess)
    s.sendline(str(res[0]))
    resp = s.recvline().strip()
    if "success" in resp:
        print resp
        exit(0)
