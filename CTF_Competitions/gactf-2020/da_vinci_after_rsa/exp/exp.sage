from Crypto.Util.number import long_to_bytes
import itertools

c = 421363015174981309103786520626603807427915973516427836319727073378790974986429057810159449046489151
pa = 9749
pb = 11237753507624591
pc = 9127680453986244150392840833873266696712898279308227257525736684312919750469261
# factor with yafu

mas = GF(pa)(c).nth_root(5, all=True) # find 5-th root in modulus pa, so do below
mbs = GF(pb)(c).nth_root(5, all=True)
mcs = GF(pc)(c).nth_root(5, all=True)
# algl = True, which means find all roots, otherwise...
# all = False is default

# find all possible m
ms = [] 
for ma, mb, mc in itertools.product(mas, mbs, mcs): 
    m = ZZ(crt(list(map(ZZ,[ma,mb,mc])), [pa,pb,pc]))
    mi = long_to_bytes(m)
    if mi[:4] == b'flag':
        flag = mi[5:-1]

print(flag)

# decrypt da vinci encryption
fb = [1,1]
LEN = len(flag)
while len(fb) < LEN:
    fb.append(fb[-1] + fb[-2])
fb[0] = 0
enc = [0,28657,2,1,3,17711,5,8,13,21,46368,75025,34,55,89,610,377,144,233,1597,2584,4181,6765,10946,987]
r_flag = [flag[fb.index(enc[i])] for i in range(LEN)]
for i in r_flag:
    print(chr(i),end='')


