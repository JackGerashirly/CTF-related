#! /usr/bin/python2
# -*-coding: utf-8 -*-
# Written by buki
from Crypto.Util.number import getPrime
from pwn import *
import gmpy2
import sys

# prime pool
pripool = []
for i in range(64):	
    if gmpy2.is_prime(i):
        pripool.append(i)
pripool.append(67)  # getPrime has some exceptional situation...
print "[+]Successfully generating prime pool!"
print pripool


# get q, p
def getpq(m):
    for i in pripool:
        for j in pripool:
            if (i - 1) * (j - 1) == m:
                return i, j


sh = remote('38.39.244.2', 28101)

fullflag = ""
while True:
    sh.recvuntil("m:  ", drop=True)
    M = int(sh.recvuntil("d:  ", drop=True).strip())
    print "  [-]M = ", M
    d = int(sh.recvuntil("Now", drop=True).strip())
    print "  [-]d = ", d
    sh.recvuntil('\n')
    p, q = getpq(M)
    print "  [-]p = ", p
    print "  [-]q = ", q
    m = p * q * 2 ** 5
    b = 4 * p * q + 1
    c = getPrime(10)
    x = 200
    before = []
    group = 1

    i = 0

    # get the groupsize
    while True:
        if x in before:
            print "  [-]groupsize: ", i
            group = i
            break
        else:
            before.append(x)
            x = (b * x + c) % m
            i += 1

    # get the position of real flag
    if group < 2 ** d:
        left = (2 ** d) % group
        res = group - left
        print "  [-]result: ", res
        sh.sendline(str(res))
        flag = int(sh.recvline().strip())
        print "  [-]flag = ", flag
        fullflag += chr(flag/257)
        print "[+]fullflag = ", fullflag
    else:
        res = group - 2 ** d
        print "  [-]result: ", res
        sh.sendline(str(res))
        flag = int(sh.recvline().strip())
        print "  [-]flag = ", flag
        fullflag += chr(flag/257)
        print "[+]fullflag = ", fullflag
