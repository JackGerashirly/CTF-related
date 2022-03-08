#!/usr/bin/env sage -python
#-*- coding: utf-8 -*-
from sage.all import *
import binascii


n=0xafa5236a0f7859587285161d98682d1960e7ab63f2f2687113dc3119a4c42c531e1c859c06a7a4c94615f1b3234688d4de14a87712c9c252fe2a08b80e2c3957083928dc4cebbe10453d59c9c54f36d8be1be578f31aa668cd11862b9dd4c814a18a1ea3b2a6059c4f473e998c4ffce3b18c4ef36bf84a396ac827daab441387


cipher=0x5e3e72dd3e9d633fd3b99e2303ab31b429f046765cb23be2f4f13d32652f621979e29c71df2c9fde7adf3057b8d446295da656f42e358635205b926157e322b2a31e89582015eada144134d1f5090e6b735ad0576776537436c64055dfe978cb3c150359d7e3e6b4703c9d5ffe48790991126f040d4df1517c62c88acb48e634




e2 = 0x10001

pbits = 512

for i in range(0,2**16):
  p4=0x1f2458a57aaf9cbb2bb6045f5abf5d5d8b7556220d2740631cb9d67154d8e2b17e0670000  # Remember to fill the zeros
  p4 = p4 + int(hex(i),16)
  print "	[-] p4.nbits: ", p4.nbits()
  kbits = pbits - p4.nbits()  #未知需要爆破的比特位数
  p4 = p4 << kbits 
  PR.<x> = PolynomialRing(Zmod(n))
  f = x + p4
  roots = f.small_roots(X=2^kbits, beta=0.4) #进行爆破

  #print roots
  if roots:        #爆破成功，求根
    p = p4+int(roots[0])
    assert n % p == 0
    q = n/int(p)
    phin = (p-1)*(q-1)
    d = inverse_mod(e2,phin)
    flag = pow(cipher,d,n)
    flag = hex(int(flag))[2:-1]
    print binascii.unhexlify(flag)
