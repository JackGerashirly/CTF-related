import math
from Crypto.Util.number import long_to_bytes
from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import getRandomNBitInteger
from Crypto.Util.number import getPrime
from Crypto.Util.number import isPrime
from Crypto.Util.number import inverse

from flag import flag

def nextPrime(n):
    n += 2 if n & 1 else 1
    while not isPrime(n):
        n += 2
    return n

def init(S, K):
    j = 0
    k = []
    K=list(K)
    for i in range(len(K)):
        K[i]=ord(K[i]) # to char len = 100 // 8 = 13
    for i in range(256):
        S.append(i)  # s list 0-255
        k.append(K[i % len(K)]) 
    for i in range(256):
        j = (j + S[i] + k[i]) % 256
        S[i], S[j] = S[j], S[i]

def Encrypt(key, D):
    S=[]
    init(S, key)
    i = j = 0
    result =b''

    for a in D:
        a=ord(a)
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k = bytes([a ^ S[(S[i] + S[j]) % 256]])
        result += k
    return result


def Decrypt(key, D):
    S = []
    init(S, key)
    i = j = 0
    result = b''
    for a in D:
        a=ord(a)
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k = bytes([a ^ S[(S[i] + S[j]) % 256]])
        result += k
    return result

if __name__ == "__main__":
    key = long_to_bytes(getRandomNBitInteger(100))
    e=getPrime(512)
    print ("e=",e)

    E=nextPrime(e)
    f = math.factorial(e) % E   # f = e! mod E

    d = long_to_bytes(f)

    c1 = bytes_to_long(Encrypt(key, d))
    print("c1=",c1)

    c2=bytes_to_long(Encrypt(key, flag))
    print ("c2=",c2)

# e= 8768431453653962054853832386801335854105061327022291417088778857581796325166174829298734682431255192950523854451967733577841100835715651543540971198198681
# c1= 11831774853911019972017320460161774814750266235729653101958962953511957754480894541171974374871242127323737819393853417678958793722480644778746975681327479
# c2= 410992428811672881118232062346883001867079265462810154261017013352873467471099210054471