# coding:utf8
import time


ma, mb, mc, md = 0x505a1, 0x40f3f, 0x1f02, 0x31
key = open("data").read()


def lfsr(r, m): return ((r << 1) & 0xffffff) ^ (bin(r & m).count('1') % 2)


def calcR(x, y):
    assert len(x) == len(y)
    cnt = 0.0
    for i, j in zip(x, y):
        cnt += (i == j)
    return cnt / len(x)


def brutea(nb):
    relation, reala = 0, 0
    for i in range(0, 2 ** 19):
        s = ''
        a = i
        for j in range(nb * 8):
            a = lfsr(a, ma)
            s += str(a & 1)
        r = calcR(s, key[:nb * 8])
        if relation < r:
            relation, reala = r, i
    print(reala, relation)
    return reala


def brutecd(nb):
    relation, realc, reald = 0, 0, 0
    for i in range(0, 2 ** 6):
        d = i
        for j in range(0, 2 ** 13):
            c = j
            s = ''
            for k in range(nb * 8):
                c = lfsr(c, mc)
                d = lfsr(d, md)
                s += str((c & 1) ^ (d & 1))
            r = calcR(s, key[:nb * 8])
            if relation < r:
                relation, realc, reald = r, j, i
    print(realc, reald, relation)
    return realc, reald


def bruteb(nb, a_, c_, d_):
    for i in range(0, 2 ** 19):
        b = i
        a, c, d = a_, c_, d_
        s = ''
        for j in range(nb * 8):
            a = lfsr(a, ma)
            b = lfsr(b, mb)
            c = lfsr(c, mc)
            d = lfsr(d, md)
            [ao, bo, co, do] = [k & 1 for k in [a, b, c, d]]
            s += str((ao * bo) ^ (bo * co) ^ (bo * do) ^ co ^ do)
        if s == key[:nb * 8]:
            print(i)
            return i


if __name__ == "__main__":
    start_time = time.time()
    print(start_time)
    a = brutea(20)
    c, d = brutecd(20)
    b = bruteb(20, a, c, d)
    print("De1CTF{%s}" % (''.join([hex(i)[2:] for i in [a, b, c, d]])))
    end_time = time.time()
    print("Used time:", end_time - start_time)
# De1CTF{58bb578d5611363f}