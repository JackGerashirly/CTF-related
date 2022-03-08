#!/usr/bin/python3 -u

import random
from Crypto.Util.number import *
from gmpy2 import *

a = 0x497a81edc78549df # 63
block_len = 64

def gen_prime(bits_len):
    s = random.getrandbits(block_len) # fixed
    
    while True:
    	s |= 0xe000000000000003 # fixed 16140901064495857667
    	p = 0
    	for _ in range(bits_len // block_len):  # fixed 16 rounds
      		p = (p << block_len) + s
      		s = a * s % 2**block_len
    	if is_prime(p):
      		return p

n = None
e = 0x10001
flag = open("flag.txt", "rb").read()

with open("challenge.py") as f:
    print(f.read())
    
print("Welcome to my Prime Obsession. Tell me what do you want.\n")
while True:
    print("[1] Generate key")
    print("[2] Get Encrypted flag")
    print("[3] Exit")
    opt = int(input(">>> "))
    if opt == 1:
        p = gen_prime(1024)
        q = gen_prime(1024)
        n1 = p * q
        print('pq =',hex(n1))
        c = getRandomInteger(100)
        p = next_prime(p+c)
        q = next_prime(q+c)
        n = p * q
        print('n =',hex(n)) 
    if opt == 2:
        if not n:
            print("No key generated :(")
        else:
            print('cipher =',hex(pow(bytes_to_long(flag), e, n)))
    if opt == 3:
        print("Good bye! Good luck in this game :)")
        break
    print("\n")
