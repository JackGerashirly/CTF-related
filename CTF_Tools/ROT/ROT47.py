# -*- coding:utf-8 -*-
# Used for ROT47
# Test string "v)*L*_F0<}@H0>F49023@FE0#@EN".
import base64


def rot47(strs):
    sl = []
    for i in range(len(strs)):
        j = ord(strs[i])
        if 33 <= j <= 126:
            sl.append(chr(((j+14) % 94) + 33))
        else:
            sl.append(strs[i])
    return ''.join(sl)


cipher = raw_input("Please input your rot47 cipher: " + '\n')
print rot47(cipher)



