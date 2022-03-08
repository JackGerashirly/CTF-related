#from Qmath import *
from libnum import *
from pwn import *

def inv(a, q):
    assert gcd(a % q, q) == 1
    return xgcd(a % q, q)[0] % q

def get_key(r, s1, s2, h1, h2, q, y, g, p):
    k_ = (h1 - h2) % q
    invv = inv(s1 - s2, q)
    k = k_ * invv % q
    print "k =", k
    x = (s1 * k - h1) * inv(r, q) % q
    assert pow(g, x, p) == y
    print "x =", x
    return x

def make_signature(h, x, g, p, q):
    k = 151512
    r = pow(g, k, p) % q
    s = (h + x * r) * inv(k, q) % q
    return (r, s)

def get_num(string):
    io.recvuntil(string)
    return int(io.recvline())


host = '47.111.59.243'
port = 8001
io = remote(host,port)
io.recvuntil('for me?')
io.send('\n')
p = get_num('p:')
q = get_num('q:')
g = get_num('g:')
y = get_num('y:')
io.recvuntil('before:')
io.send('\n')
md5 = []
r = []
s = []
for i in range(12):
    md5.append(get_num('digest: '))
    cur = io.recvline().split(', ')
    r.append(int(cur[0][1: ].strip('L')))
    s.append(int(cur[1][: -2].strip('L')))
rr = 0
index = (0, 0)
for i in range(len(r)):
    rr = r[i]
    flag = 0
    for j in range(i+1, len(r)-1):
        if r[j] == rr:
            rr = r[j]
            index = (i, j)
            flag = 1
            break
    if flag:
        break
print 'Found same key:', rr
s1 = s[i]
s2 = s[j]
h1 = md5[i]
h2 = md5[j]
x = get_key(rr, s1, s2, h1, h2, q, y, g, p)
io.recvuntil('Its MD5 digest is:')
h = int(io.recv())
sig = make_signature(h, x, g, p, q)
print 'Finished!!!'
print 'make_signature------------------------------------------------------'
print '>', sig
io.sendline(str(sig))
print io.recv(512)

