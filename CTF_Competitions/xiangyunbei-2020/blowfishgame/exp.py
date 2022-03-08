#coding:utf-8
from base64 import *
from pwn import *
from hashlib import sha384
from string import printable
from tqdm import *

#context.log_level = 'debug'
sh = remote("8.131.69.237","15846")
def _xor(s1,s2):
    tmp=""
    for i in range(len(s1)):
        tmp+=chr(ord(s1[i])^ord(s2[i]))
    #print tmp
    return tmp

def sha384(content):
    return hashlib.sha384(content).hexdigest()

def PoW():
    sh.recvuntil("sha384(XXX+")
    tail = sh.recvuntil(")")[:-1]
    sh.recvuntil(" == ")
    tar = sh.recvuntil("\n")[:-1]
    for i in tqdm(printable): # learn to use tqdm
        for j in printable:
            for k in printable:
                tmp = i+j+k
                #print tmp+tail
                #print tar
                #print sha384(tmp+tail)
                if sha384(tmp+tail) == tar:
                    sh.sendline(tmp)
                    return
    else:
        print "no"
PoW()
#sh.interactive()                    
sh.recvuntil("\\___/|_|  |_|\\__,_|\n") # python print line by line
sh.recvuntil("\n")
msg = sh.recvuntil("\n")[:-1]
#print "msg",msg
#msg='ralI0ycVw0IuDjZ/cPp0m6dxFH1ROdAo'
iv = b64decode(msg)[:8]
cipher = b64decode(msg)[8:]
#print iv,cipher
ticket=b64encode(_xor(_xor(iv,'Blowfish'),'get_flag')+cipher)
#print "ticket",ticket

pre="0"*47
flag=""

for block in range(42):
        sh.sendline(ticket)
        sh.sendline(pre)
        target = b64decode(sh.recvuntil("\n")[:-1])[40:48]
        for i in printable:
            tmp = '0'*(47-block)+flag+i
            sh.sendline(ticket)
            sh.sendline(tmp)
            get = sh.recvuntil("\n")[:-1]
            now = b64decode(get)
            #print now
            if now[40:48] == target:
                flag += i
                print flag
                pre = pre[:-1]
                break
        else:
            print "no"