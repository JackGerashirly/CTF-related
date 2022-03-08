from Crypto.Cipher import DES
from Crypto.Util.number import long_to_bytes
import base64
import hashlib
#b'D4meWwYAUE4='
#b'qMMGe3wORmFJePnQnM2ZeA=='

strdic = '0123456789abcdef'
dic = []
#part1
"""
print("-----Part 1 Start!-----")

for i in strdic:
    for j in strdic:
        for k in strdic:
            for m in strdic:
                possi_k1 = (i + j + k + m) * 2
                e1=DES.new(possi_k1.encode(),DES.MODE_CBC,bytes(8))
                c1=e1.encrypt(b'12345678')
                dic.append(c1)

print("-----Part 1 End!-----")
print(len(dic))

for i in strdic:
    for j in strdic:
        for k in strdic:
            for m in strdic:
                possi_k2 = (i + j + k + m) * 2
                e2=DES.new(possi_k2.encode(),DES.MODE_CBC,bytes(8))
                c2=e2.encrypt(b'\x0f\x89\x9e[\x06\x00PN')
                if c2 in dic:
                    print(dic.index(c2))
                    print(possi_k2)
                    exit(0)

"""

# part2
"""
index = 45238
cnt = 0
for i in strdic:
    for j in strdic:
        for k in strdic:
            for m in strdic:
                possi_k1 = (i + j + k + m) * 2
                if cnt == index:
                    print(possi_k1)
                    exit(0)
                cnt += 1


"""
k1 = 'b0b6b0b6'
k2 = 'ba62ba62'
c = b'qMMGe3wORmFJePnQnM2ZeA==' # encrypted flag after base64
c = base64.b64decode(c)
e=DES.new(k2.encode(),DES.MODE_CBC,bytes(8))
c = e.encrypt(c)
e=DES.new(k1.encode(),DES.MODE_CBC,bytes(8))
c= e.decrypt(c)
print(c)
print(hashlib.md5(c).hexdigest())
