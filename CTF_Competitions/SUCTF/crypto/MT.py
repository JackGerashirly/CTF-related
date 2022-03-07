from Cryp.Util import number


def decrypt_left(cipher, blocksize, mask):
    plain = cipher
    t = cipher
    for i in range(32 / blocksize):
        tt = (t << blocksize) & mask
        plain = plain ^ tt
        t = tt
    return plain


def decrypt_right(cipher, blocksize, mask):
    plain = cipher
    t = cipher
    for i in range(32 / blocksize):
        tt = t >> blocksize
        tt = tt & mask
        plain = plain ^ tt
        t = tt
    return plain


def invert(block):
    block = decrypt_right(block, 19, 0xffffffff)
    block = decrypt_left(block, 17, 2245263360)
    block = decrypt_left(block, 9, 2029229568)
    block = decrypt_right(block, 13, 0xffffffff)
    return block


def transform(message):
    assert len(message) % 4 == 0
    new_message = ''
    for i in range(len(message) / 4):
        block = message[i * 4: i * 4 + 4]
        block = number.bytes_to_long(block)
        print bin(block)
        print len(bin(block)) - 2
        block = invert(block)
        block = number.long_to_bytes(block, 1)
        new_message += block
    return new_message


transformed_flag = '641460a9e3953b1aaa21f3a2'
c = transformed_flag.decode('hex')
flag = transform(c)
print flag.encode('hex')
