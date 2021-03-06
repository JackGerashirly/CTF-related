import json
from os import urandom
from pwn import remote, process
from string import ascii_letters, digits
from itertools import product

PAD = (("2019") * 8).decode('hex')

def get_paddings_dict(n):
    ans = {}
    for i in range(n):
        ans[i] = pad(i+1)
    return ans

def pad(n):
    pad_length = n
    return chr(pad_length) + PAD[:pad_length - 1]

def crack_byte(token, pos, i):
    token[pos] = i
    return ''.join('{:02x}'.format(x) for x in token)

def find_pad(r, token, pos, last_x):
    token = bytearray(token)
    padings = get_paddings_dict(pos+1)
    if pos:
        token[0] = last_x[0] ^ ord(padings[0][0]) ^ ord(padings[pos][0])
        for j in range(1, pos):
            token[j] = last_x[j]
    for i in range(256):
        payload = crack_byte(token, pos, i)
        r.sendline(payload)
        ans = r.recvline()
        if i % 64 == 0:
            print("current step: ", pos, i, ans)
        if 'padding' in ans:
            continue
        else:
            return i
    raise Exception("All padings are incorrect")

if __name__ == '__main__':
    r = remote("47.98.156.31", 7887)
    token_hex = r.recvline(False)
    print(token_hex)
    token = token_hex.decode('hex')
    parts = [token[i:i+16] for i in range(0, len(token), 16)]
    known = "TF{***********"
    flag = ''
    exp_pad = pad(1)
    c1 = parts[2]
    c2 = parts[3]
    last_x = []
    for i in range(len(known)):
        exp_pad = pad(i+1)
        x = find_pad(r, c1+c2, i, last_x)
        i2 = x ^ ord(exp_pad[i])
        ch = chr(i2 ^ ord(c1[i]))
        if i < len(known) and ch == known[i]:
            flag += ch
            print("Horay!", flag)
            last_x.append(x)
        else:
            flag += ch
            print("Is it right?", flag)
            last_x.append(x)
    print('TetC' + flag[:-2])