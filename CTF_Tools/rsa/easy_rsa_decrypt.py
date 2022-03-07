# -*-coding: utf-8 -*-
import gmpy2
import libnum


def rsa_decrypt(e, c, p, q):  # e 为公钥，c 为密文，p，q 为大质数，以上参数皆为10进制
    phi = (p - 1) * (q - 1)
    n = p * q
    try:
        d = gmpy2.invert(e, phi)  # 求e模phi的逆
        return pow(c, d, n)
    except Exception as e:
        print "e and phi are not coprime! "
        raise e


# 写入各参数
e = 65537
c = 14874271064669918581178066047207495551570421575260298116038863877424499500626920855863261194264169850678206604144314318171829367575688726593323863145664241189167820996601561389159819873734368810449011761054668595565217970516125181240869998009561140277444653698278073509852288720276008438965069627886972839146199102497874818473454932012374251932864118784065064885987416408142362577322906063320726241313252172382519793691513360909796645028353257317044086708114163313328952830378067342164675055195428728335222242094290731292113709866489975077052604333805889421889967835433026770417624703011718120347415460385182429795735  # 若密文为16进制，则使用c = int(c1, 16)将其转为10进制
p = 127353412948873836906687778206509910878775314988106052080998527001224905757226684812828764973002447453109594922446553339420598206561385151430457829996205647622747518251616965320363658027264186719678664334278218049211583365254398026548102259795044636599208243773041401637282792878778039534749858540041527364997
q = 172752312328592624820203740864759781695743799410666998265780217233395427110343557002559899380499347155322034504624186688200558644773452887313745765534949614397043804397334009458504041075763421353984745778272625061206929646265927538923171329777117876902761816678106270946112638108943916135772001528126188051463

m = rsa_decrypt(e, c, p, q)
print m
print ('%x' % m).decode('hex')  # 10 进制转 chr
# print rsa_decrypt(65537, 242094131279916, 23781539, 13574881)  # 脚本检验样本