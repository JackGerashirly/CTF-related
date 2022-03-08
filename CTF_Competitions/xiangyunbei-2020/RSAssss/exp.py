# -*- coding:utf-8 -*-
# Fermat Method: Used in two close-gap integers
from gmpy2 import *


def fermat(n):
    a = isqrt_rem(n)[0] + 1
    b = a ** 2 - n
    while 1:
        q = isqrt_rem(b)
        if q[1] == 0:
            fac = a - q[0]
            p = n / fac
            return fac, p
        a += 1
        b = a ** 2 - n


n = 8030860507195481656424331455231443135773524476536419534745106637165762909478292141556846892146553555609301914884176422322286739546193682236355823149096731058044933046552926707682168435727800175783373045726692093694148718521610590523718813096895883533245331244650675812406540694948121258394822022998773233400623162137949381772195351339548977422564546054188918542382088471666795842185019002025083543162991739309935972705871943787733784491735500905013651061284020447578230135075211268405413254368439549259917312445348808412659422810647972872286215701325216318641985498202349281374905892279894612835009186944143298761257
t1 = 89615068527538836315602124154008300286636934599617334867509053076622715365809371740037316558871796433906844464070995869293654082577887578197182408045172781798703173650574737644914515591522256758848089955578713458715234536664415216526830967831862301518636586702212189087959136509334102772855657664091570630079
t2 = 89615068527538836315602124154008300286636934599617334867509053076622715365809371740037316558871796433906844464070995869293654082577887578197182408045175035339285085728002838220314068474670975228778464240088084331807420720121364486765011169669747553393661650912114228227308579940164269877101973728452252879383
print(t1)
print(t2)
# t = (t1 - t2) + (t1 + t2)
# print(gcd(t,n))

"""
print('n =', n)
print('[+]Factorising n...\n')
print(fermat(n), '\n')
print('[!]Done!\n')
"""