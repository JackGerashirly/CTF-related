import hashlib
import binascii
from Cryptodome.Util.number import *
import string

XOR = lambda s1, s2: bytes([x1 ^ x2 for x1, x2 in zip(s1, s2)])
initial_state = [0] * 233
initial_state2 = [0] * 233
cipher = ['cef4876036ee8b55aa59bca043725bf3',
          '50a5e491debdef7ef7d63e9609a288ca',
          '1e2c82a7fe566bd8709e73c8d495ea50',
          '4a486ed11189faf8e6fb35617e47d2d1',
          'ad5e4783e96afeaae9f7104ec477fb39',
          'fe4ec619bf58289709e15c4449f03fc5',
          '1cba918cd0ebfdc12376b41e78154064',
          '82733b3b200826b6c78d86563edaea94',
          'dccf459a4291517a4b8367d7b4a53aee',
          'cd7e0accf661bfc726f5ba62e1c0e041',
          '00108ad32e7d5711f780185cba5cf31d',
          '328bee84066be4ab9582cf9d4bfe3c6f',
          '96a7732e1c37d800c90fd46277147f0a',
          '26c149dcd5eeb0f2df0c075627bc220b',
          'e5eefdd67186056ac28c21e155a7f247',
          '664aaecdb498134de274df10114d1f06',
          'f84dd21820f150d69c9439d909dec0f5',
          'ccfeab61b62db2ea91d31bc8163ff16c',
          '7f458006bd5ac4a5f5bfae2770b23ccf',
          'b7195b76aa0a9aa146831667a7b9fe08',
          'c19e691afadccb3ca5169ef3fabaa3da',
          'd47d536e89ed4cee6f788bc969c3ad31',
          '37850ebfc46a73af2b0c036c3da4b4a1',
          '6506f499445c604dd73eeb846a52f881',
          '515a3ad0ab448b4f9ed3e0ab1fffac60',
          'b223dde6450ba6198e90e14de107aaf2']

starts = "npuctf{"
ends = "}"


class mt73991:
    def __init__(self, seed):
        self.state = [seed] + [0] * 232
        self.flag = 0
        self.srand()
        self.generate()

    def srand(self):
        for i in range(232):
            self.state[i + 1] = 1812433253 * (self.state[i] ^ (self.state[i] >> 27)) - i
            self.state[i + 1] &= 0xffffffff

    def generate(self):
        for i in range(233):
            y = (self.state[i] & 0x80000000) | (self.state[(i + 1) % 233] & 0x7fffffff)
            temp = y >> 1
            temp ^= self.state[(i + 130) % 233]
            if y & 1:
                temp ^= 0x9908f23f
            self.state[i] = temp

    def getramdanbits(self):
        if self.flag == 233:
            self.generate()
            self.flag = 0
        bits = self.Next(self.state[self.flag]).to_bytes(4, 'big')
        self.flag += 1
        return bits

    def Next(self, tmp):
        tmp ^= (tmp >> 11)
        tmp ^= (tmp << 7) & 0x9ddf4680
        tmp ^= (tmp << 15) & 0xefc65400
        tmp ^= (tmp >> 18) & 0x34adf670
        return tmp


def USMR(x, shift, mask):
    res = x
    for i in range(32):
        res = x ^ (res >> shift & mask)
    return res


def USML(x, shift, mask):
    res = x
    for i in range(32):
        res = x ^ (res << shift & mask)
    return res


def inv_Next(x):
    x = USMR(x, 18, 0x34adf670)
    x = USML(x, 15, 0xefc65400)
    x = USML(x, 7, 0x9ddf4680)
    x = USR(x, 11, 0xffffffff)
    return x


def inv_srand(value, index):
    for i in range(index-1, -1, -1):
        value += i
        value *= inverse(1812433253, 0x100000000)
        value = USR(value, 27, 0xffffffff)
        value &= 0xffffffff
    return value


def USR(value, shift, mask):
    i = 0
    res = 0
    while i * shift < 32:
        partMask = ((0xffffffff << (32 - shift)) & 0xffffffff) >> (shift * i)
        part = value & partMask
        value ^= (part >> shift) & mask
        res |= part
        i += 1
    return res


# hash all known characters
hash_starts = []
for i in starts:
    hash_starts.append(hashlib.md5(i.encode()).digest())
# print(hash_starts)
hash_ends = hashlib.md5(ends.encode()).digest()

state = [0] * 233

# first 7 characters
for i in range(len(starts)):
    key = XOR(hash_starts[i], binascii.unhexlify(cipher[i]))
    for j in range(4):
        tmp = inv_Next(bytes_to_long(key[4*j:4*j+4]))
        state[4*i+j] = tmp
# print(state[:28])  # check pass


def decrypt(key, cipher):
    cipher = binascii.unhexlify(cipher)
    temp = XOR(key, cipher)
    for i in md5_dic:
        if temp == i:
            print(string.printable[md5_dic.index(i)], end="")


# the last character
key = XOR(hash_ends, binascii.unhexlify(cipher[-1]))
for i in range(4):
    tmp = inv_Next(bytes_to_long(key[4*i:4*i+4]))
    state[100+i] = tmp
# print(state[100:104]) # check pass


# Since it can be simplified, there are only two situations of old_state[104]

# old_state[104] is even
y = (state[0] ^ state[103]) << 1  # recover y
# print(y) # check pass
poss_1 = y & 0x7fffffff
poss_2 = (y & 0x7fffffff) | 0x80000000

# print(poss_1) possible one is correct
# print(poss_2)
# check pass


# get the seed of each situation
poss_1 = inv_srand(poss_1, 104)
poss_2 = inv_srand(poss_2, 104)
print(poss_1)
print(poss_2)


# generate md5 dictionary
md5_dic = []
for i in string.printable:
    md5_dic.append(hashlib.md5(i.encode()).digest())


random_1 = mt73991(poss_1)
random_2 = mt73991(poss_2)

# recover the flag from random_1
flag = ""
for i in range(26):
    key = b''.join([random_1.getramdanbits() for _ in range(4)])
    decrypt(key, cipher[i])

# Since random_1 is the correct one, random_2 can be ignored.
