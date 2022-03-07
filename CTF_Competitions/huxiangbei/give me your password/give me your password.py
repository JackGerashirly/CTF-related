# -*- coding:utf-8 -*-
# This Challenge belongs to Remote Challenges.
# Get string "8a9c308c5c0a4b9f2a9fcd35a1d0f006d831de32d7bd73fc5f09c998f5ef9bba" from terminal.
from Cryptodome.Cipher import AES
import binascii

KEY = b'JustKey not fl@g'

def pad(s, block_size):
    return s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size)

cipher = "8a9c308c5c0a4b9f2a9fcd35a1d0f006d831de32d7bd73fc5f09c998f5ef9bba"
iv = cipher[:32].decode('hex')


c = AES.new(KEY, AES.MODE_CBC, iv)
result = iv + c.encrypt(pad("Admin", AES.block_size))
print binascii.hexlify(result)


