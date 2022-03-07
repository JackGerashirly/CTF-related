c = "177401504b0125272c122743171e2c250a602e3a7c206e014a012703273a3c0160173a73753d"
li_c = [int(c[i:i+2], 16) for i in range(0, len(c), 2)]
# print(li_c)
m = "flag{"
d_c = li_c[3] - li_c[0]
# print(d_c)
d_m = ord(m[3]) - ord(m[0])
# print(d_m)  # a = 57 mod 128
a = 57
# print((li_c[0] - a * ord(m[0])) % 128)
# print(chr(97))  y1 = 'a'
# print((li_c[1] - a * ord(m[1])) % 128)
# print(chr(104)) y2 = 'h'
# print((li_c[2] - a * ord(m[2])) % 128)
# print(chr(104))  # y3 = 'h'
# print((li_c[3] - a * ord(m[3])) % 128)
m = ""
from gmpy2 import invert
import itertools
inv_a = invert(a, 128)
key = itertools.cycle("ahh")
for i in li_c:
    m += chr(((i - ord(next(key))) * inv_a) % 128)
print(m)

