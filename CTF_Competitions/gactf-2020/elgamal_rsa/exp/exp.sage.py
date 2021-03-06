

# This file was *autogenerated* from the file ./exp.sage
from sage.all_cmdline import *   # import sage library

_sage_const_0x1296 = Integer(0x1296); _sage_const_255310806360822158306697936064463902328816816156848194779397173946813224291656351345682266227949792774097276485816149202739762582969208376195999403112665514848825884325279574067341653685838880693150001066940379902609411551128810484902428845412055387955258568610350610226605230048821754213270699317153844590496606931431733319116866235538921198147193538906156906954406577796507390570080177313707462469835954564824944706687157852157673146976402325057144745208116022973614795377968986322754779469798013426261911408914756488145211933799442123449261969392169406969410065018032795960230701484816708147958190769470879211953704222809883281592308316942052671516609231501663363123562942 = Integer(255310806360822158306697936064463902328816816156848194779397173946813224291656351345682266227949792774097276485816149202739762582969208376195999403112665514848825884325279574067341653685838880693150001066940379902609411551128810484902428845412055387955258568610350610226605230048821754213270699317153844590496606931431733319116866235538921198147193538906156906954406577796507390570080177313707462469835954564824944706687157852157673146976402325057144745208116022973614795377968986322754779469798013426261911408914756488145211933799442123449261969392169406969410065018032795960230701484816708147958190769470879211953704222809883281592308316942052671516609231501663363123562942); _sage_const_42044128297 = Integer(42044128297); _sage_const_6 = Integer(6); _sage_const_232087313537 = Integer(232087313537); _sage_const_5 = Integer(5); _sage_const_653551912583 = Integer(653551912583); _sage_const_15 = Integer(15); _sage_const_802576647765917 = Integer(802576647765917); _sage_const_7 = Integer(7); _sage_const_28079229001363 = Integer(28079229001363); _sage_const_14 = Integer(14); _sage_const_104280142799213 = Integer(104280142799213); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_2 = Integer(2)
from gmpy2 import gcd, invert
from Crypto.Util.number import *
import random

e = _sage_const_0x1296 
c = _sage_const_255310806360822158306697936064463902328816816156848194779397173946813224291656351345682266227949792774097276485816149202739762582969208376195999403112665514848825884325279574067341653685838880693150001066940379902609411551128810484902428845412055387955258568610350610226605230048821754213270699317153844590496606931431733319116866235538921198147193538906156906954406577796507390570080177313707462469835954564824944706687157852157673146976402325057144745208116022973614795377968986322754779469798013426261911408914756488145211933799442123449261969392169406969410065018032795960230701484816708147958190769470879211953704222809883281592308316942052671516609231501663363123562942 

# factor through yafu
fac = [(_sage_const_42044128297 , _sage_const_6 ), (_sage_const_232087313537 , _sage_const_5 ), (_sage_const_653551912583 , _sage_const_15 ),
       (_sage_const_802576647765917 , _sage_const_7 ), (_sage_const_28079229001363 , _sage_const_14 ), (_sage_const_104280142799213 , _sage_const_6 )]


def AMM(q, r, delta, k=_sage_const_1 ):
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

    phi = pow(q, k-_sage_const_1 )*(q-_sage_const_1 )
    mod = pow(q, k)

    while True:  # step1 & step2
        rho = random.getrandbits(mod.nbits()) % mod
        if pow(rho, phi//r, mod) == _sage_const_1 :
            break

    # step 3
    s = phi
    t = _sage_const_0 
    while s % r == _sage_const_0 :
        s //= r
        t += _sage_const_1 
    assert(gcd(s, r) == _sage_const_1 )  # check if s is coprimed with r
    assert(pow(r, t) * s == phi)

    alpha = invert(r, s)
    a, b, c, h = pow(rho, phi//r, mod), pow(delta, r *
                                            alpha-_sage_const_1 , mod), pow(rho, s, mod), _sage_const_1 

    # step 4
    j, k = _sage_const_0 , phi // (r * s)
    for i in range(_sage_const_1 , t):
        k //= r
        d = pow(b, k, mod)
        if d == _sage_const_1 :
            j = _sage_const_0 
        else:
            j = - discrete_log(phi, d, a)  # fix here
            b, h, c = b*(pow(c, r*j, mod)) % mod, h * \
                pow(c, j, mod) % mod, pow(c, r, mod)

    # step 5
    return pow(delta, alpha, mod) * h % mod


def allroot(root, r, q, k = _sage_const_1 ):
    # find all roots satisfy a**r = delta % q**k
    
    phi = (q - _sage_const_1 ) * q**(k - _sage_const_1 )
    mod = q ** k
    all_root = set()
    all_root.add(root)
    while len(all_root) < r:
        new_root = root
        unity = pow(getRandomRange(_sage_const_2 , mod), phi // r, mod)
        for i in range(r - _sage_const_1 ):
            new_root = (new_root * unity) % mod
            all_root.add(new_root)
    return all_root

# since 653551912583**15 > 2**(36*8)
n0 = _sage_const_653551912583 
n = pow(_sage_const_653551912583 , _sage_const_15 )
phi = n * (_sage_const_653551912583  - _sage_const_1 ) // _sage_const_653551912583 
print(gcd(e,phi))
e_p = e // gcd(e, phi)
d = invert(e_p, phi)
c_p = pow(c, d, n)
ar = allroot(AMM(n0,_sage_const_2 ,c_p,_sage_const_15 ),_sage_const_2 ,n0,_sage_const_15 )
for i in ar:
    print(long_to_bytes(i))

