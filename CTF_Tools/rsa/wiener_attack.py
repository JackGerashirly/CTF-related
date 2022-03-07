# -*- coding: utf-8 -*-
# Wiener Attack, used in big public key (or small private key).
# For better comprehension, please view site: https://www.tr0y.wang/2017/11/06/CTFRSA/index.html
from gmpy2 import *


# 展开为连分数
def continuedfra(x, y):
    cF = []
    while y:
        cF += [x / y]
        x, y = y, x % y
    return cF


def simplify(ctnf):
    numerator = 0
    denominator = 1
    for x in ctnf[::-1]:
        numerator, denominator = denominator, x * denominator + numerator
    return (numerator, denominator)


# 连分数化简
def calculatefrac(x, y):
    cF = continuedfra(x, y)
    cF = map(simplify, (cF[0:i] for i in range(1, len(cF))))
    return cF


# 解韦达定理
def solve_pq(a, b, c):
    par = isqrt(b * b - 4 * a * c)
    return (-b + par) / (2 * a), (-b - par) / (2 * a)


def wienerattack(e, n):
    for (d, k) in calculatefrac(e, n):
        if k == 0:
            continue
        if (e * d - 1) % k != 0:
            continue
        phi = (e * d - 1) / k
        p, q = solve_pq(1, n - phi + 1, n)
        if p * q == n:
            return abs(int(p)), abs(int(q))
    print('not find!')


n = 86966590627372918010571457840724456774194080910694231109811773050866217415975647358784246153710824794652840306389428729923771431340699346354646708396564203957270393882105042714920060055401541794748437242707186192941546185666953574082803056612193004258064074902605834799171191314001030749992715155125694272289
e = 46867417013414476511855705167486515292101865210840925173161828985833867821644239088991107524584028941183216735115986313719966458608881689802377181633111389920813814350964315420422257050287517851213109465823444767895817372377616723406116946259672358254060231210263961445286931270444042869857616609048537240249
c = 37625098109081701774571613785279343908814425141123915351527903477451570893536663171806089364574293449414561630485312247061686191366669404389142347972565020570877175992098033759403318443705791866939363061966538210758611679849037990315161035649389943256526167843576617469134413191950908582922902210791377220066
p, q = wienerattack(e, n)
print('[+]Found!', '\n')
print('  [-]p =', p)
print('  [-]q =', q)
print('  [-]n =', p * q)
d = invert(e, (p-1)*(q-1))
print('  [-]d =', d)
# print('  [-]m is: ' + '{:x}'.format(pow(c, d, n)).decode('hex'), '\n')
print('[!]All Done!')
