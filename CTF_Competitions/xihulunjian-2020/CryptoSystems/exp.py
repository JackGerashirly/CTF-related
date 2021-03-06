# -*- coding: utf-8 -*-
from gmpy2 import *
import gmpy2
from Crypto.Util.number import long_to_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def continuedfra(x, y):
    cF = []
    while y:
        cF += [x / y]
        x, y = y, x % y
    return cF


def simplify(ctnf):
    numerator = 0
    denominator = 1
    for x in ctnf[::-1]:
        numerator, denominator = denominator, x * denominator + numerator
    return (numerator, denominator)


def calculatefrac(x, y):
    cF = continuedfra(x, y)
    cF = map(simplify, (cF[0:i] for i in range(1, len(cF))))
    return cF


def solve_pq(a, b, c):
    par = isqrt(b * b - 4 * a * c)
    return (-b + par) / (2 * a), (-b - par) / (2 * a)


def wienerattack(e, n):
    for (d, k) in calculatefrac(e, n):
        if k == 0:
            continue
        if (e * d - 1) % k != 0:
            continue
        phi = (e * d - 1) / k
        p, q = solve_pq(1, n - phi + 1, n)
        if p * q == n:
            return abs(int(p)), abs(int(q))
    print('not find!')


n = 24493816160588971749455534346389861269947121809901305744877671102517333076424951483888863597563544011725032585417200878377314372325231470164799594965293350352923195632229495874587039720317200655351788887974047948082357232348155828924230567816817425104960545706688263839042183224681231800805037117758927837949941052360649778743187012198508745207332696876463490071925421229447425456903529626946628855874075846839745388326224970202749994059533831664092151570836853681204646481502222112116971464211748086292930029540995987019610460396057955900244074999111267618452967579699626655472948383601391620012180211885979095636919
e = 3683191938452247871641914583009119792552938079110383367782698429399084083048335018186915282465581498846777124014232879019914546010406868697694661244001972931366227108140590201194336470785929194895915077935083045957890179080332615291089360169761324533970721460473221959270664692795701362942487885620152952927112838769014944652059440137350285198702402612151501564899791870051001152984815689187374906618917967106000628810361686645504356294175173529719443860140795170776862320812544438211122891112138748710073230404456268507750721647637959502454394140328030018450883598342764577147457231373121223878829298942493059211583
c = 5005506188015283858618563146910806063877921793777978994915497795876938512755438407136257676431725794584739591081520092904805015329015078208120428335307568025626961078774464089850298597196144685189876104836723992575488792059316933286283680113304988491073245798629428127361669397770834108716291576117851676329812293116545555063668060753416820927621896648263794070909343393833391190511954243001173709216900016519978222229519537931075964991814352014046683068580265025109108417752977595495011359622930468690758616479580008393165416315936108980879332331515829028922252448286421964886808014893689612307271812468977429977314
p, q = wienerattack(e, n)

assert(p * q == n)
assert(gmpy2.is_prime(p) == True)
assert(gmpy2.is_prime(q) == True)
d = invert(e, (p-1)*(q-1))
rsakey=RSA.importKey(open("./private.pem","r").read())
rsa = PKCS1_OAEP.new(rsakey)
msg=rsa.decrypt(long_to_bytes(c))
print(msg)
"""
In [45]: rsa = RSA.construct([n,e,d])                                                                                          

In [46]: rsa.exportKey()                                                                                                       
Out[46]: b'-----BEGIN RSA PRIVATE KEY-----\nMIIEXgIBAAKCAQEAwgdFIj/1uUss2EEhZvcoiiHyGH4aQhRTkYyrA8gCU0USM+sb\n3CNjdEIoqoaUqMLLyDP4Dd9AgxpokBsjC4Pz8P7Uty0LlCteld7ayNzABHoq+5DI\nHtctOtSbcvyL0NMWfd2qarUWfAWN82rxkLIWCFu9nWIfm9I6CT5OPZzDh7YnTywz\nnIjhstkIrLM/TiDmR6vuBxSjzORkbolilLeBA9zJpNt+1oEWTG5sx/0zR24XSmxw\ncDeyUEkTZfnw63auq6B9svZi2IBIr5jIjHbGcQ25ZY1J/KDK8fXNmdwH8YhDK0j4\nVXEWitEPyCS3toK61sql0S/28EySeGtzirGbtwKCAQAdLS8fFz+BzzaP7AbUDUf9\nkvhhXBLuwUFo8ohCeVK4z1pTj3C6M0G2oXOugDdalrDThNlyKxkUn3iUc3Xgoz31\n5pPtq9Xk1Ez/qeUl6gFPP6SZtfeymyGdkLiNpVquOghjczjXvtBW467Fdb5Wu95T\nSzVaLndX23rsqW541n8hUwt8PsJKxh+bR0qygyIN2VRRNdBlpyTOL49E4y5GDu9f\nmVgAnFivWVGT135ywl8MsBUFuZPBNTKLEbUA3KvJVckXf4Od0ENYbiWjEzXn1UN9\nyebNbU6+yyk34WAmwnkuF0X0Tu1UEb6qtV7QkF25GYy9QxERvodGL0Y2njHRpGE/\nAkAh+KKpFWG886QHeF2pJ1y02WI/ujRcTwcW8ua4XraWCV8QtzAJCoxhIAJ6XDOO\nIu3YQ1lIecqwAV2pbZNMV38/AoGBAOkmqYadbPNvB9gWhZ7iAMgd2w804HJScDwq\n+SNSv7XllNnh0CJDbY19G3nsfLQy+R2JqzCCdFmIsCJtBHRIvApMykPnsgG5Qfwj\n/7XK77LGzb8P7X3mrK4eQrELRjpY8h0+YqMDxJ5OYsr8oVj6rD3QMfVu53XhgqoN\nHD56lYD9AoGBANULF4Vk4SHNib8CbUL5UtBPEYiD7ePRUFvXmMLEA5MgtOfshpmp\nBiSiXHW4abGnSO9pXUv0v+TW6VYyYbVDFmWH87vni6l6+QnUR6qKlegfBxrVL29y\ncqFaJz+lt/Zo5QPwvr50mgjQ6hOtD+4SAVgk6a059VKyuTho56XcojfDAkAh+KKp\nFWG886QHeF2pJ1y02WI/ujRcTwcW8ua4XraWCV8QtzAJCoxhIAJ6XDOOIu3YQ1lI\necqwAV2pbZNMV38/AkAh+KKpFWG886QHeF2pJ1y02WI/ujRcTwcW8ua4XraWCV8Q\ntzAJCoxhIAJ6XDOOIu3YQ1lIecqwAV2pbZNMV38/AoGBAJ/8/LizZOrBACJ8R1ma\nUWAvuuxI7lGac2B+/A/EcwBJfOT/qLCPpvFhA0Qje1HqlNSXc9e/FGt1UwxZkJBJ\nJNGhlKRKaB0RJgJW5dA1jfyYU8xpPsDxfdDzLf2y167IbfqNNmL7ZF8IHj5+hPsB\n0oVAN0gvoLxcOM2qMOXIt6aM\n-----END RSA PRIVATE KEY-----'

In [47]: output = rsa.exportKey()                                                                                              

In [48]: f=open("private.pem","w") 
    ...: f.write(output.decode()) 
    ...: f.close()            
"""
