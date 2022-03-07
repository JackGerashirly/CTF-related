import base64
flag0 = "ZEZNTAAZGJTWJLXVHGXD"


def change(m, c, inv_a, b):
    for i in range(len(m)):
        c.append(chr(((ord(m[i]) - 65) - b) * inv_a % 26 + 97))
    d = ''.join(c)
    return d


if __name__ == "__main__":
    m = flag0
    for inv_a in range(10, 100):
        for b in range(10, 100):
            c = []
            res = change(m, c, inv_a, b) + ""
            if res[:2] == "it":
                print (res)
