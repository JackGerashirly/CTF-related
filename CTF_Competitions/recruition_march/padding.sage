#! /usr/bin/python
# Franklin-Reiter attack against RSA.
# If two messages differ only by a known fixed difference between the two messages
# and are RSA encrypted under the same RSA modulus N
# then it is possible to recover both of them.

# Inputs are modulus, known difference, ciphertext 1, ciphertext2.
# Ciphertext 1 corresponds to smaller of the two plaintexts. (The one without the fixed difference added to it)

import random
import math
import binascii


def franklinReiter(n,e,r,c1,c2):
    R.<X> = Zmod(n)[]
    f1 = X^e - c1
    f2 = (X + r)^e - c2
    # coefficient 0 = -m, which is what we wanted!
    return Integer(n-(compositeModulusGCD(f1,f2)).coefficients()[0])

  # GCD is not implemented for rings over composite modulus in Sage
  # so we do our own implementation. Its the exact same as standard GCD, but with
  # the polynomials monic representation
def compositeModulusGCD(a, b):
    if(b == 0):
        return a.monic()
    else:
        return compositeModulusGCD(b, a % b)

def CoppersmithShortPadAttack(e,n,C1,C2,eps=1/100):
    """
    Coppersmith's Shortpad attack!
    Figured out from: https://en.wikipedia.org/wiki/Coppersmith's_attack#Coppersmith.E2.80.99s_short-pad_attack
    """
    import binascii
    P.<x,y> = PolynomialRing(ZZ)
    ZmodN = Zmod(n)
    g1 = x^e - C1
    g2 = (x+y)^e - C2
    res = g1.resultant(g2)
    P.<y> = PolynomialRing(ZmodN)
    # Convert Multivariate Polynomial Ring to Univariate Polynomial Ring
    rres = 0
    for i in range(len(res.coefficients())):
        rres += res.coefficients()[i]*(y^(res.exponents()[i][1]))

    diff = rres.small_roots(epsilon=eps)
    # Test point here
    print rres
    recoveredM1 = franklinReiter(n,e,diff[0],C1,C2)
    print(recoveredM1)
    print("Message is the following hex, but potentially missing some zeroes in the binary from the right end")
    print(hex(recoveredM1))
    print("Message is one of:")
    for i in range(8):
        msg = hex(Integer(recoveredM1*pow(2,i)))
        if(len(msg)%2 == 1):
            msg = '0' + msg
        if(msg[:2]=='0x'):
            msg = msg[:2]
        print(binascii.unhexlify(msg))


def testFranklinReiter():
    n = 0 # 1024-bit modulus
    e = 0

    m = randint(0, n) # some message we want to recover
    r = randint(0, n) # random padding

    c1 = pow(m + 0, e, n)
    c2 = pow(m + r, e, n)
    print(m)
    recoveredM = franklinReiter(n,e,r,c1,c2)
    print(recoveredM)
    assert recoveredM==m
    print("They are equal!")
    return True


n = 0x995d87f5e77364947de43de9a04dc7b3cb81976f4853c51f183adff5682cdf30ad30d9c33e076581e75f7ebe48f39ab10d42b7b182879db59d8f3961d9fb7b24dbfe7a3e5455977cf0f10e487843685d1586d395ab54c2de24423654b16efb2fe0c88c34c48fef292a87d0674a85b698520397fcf89605e354d8786fc6acaf65


e = 7
c1 = 0x27e34ccd3a7b6772c6ddaa953952dd16288f9bfac5fbd48fbaa42e9c22a08f8fd5e9a14396170178b1161ab0ab7b9cd06b20f78dc73fd29f92c3a5afa9672d21ce33c095b30ee997005d99deb108792f02f4be592e792a37b6f0312f96b4337e715e5465a54db9b5c16b461323fbbe3a560dfafd123d738ab6e9d4948fb4dc51


c2 = 0x7b5e8e881b904b900b56903ee9c3b62b65424dcccfac8fcb74921df8955ecb7f4d34abd900e4806b3ff32e637fcdf9ff9132e1d34b90d46d17855afd4ada6472e2bcf3be439aea1bd1551c405130788c388c24bf3684fab4e0044fdc2b00e5acecc5cd254b8053285d538f4a752d986b4603094300033402136f8eb050edf906



CoppersmithShortPadAttack(e, n, c1, c2)
