# sage 8.9
ciphers = load("cipher.sobj")
pubkey = load("pubkey.sobj")

C = codes.LinearCode(pubkey)
from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm
A = LeeBrickellISDAlgorithm(C, (6,6))

s = ""
for cipher in ciphers:
    corrected = A.decode(cipher[0])    # c = m * pubkey + e ==> c' = m * pubkey
    m = pubkey.solve_left(corrected)
    s += ''.join(str(i) for i in m)

print hex(int(s, 2)).strip('0xL').decode('hex')
# flag{c941a3cc-85e3-4401-a0f1-764206e71bf3}
