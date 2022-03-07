'''
plaintext1 = "RC4IsInteresting"
plaintext2 = "ThisIsAEasyGame"

ciphertext1 = 12078640933356268898100798377710191641
ciphertext2 = 79124196547094980420644350061749775

key1 = []
for i in range(len(plaintext1) - 1, -1, -1):
     key1 = [ord(plaintext1[i]) ^ (ciphertext1 & 0xff)] + key1
     ciphertext1 >>= 8
print(key1)

key2 = []
for i in range(len(plaintext2) - 1, -1, -1):
     key2 = [ord(plaintext2[i]) ^ (ciphertext2 & 0xff)] + key2
     ciphertext2 >>= 8
print(key2)

# [91, 85, 118, 176, 158, 228, 216, 21, 145, 123, 89, 181, 165, 203, 106, 126]
# [91, 85, 118, 176, 158, 228, 216, 21, 145, 123, 89, 181, 165, 203, 106]
'''
# Suppose the bit length of the flag.png is n bits, key1 and key2 can be written like:
# key1: k1, k2, ..., kn
# key2: k0, k1, ..., k(n-1)
# Above we have already known k0 is 126, which is the last key of plaintext2,
# we can retrieve m0, then k1, after that m1 and so on
from PIL import Image
from numpy import array

img1 = array(Image.open(r"./enc1.png"))
img2 = array(Image.open(r"./enc2.png"))


def recovery_img(im1, im2, k):
    x1, y1, z1 = im1.shape
    for i in range(x1):
        for j in range(y1):
            pixel1 = im1[i, j]
            pixel2 = im2[i, j]
            for _ in range(3):
                pixel2[_] = pixel2[_] ^ k
                k = pixel1[_] ^ pixel2[_]
    im2 = Image.fromarray(im2)
    im2.save("dec.png")


recovery_img(img1, img2, 126)
