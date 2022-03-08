import binascii

def exor(a, b):
    temp = ""
    for i in range(n):
        if (a[i] == b[i]):
            temp += "0"
        else:
            temp += "1"
    return temp


n = 26936
K1 = '''''' # Too long to show
K2 = '''''' # Too long to show
R3 = '''''' # Too long to show
L3 = '''''' # Too long to show

R2 = L3
L2 = exor(exor(K2, R2), R3)

R1 = L2
L1 = exor(exor(K1, R1), R2)

plaintext = L1+R1
plaintext = int(plaintext, 2)
plaintext = binascii.unhexlify('%x' % plaintext)
plaintext = binascii.unhexlify(plaintext)
print(plaintext)
