from Crypto.Util.number import *  
from gmpy2 import *  
  
  
def reverse(x):  
    y = 0  
    while x != 0:  
        y = y * 2 + x % 2  
        x = x // 2  
    return y

"""
Compute low 12 bits of possible q
"""
n = 158985980192501034004997692253209315116841431063210516613522548452327355222295231366801286879768949611058043390843949610463241574886852164907094966008463721486557469253652940169060186477803255769516068561042756903927308078335838348784208212701919950712557406983012026654876481867000537670622886437968839524889  
cur = []  
k = 12  
mod = 2**k  
for i in range(1, mod, 2):  
    t = invert(i, 4096) * (n % 4096) % 4096  
    t2 = int(bin(reverse(t))[2:].ljust(k, "0"), 2)  
    i2 = int(bin(reverse(i))[2:].ljust(k, "0"), 2)  
    l = t2 * i2 * pow(2, 1024 - 2 * k)  
    r = (t2 + 1) * (i2 + 1) * pow(2, 1024 - 2 * k)  
    if l <= n <= r:  
        cur.append(i)  
  
#print(cur) 

"""
Compute 
"""
length = 16  
for c in range(4, 65):  
    #print(c)  
    nc = []  
    mod = 16**c  
    for x in cur:  
        for y in range(16):  
            i = x + y * 16**(c - 1)  # i is lowest 4c bits of p  
            t = invert(i, mod) * (n % mod) % mod  # t is lowest 4c bits of q  
            # t2 is highest 4c bits of q  
            t2 = int(bin(reverse(t))[2:].ljust(length, "0"), 2)  
            # i2 is highest 4c bits of p  
            i2 = int(bin(reverse(i))[2:].ljust(length, "0"), 2)  
            l = i2 * t2 << (4 * (128 - c) * 2)  
            r = (i2 + 1) * (t2 + 1) << (4 * (128 - c) * 2)  
            if l <= n <= r:  
                nc.append(i)  
    cur = nc
    length += 4
    #print(len(cur))

"""
possibilities of various 256 bits is known
"""
c = 64  
mod = 16**c  
for i in cur:  
    t = invert(i, mod) * (n % mod) % mod  
    assert t * i % mod == n % mod  
    t2 = int(bin(reverse(t))[2:].ljust(256, "0"), 2)  
    i2 = int(bin(reverse(i))[2:].ljust(256, "0"), 2)  
    p1 = t2 << 256 | i  # get 256 is already enough
    q1 = i2 << 256 | t  
    if p1 * q1 == n:  
        print("find")  
        break  
p = p1  
#p = 11954360020159164180709939019047385560179850436770100207193049651260543609501871575909448998378290922795824941066935928157032997160163537467165365731882943  
enc = 103728452309804750381455306214814700768557462686461157761076359181984554990431665209165298725569861567865645228742739676539208228770740802323555281253638825837621845841771677911598039696705908004858472132222470347720085501572979109563593281375095145984000628623881592799662103680478967594601571867412886606745  
  
q = n // p  
e = 65537  
d = invert(e, (p-1)*(q-1))  
flag = pow(enc, d, n)  
print(long_to_bytes(flag))
