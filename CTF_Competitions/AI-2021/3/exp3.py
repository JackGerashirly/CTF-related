from functools import reduce
from Crypto.Util.number import long_to_bytes
from gmpy2 import gcd,invert,next_prime

def crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(gcd, zeroes))
    return crack_unknown_multiplier(states, modulus)

def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * invert(states[1] - states[0], modulus) % modulus
    return crack_unknown_increment(states, modulus, multiplier)

def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment

def USR(value, shift, mask):
    i = 0
    res = 0
    while i * shift < 319:
        partMask = (((2**319-1) << (319 - shift)) & (2**319-1)) >> (shift * i)
        part = value & partMask
        value ^= (part >> shift) & mask
        res |= part
        i += 1
    return res


states = [58605992502479537155943965904595921273, 525605798656979919420608964379033982804, 607738431135489138748992347244318940466, 631747898536603358381419028993140907216, 13450658701001781564543219325486287717, 407826262741495712819054543462943222370]

n,m,c = crack_unknown_modulus(states)
s = states[-1]
s = (m * s + c) % n
e = next_prime(s)
# print(e)
p = 138092450043978032187397495330379791355629274237204650898232878263413301988536751004632087169676028049236253598677819980191406826529664613957150122788435561338344715937422320958238628877093605040078776555586363593650646481242888908171897232624141894446324625781720275455534977357099473212936612966142541689717
phi = p - 1
d = invert(e,phi)
en_flag = 40522976224675404992818282038409183193065303107530049168092540620105120083552580372904554927069109321998620410524986748598618388761467715127564839742806614159382512978830563949967053562802375030363283879451081474764301602860367140250483857874335594802704634427276762179861996608105102610424633434334897307449739846880323406404392707133580686043181007091235341464802410874449708870610192494627811013526751435468963111672237058189288520084494533786573065843704621915085789731723587760910378534773137633519620193203450046994466154848079413319979993890764583887936777316159487010002407093187269512820453207591173395762513970799972839858119501585885277954258269483363133460240339866272358522431904252286259542327658731232568465990008278265227086114042064326334937705758042097987623388556184022737180944807660792992413039097516526454455063218161704505837882378018400687043158628503465274374703624257222504948612055237771581019005
flagmodp = pow(en_flag,d,p)
#print(flagmodp)
flag = USR(flagmodp,10,2**319-1)
#print(flag)
#print(flag ^ (flag >> 10))
assert(flagmodp == flag ^ (flag >> 10))
print(long_to_bytes(flag))
