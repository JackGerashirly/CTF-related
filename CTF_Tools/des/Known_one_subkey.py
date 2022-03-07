# -*- coding:utf-8 -*-
# This script must run in Python 3 and it uses soreatu tool.
# It can solve the situation that we only know the cipher and one of the subkeys.
# The principle is that the subkey only shifts(logical) one/two bits during its encryption without any changes, as a
# result of which, any subkeys will retrieve after 16-time shifts(logical). Support formula: (16 - 4) * 2 + 4 = 28bits.
from base64 import b64decode
from itertools import product
from Cryp.soreatu_tool.DES import *          # https://github.com/soreatu/Cryptography/blob/master/DES.py


guess_8bit = list(product(range(2), repeat=8))
not_in_PC2 = [9, 18, 22, 25, 35, 38, 43, 54]

def re_PC2(sbkey):
    # 48-bit -> 56-bit
    res = [0]*56
    for i in range(len(sbkey)):
        res[PC_2_table[i]-1] = sbkey[i]
    return res # ok

def guess_CiDi10(sbkey, t):
    res = re_PC2(sbkey)
    for i in range(8):
        res[not_in_PC2[i]-1] = guess_8bit[t][i]
    return res # ok

def guess_allsbkey(roundkey, r, t):
    sbkey = [[]]*16
    sbkey[r] = roundkey
    CiDi = guess_CiDi10(roundkey, t)
    Ci, Di = CiDi[:28], CiDi[28:]
    for i in range(r+1,r+16):
        Ci, Di = LR(Ci, Di, i%16)
        sbkey[i%16] = PC_2(Ci+Di)
    return sbkey # ok

def long_des_enc(c, k):
    assert len(c) % 8 == 0
    res = b''
    for i in range(0,len(c),8):
        res += DES_enc(c[i:i+8], k)
    return res

def try_des(cipher, roundkey):
    for t in range(256):
        allkey = guess_allsbkey(roundkey, 10, t)
        plain = long_des_enc(cipher, allkey[::-1])
        if plain.startswith(b'NCTF'):  # Recognised Sign
            print(plain)

if __name__ == "__main__":
    cipher = b64decode(b'm0pT2YYUIaL0pjdaX2wsxwedViYAaBkZA0Rh3bUmNYVclBlvWoB8VYC6oSUjfbDN')  # CipherText
    sbkey10 = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    # The 10th subkey.
    try_des(cipher, sbkey10)
# b'NCTF{1t_7urn3d_0u7_7h47_u_2_g00d_@_r3v3rs3_1snt}'
