#!/user/bin/env python
# -*-coding:utf-8 -*-

ciphertext = "1220248014224204040180114021202244048012208842101180118010124"  # 密文开头不为零

s = ciphertext.split('0')
flag = ""
for i in range(len(s)):
    list = []
    for j in s[i]:
        list.append(j)
    b = 0
    for k in list:
        b += int(k)
    # 字母ascii值与字母顺序相差为96
    flag += chr(b+64)
print flag
