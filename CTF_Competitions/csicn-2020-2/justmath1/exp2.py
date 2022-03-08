import math
from Crypto.Util.number import *
import gmpy2
from libnum import xgcd


def nextPrime(n):
    n += 2 if n & 1 else 1
    while not isPrime(n):
        n += 2
    return n


def xor(a, b):
    ans = b''
    for i in range(len(a)):
        ans += long_to_bytes(a[i] ^ b[i])
    return ans


e= 8768431453653962054853832386801335854105061327022291417088778857581796325166174829298734682431255192950523854451967733577841100835715651543540971198198681
c1= 11831774853911019972017320460161774814750266235729653101958962953511957754480894541171974374871242127323737819393853417678958793722480644778746975681327479
c2= 410992428811672881118232062346883001867079265462810154261017013352873467471099210054471

fa = 1
E = nextPrime(e)
for i in range(E-2, e, -1):
    fa *= xgcd(i, E)[0] % E
    fa %= E
fa = long_to_bytes(fa)
c1 = long_to_bytes(c1)
c2 = long_to_bytes(c2)
k = xor(c1[:36], fa[:36])
flag = xor(c2, k)
print (flag)
