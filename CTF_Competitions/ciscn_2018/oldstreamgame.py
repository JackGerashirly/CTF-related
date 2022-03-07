# -*- coding: utf-8 -*-
# LFSR leaks feedback, goal is to get the initial value, which is the flag
from w366er_tool import Util

taps = [31, 29, 26, 19, 11, 7, 4, 2]
feedback = [32, 253, 238, 248, 164, 201, 244, 8, 63, 51, 29, 168, 35, 138, 229, 237, 8, 61, 240, 203, 14, 122, 131, 53, 86, 150, 52, 93, 244, 77, 124, 24, 108, 31, 69, 155, 206, 19, 95, 29, 182, 199, 103, 117, 213, 220, 186, 183, 167, 131, 228, 138, 32, 60, 25, 202, 37, 194, 47, 96, 174, 98, 179, 125, 232, 228, 5, 120, 227, 167, 120, 126, 180, 41, 115, 13, 149, 201, 225, 148, 66, 136, 235, 62, 46, 116, 125, 130, 22, 164, 120, 85, 7, 161, 55, 180, 19, 205, 105, 12]
f_stream = ""
for i in feedback:
    f_stream += Util.fore_8bits_padding(str(bin(i))[2:])
iv = ""

for i in range(32):
    tmp_iv = 0
    tmp_f_stream = f_stream[31-i] + iv[::-1] + f_stream[:(32 - i - 1)]  # solve bits by bits,remember to reverse to (F_{i-1}, ..., F_{0})
    # print(tmp_f_stream)
    for j in taps:
        tmp_iv ^= int(tmp_f_stream[31 - j])  # convert the index
    iv += str(tmp_iv)
    print(iv)
iv = iv[::-1]  # remember to reverse
print("iv:", iv)
print("flag{", end="")
for i in range(8):
    print(str(hex(int('0b'+iv[i*4:i*4+4], 2)))[2:], end="")
print("}")

