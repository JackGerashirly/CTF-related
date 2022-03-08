#! /bin/usr/python2
import hashlib
import gmpy2
from Crypto.Util.number import bytes_to_long, long_to_bytes
from pwn import *
s = remote('47.98.156.31', 7557)


def proof_of_work():
    s.recvuntil("[+] hashlib.sha256(s).hexdigest() = ")
    res = s.recvuntil("[+] s[:7].encode('hex') = ", drop=True).strip()
    part_s = s.recvuntil("[-] s.encode('hex') = ", drop=True).strip()
    part_s = int(part_s, 16) * (2 ** 24)
    for i in range(2 ** 24):
        if hashlib.sha256(long_to_bytes(part_s + i)).hexdigest() == res:
            part_s = part_s + i
            s.sendline(str(hex(part_s))[2:])
            print s.recvline().strip()
            break


def solve1(N1, a, b, next):
    state = ((next - b) * gmpy2.invert(a, N1)) % N1
    s.sendline(str(state))
    print s.recvline().strip()


def solve2(N2, a, next, next1):
    state = (next - (next1 - next) * gmpy2.invert(a, N2)) % N2
    s.sendline(str(state))
    print s.recvline().strip()


def solve3(N3, next, next1, next2):
    a = ((next1 - next2) * gmpy2.invert((next - next1), N3)) % N3
    solve2(N3, a, next, next1)


def challenge1():
    s.recvuntil("[+] lcg.N = ")
    N1 = int(s.recvuntil("[+] lcg.a = ", drop=True).strip())
    a = int(s.recvuntil("[+] lcg.b = ", drop=True).strip())
    b = int(s.recvuntil("[+] lcg.next() = ", drop=True).strip())
    next = int(s.recvuntil("[-] lcg.seed = ", drop=True).strip())
    solve1(N1, a, b, next)


def challenge2():
    s.recvuntil("[+] lcg.N = ")
    N2 = int(s.recvuntil("[+] lcg.a = ", drop=True).strip())
    a = int(s.recvuntil("[+] lcg.next() = ", drop=True).strip())
    next = int(s.recvuntil("[+] lcg.next() = ", drop=True).strip())
    next1 = int(s.recvuntil("[-] lcg.seed = ", drop=True).strip())
    solve2(N2, a, next, next1)


def challenge3():
    s.recvuntil("[+] lcg.N = ")
    N3 = int(s.recvuntil("[+] lcg.next() = ", drop=True).strip())
    next = int(s.recvuntil("[+] lcg.next() = ", drop=True).strip())
    next1 = int(s.recvuntil("[+] lcg.next() = ", drop=True).strip())
    next2 = int(s.recvuntil("[-] lcg.seed = ", drop=True).strip())
    solve3(N3, next, next1, next2)


def challenge4():
    states = []
    s.recvuntil("[+] lcg.next() = ")
    states.append(int(s.recvuntil("[+] lcg.next() = ", drop=True).strip()))
    states.append(int(s.recvuntil("[+] lcg.next() = ", drop=True).strip()))
    states.append(int(s.recvuntil("[+] lcg.next() = ", drop=True).strip()))
    states.append(int(s.recvuntil("[+] lcg.next() = ", drop=True).strip()))
    states.append(int(s.recvuntil("[+] lcg.next() = ", drop=True).strip()))
    states.append(int(s.recvuntil("[-] lcg.seed = ", drop=True).strip()))
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [abs(t2*t0 - t1*t1) for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    N4 = reduce(gmpy2.gcd, zeroes)
    solve3(N4, states[0], states[1], states[2])


proof_of_work()
challenge1()
challenge2()
challenge3()
challenge4()
print s.recvline()
s.interactive()