# -*- coding: utf-8 -*-
# 这题很迷。。
n = ['69', '35', '41', '01', '1C', '9E', '75', '78', '5D', '48', 'FB', 'F0', '84', 'CD', '66', '79', '55', '30', '49', '4C', '56', 'D2', '73', '70', '12', '45', 'A8', 'BA', '85', 'C0', '3E', '53', '73', '1B', '78', '2A', '4B', 'E9', '77', '26', '5E', '73', 'BF', 'AA', '85', '9C', '15', '6F', '54', '2C', '73', '1B', '58', '8A', '66', '48', '5B', '19', '84', 'B0', '80', 'CA', '33', '73', '5C', '52', '0C', '4C', '10', '9E', '32', '37', '12', '0C', 'FB', 'BA', 'CB', '8F', '6A', '53', '01', '78', '0C', '4C', '10', '9E', '32', '37', '12', '0C', 'FB', 'BA', 'CB', '8F', '6A', '53', '01', '78', '0C', '4C', '10', '9E', '32', '37', '12', '0C', 'FB', 'BA', 'CB', '8F', '6A', '53', '01', '78', '0C', '4C', '10', '9E', '32', '37', '12', '0C', '89', 'D5', 'A2', 'FC']
# n 取出来

specical_n = ['01', '78', '0C', '4C', '10', '9E', '32', '37', '12', '0C', 'FB', 'BA', 'CB', '8F', '6A', '53']
# special_n 取出来

num = []
j = 0
r = ""
for i in range(0, len(n)):  # len() 也可以求数组长度
    x = int(n[i], 16)
    y = int(specical_n[j % 16], 16)
    j += 1
    num.append(hex(x ^ y)[2:])  # [ a ：b] 从第 a 位 到 第 b 位
    r += chr((x ^ y))  # 返回 int 十进制

print r
print num

num1 = []
r1 = ""
for i in range(0, len(num)):
    x = int(num[i], 16)
    num1.append(hex(x ^ 32)[2:])
    r1 += chr((x ^ 32))

print r1
print num1


r2 = ""
num2 = []
for i in range(0, len(num1)):
    x = int(num1[i], 16)
    num2.append(hex(x ^ 94)[2:0])
    r2 += chr((x ^ 94))

print r2
print num2
print chr(ord('k') ^ ord('^'))

r3 = ""
num3 = ['21', '58', '2c', '6c', '30', 'be', '12', '17', '32', '2c', 'db', '9a', 'eb', 'af', '4a', '73']
for i in range(0, len(num3)):
    r3 += chr(int(num3[i], 16))
print r3