# coding = utf8
def decrypt(key, groupnums):
    plaintext = ""
    half = ""
    for i in range(len(key)):
        half += chr(ord(key[i]) ^ i)

    section = len(key) / groupnums
    for i in range(0, groupnums):
        for j in range(0, section):
            plaintext += half[i + j * groupnums]

    print "When the groupnum is", groupnums, ", the result is : ", plaintext


cipher = "f^n2ekass:iy~>w|`ef\"${Ip)8if"

# 2, 4, 7, 14
circumstance = [1, 2, 4, 7, 14, 28]
for p in circumstance:
    decrypt(cipher, p)

