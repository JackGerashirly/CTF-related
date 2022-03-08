#!/usr/bin/python

import os, string, signal, sys
from Crypto.Cipher import Blowfish
from base64 import *
from secret import flag
from proof_of_work import proof_of_work
banner = '''
 ____  _                __ _     _                          _     _
| __ )| | _____      __/ _(_)___| |__   __      _____  _ __| | __| |
|  _ \| |/ _ \ \ /\ / / |_| / __| '_ \  \ \ /\ / / _ \| '__| |/ _` |
| |_) | | (_) \ V  V /|  _| \__ \ | | |  \ V  V / (_) | |  | | (_| |
|____/|_|\___/ \_/\_/ |_| |_|___/_| |_|   \_/\_/ \___/|_|  |_|\__,_|
'''

bk = 8
master_key = os.urandom(bk) # 8 bytes
sendIV = os.urandom(bk) # 8 bytes
class Blow_CBC_demo:
    def __init__(self, iv):
        self.key = master_key
        self.iv = iv

    def pad(self, message):
        pad_length = bk-len(message)%bk # PKCS7
        return message+chr(pad_length)*pad_length

    def unpad(self, message):
        return message[:-ord(message[-1])]

    def encrypt(self, message):# pad --> CBC(key,iv)_encrypt | message can be bytes or string
        message = self.pad(message) 
        blow = Blowfish.new(self.key, Blowfish.MODE_CBC, self.iv)
        ciphertxt = blow.encrypt(message)
        return ciphertxt

    def decrypt(self, message):
        blow = Blowfish.new(self.key, Blowfish.MODE_CBC, self.iv) # CBC(key,iv)_decrypt --> unpad | message can be bytes or string
        plaintxt = blow.decrypt(message)
        plaintxt = self.unpad(plaintxt)
        return plaintxt

def send_enc(message): # iv (8 bytes) | cipher (8*n bytes)
    sys.stdout.flush()
    handle = Blow_CBC_demo(sendIV)
    ciphertxt = handle.encrypt(message) # --> bytes
    message = sendIV+ciphertxt # bytes
    message = b64encode(message) # base64 encode
    print(message)
    return

def get_enc(): # iv (8 bytes) | cipher (8*n bytes)
    sys.stdout.flush()
    message = sys.stdin.readline().strip()
    try:
        message = b64decode(message) # base64 decode
        if (len(message) > 600): # iv | message can not be longer than 600
            exit(0)
        handle = Blow_CBC_demo(message[:bk]) # initial with my iv
        plaintxt = handle.decrypt(message[bk:]) # decrypt
        return plaintxt
    except:
        print('Error')
        exit(0)

def send_pl(m):
    sys.stdout.flush()
    print(m)
    sys.stdout.flush()

def get_pl():
    sys.stdout.flush()
    return sys.stdin.readline().strip()

def pad(message):
    pad_length = bk-len(message)%bk
    return message+chr(pad_length)*pad_length

if __name__ == '__main__':
    assert(len(flag) == 42)
    if (not proof_of_work()): # pass the proof
        send_pl("Bye!")
        exit()
    signal.alarm(180)
    send_pl(banner)
    send_enc('Blowfish_w0rld') # len = 14
    while True: # dead circulation
        try:
            message = get_enc().strip()
            if message.startswith('get_flag'):  # vulnerability
                user = get_pl().strip()
                blow = Blowfish.new(master_key)
                send_pl(b64encode(blow.encrypt(pad(user+flag))))
            elif message.startswith('exit'):
                exit()
            else:
                send_enc('Invalid command')
        except:
            exit()
