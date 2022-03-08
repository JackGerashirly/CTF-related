from gmpy2 import gcd, invert
from Crypto.Util.number import *
import random

e = 0x1296
c = 255310806360822158306697936064463902328816816156848194779397173946813224291656351345682266227949792774097276485816149202739762582969208376195999403112665514848825884325279574067341653685838880693150001066940379902609411551128810484902428845412055387955258568610350610226605230048821754213270699317153844590496606931431733319116866235538921198147193538906156906954406577796507390570080177313707462469835954564824944706687157852157673146976402325057144745208116022973614795377968986322754779469798013426261911408914756488145211933799442123449261969392169406969410065018032795960230701484816708147958190769470879211953704222809883281592308316942052671516609231501663363123562942

# factor through yafu
fac = [(42044128297, 6), (232087313537, 5), (653551912583, 15),
       (802576647765917, 7), (28079229001363, 14), (104280142799213, 6)]


def AMM(q, r, delta, k=1):
    """
    Adleman-Manders-Miller r-th Root Extraction Algorithm in F_q

    * Attention:
        - r and q satisfy r | q - 1
    :param q: modulus q --> int
    :param r: exponent r --> int
    :param delta: remain --> int
    :param k: the exponent of k, default is 1 --> int
    :return: a r-th root of delta
    """

    phi = pow(q, k-1)*(q-1)
    mod = pow(q, k)

    while True:  # step1 & step2
        rho = random.getrandbits(mod.nbits()) % mod
        if pow(rho, phi//r, mod) == 1:
            break

    # step 3
    s = phi
    t = 0
    while s % r == 0:
        s //= r
        t += 1
    assert(gcd(s, r) == 1)  # check if s is coprimed with r
    assert(pow(r, t) * s == phi)

    alpha = invert(r, s)
    a, b, c, h = pow(rho, phi//r, mod), pow(delta, r *
                                            alpha-1, mod), pow(rho, s, mod), 1

    # step 4
    j, k = 0, phi // (r * s)
    for i in range(1, t):
        k //= r
        d = pow(b, k, mod)
        if d == 1:
            j = 0
        else:
            j = - discrete_log(phi, d, a)  # fix here
            b, h, c = b*(pow(c, r*j, mod)) % mod, h * \
                pow(c, j, mod) % mod, pow(c, r, mod)

    # step 5
    return pow(delta, alpha, mod) * h % mod


def allroot(root, r, q, k = 1):
    # find all roots satisfy a**r = delta % q**k
    
    phi = (q - 1) * q**(k - 1)
    mod = q ** k
    all_root = set()
    all_root.add(root)
    while len(all_root) < r:
        new_root = root
        unity = pow(getRandomRange(2, mod), phi // r, mod)
        for i in range(r - 1):
            new_root = (new_root * unity) % mod
            all_root.add(new_root)
    return all_root

# since 653551912583**15 > 2**(36*8)
n0 = 653551912583
n = pow(653551912583, 15)
phi = n * (653551912583 - 1) // 653551912583
print(gcd(e,phi))
e_p = e // gcd(e, phi)
d = invert(e_p, phi)
c_p = pow(c, d, n)
ar = allroot(AMM(n0,2,c_p,15),2,n0,15)
for i in ar:
    print(long_to_bytes(i))
