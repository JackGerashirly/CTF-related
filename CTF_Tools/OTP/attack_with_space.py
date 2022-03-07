#! /usr/bin/python3
# Reference:
#   - https://www.anquanke.com/post/id/161171#h3-3
# The script is for OTP xor attack, the length of the key 'd better
# smaller than 40.
# Method: Hamming distance + space characteristic with alphabet
# Extension:
#   - What about key with numbers in it?

import string
from itertools import *
import time


def XORsalt(s):
    salt="WeAreDe1taTeam"
    cs = cycle(salt)
    res = b''
    for i in range(0,len(s),2):
        t = int(s[i:i+2],16) ^ ord(next(cs))
        res += bytes([t])
    return res


def bxor(a, b):  # xor two byte string of different length
    if len(a) > len(b):
        return bytes([x ^ y for x, y in zip(a[:len(b)], b)])
    else:
        return bytes([x ^ y for x, y in zip(a, b[:len(a)])])


def hamming_distance(b1, b2): # stop here
    differing_bits = 0
    for byte in bxor(b1, b2):
        differing_bits += bin(byte).count('1')
    return differing_bits


def hex2bin(s):
    return bin(int(bytes.hex(s),16))[2:].encode()


def break_single_key_xor(text):
    key = 0
    possible_space = 0
    max_possible = 0  # Record maximun possible of each character
    letters = string.ascii_letters.encode('ascii')
    for a in range(len(text)):
        maxpossible = 0  # Each character 's space possibility
        for b in range(len(text)):
            if a == b:
                continue
            c = text[a] ^ text[b]
            if c not in letters and c != 0:
                continue
            maxpossible += 1
        if maxpossible > max_possible:
            max_possible = maxpossible
            possible_space = a
    key = text[possible_space] ^ 0x20 # XOR with space
    return chr(key)


def guess_keysize():
    for keysize in range(2,38):
        b1 = hex2bin(cipher[:keysize])
        b2 = hex2bin(cipher[keysize:2*keysize])
        b3 = hex2bin(cipher[2*keysize:3*keysize])
        b4 = hex2bin(cipher[3*keysize:4*keysize])
        b5 = hex2bin(cipher[4*keysize:5*keysize])
        b6 = hex2bin(cipher[5*keysize:6*keysize])
        averaged_distance = (\
            hamming_distance(b1,b2) +\
            hamming_distance(b2,b3) +\
            hamming_distance(b3,b4) +\
            hamming_distance(b4,b5) +\
            hamming_distance(b5,b6)) /\
            (6 * keysize)
    
        if averaged_distance < 3 and averaged_distance > 2:
            candidate_keysize.append(keysize)  # Append to candidata keysize list


def solve(candidate, secret):
    for keysize in candidate:
        block_bytes = [[] for i in range(keysize)]
        for i, byte in enumerate(secret):
            block_bytes[i % keysize].append(byte)
        keys = ''
        try:
            for bbytes in block_bytes:
                keys += break_single_key_xor(bbytes)
            key = bytearray(keys * len(secret), "utf-8")
            plaintext = bxor(secret, key).decode()
            print("keysize:", keysize)
            print()
            time.sleep(0.1)
            print("key is:", keys)
            print()
            time.sleep(0.1)
            print("plaintext:", plaintext)
        except Exception:
            continue


if __name__ == "__main__":
    # The cipher is in format like '123' ---> '303132' in hex
    cipher = "49380d773440222d1b421b3060380c3f403c3844791b202651306721135b6229294a3c3222357e766b2f15561b35305e3c3b670e49382c295c6c170553577d3a2b791470406318315d753f03637f2b614a4f2e1c4f21027e227a4122757b446037786a7b0e37635024246d60136f7802543e4d36265c3e035a725c6322700d626b345d1d6464283a016f35714d434124281b607d315f66212d671428026a4f4f79657e34153f3467097e4e135f187a21767f02125b375563517a3742597b6c394e78742c4a725069606576777c314429264f6e330d7530453f22537f5e3034560d22146831456b1b72725f30676d0d5c71617d48753e26667e2f7a334c731c22630a242c7140457a42324629064441036c7e646208630e745531436b7c51743a36674c4f352a5575407b767a5c747176016c0676386e403a2b42356a727a04662b4446375f36265f3f124b724c6e346544706277641025063420016629225b43432428036f29341a2338627c47650b264c477c653a67043e6766152a485c7f33617264780656537e5468143f305f4537722352303c3d4379043d69797e6f3922527b24536e310d653d4c33696c635474637d0326516f745e610d773340306621105a7361654e3e392970687c2e335f3015677d4b3a724a4659767c2f5b7c16055a126820306c14315d6b59224a27311f747f336f4d5974321a22507b22705a226c6d446a37375761423a2b5c29247163046d7e47032244377508300751727126326f117f7a38670c2b23203d4f27046a5c5e1532601126292f577776606f0c6d0126474b2a73737a41316362146e581d7c1228717664091c"
    cipher = XORsalt(cipher)  # Recover from salt
    candidate_keysize = []  # store it
    guess_keysize()
    print("Candidate keysize: ", candidate_keysize)  # check pass
    solve(candidate_keysize,cipher)

