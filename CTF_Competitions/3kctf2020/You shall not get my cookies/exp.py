# -*- coding:utf-8 -*-
from pwn import *
from Crypto.Util.number import bytes_to_long
# context.log_level = 'debug'

target = 'youshallnotgetmycookies.3k.ctf.to'
port = 13337

cipher = "6F6A6A2C6E780D070A19001707060C0D"

suffix = ''
fake_iv = ''
dc = ''
try:
    for i in range(1,17):
        assert(len(dc) == 2*(i-1))
        for j in range(0x100):
            guess = hex(j)[2:].upper().zfill(2)
            fake_iv = '00' * (16-i) + guess + suffix
            print('[-]' + fake_iv)
            p = remote(target, port)
            p.sendlineafter('So... whats your cookie: ', fake_iv + cipher)
            res = p.recvall(timeout=4)
            p.close()
            res = res.decode()
            if  len(res) == 11:
                pad = bytes([i])
                dc = hex(int(guess, 16) ^ bytes_to_long(pad))[2:].upper().zfill(2) + dc
                suffix = hex(int(dc, 16) ^ bytes_to_long(bytes([(i+1)]) * i))[2:].upper().zfill(i*2)
                print('[-]  D(C1) '+ dc)
                break
    print('[-]  D(C1) '+ dc)
except pwnlib.exception.PwnlibException:
    pass
# 1C091F451A0B070D00130A1D0D0C0607  for the first block to be d(C2)
# B0A608DDC37A458EEC0B74D37E888E8A  for the second block
# ...3B143145885BB42C94 for the third block
# C2
# 90C560B2A01529EF986E54B016E1FEAA

# C1
# 6F6A6A2C6E780D070A19001707060C0D
# Calculate d(C1)
# 218A7AEECEFB49CADF3D227AD84A21CF

# Calculate C0
# 6CEB0A82ABDB06ABAB50471BB46A63A6

# The whole cipher:
# 6CEB0A82ABDB06ABAB50471BB46A63A66F6A6A2C6E780D070A19001707060C0D90C560B2A01529EF986E54B016E1FEAA
