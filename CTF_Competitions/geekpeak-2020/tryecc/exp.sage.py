

# This file was *autogenerated* from the file exp.sage
from sage.all_cmdline import *   # import sage library

_sage_const_598756982846857855564861803797067906933452532971372536192231 = Integer(598756982846857855564861803797067906933452532971372536192231); _sage_const_773793889124783574343562335367 = Integer(773793889124783574343562335367); _sage_const_773793889124783574343613279393 = Integer(773793889124783574343613279393); _sage_const_4480960863875584511148612202888184984874434295853921 = Integer(4480960863875584511148612202888184984874434295853921); _sage_const_40868726519566019162794925971370501749760105301423309229554 = Integer(40868726519566019162794925971370501749760105301423309229554); _sage_const_54687980868371628310908123178978977864897123871328723 = Integer(54687980868371628310908123178978977864897123871328723); _sage_const_235149117685317066108245267690004572936544028030457002179126 = Integer(235149117685317066108245267690004572936544028030457002179126); _sage_const_1289371238921298371232163781261298731812137628190 = Integer(1289371238921298371232163781261298731812137628190); _sage_const_230807308713660443214609900462802224133677339138938919914236 = Integer(230807308713660443214609900462802224133677339138938919914236); _sage_const_15979270783196203822523802015845150885928738960540101206481 = Integer(15979270783196203822523802015845150885928738960540101206481); _sage_const_48539794908526618490272854315619275063139157075919926757183 = Integer(48539794908526618490272854315619275063139157075919926757183); _sage_const_253317587580758121061061480314672531383057603048054780326781 = Integer(253317587580758121061061480314672531383057603048054780326781); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3)
from Crypto.Util.number import long_to_bytes
N = _sage_const_598756982846857855564861803797067906933452532971372536192231 
p = _sage_const_773793889124783574343562335367 
q = _sage_const_773793889124783574343613279393 
C = _sage_const_4480960863875584511148612202888184984874434295853921 
P1x = _sage_const_40868726519566019162794925971370501749760105301423309229554 
P1y = _sage_const_54687980868371628310908123178978977864897123871328723 
P2x = _sage_const_235149117685317066108245267690004572936544028030457002179126 
P2y = _sage_const_1289371238921298371232163781261298731812137628190 
P3x = _sage_const_230807308713660443214609900462802224133677339138938919914236 
P3y = _sage_const_15979270783196203822523802015845150885928738960540101206481 
P4x = _sage_const_48539794908526618490272854315619275063139157075919926757183 
P4y = _sage_const_253317587580758121061061480314672531383057603048054780326781 


F = IntegerModRing(N)
A = ((P1y**_sage_const_2  - C - P1x**_sage_const_3 ) * inverse_mod(P1x,N)) % N
B = (P2y ** _sage_const_2  - P2x ** _sage_const_3  - A * P2x) % N

Eq = EllipticCurve(GF(q), [A, B])
Ep =  EllipticCurve(GF(p), [A, B])
P2q = Eq(P2x,P2y)
P2p = Ep(P2x,P2y)
P3q = Eq(P3x,P3y)
P3p = Ep(P3x,P3y)
P4q = Eq(P4x,P4y)
P4p = Ep(P4x,P4y)
oq = Eq.order()
op = Ep.order()
m1q = discrete_log(P3q,P2q,oq,operation='+')
m1p = discrete_log(P3p,P2p,op,operation='+')
m1 = CRT([m1p,m1q],[op,int(oq)//gcd(op,oq)]) # modulus are pairwise coprime
m2q = discrete_log(P4q,P2q,oq,operation='+')
m2p = discrete_log(P4p,P2p,op,operation='+')
m2 = CRT([m2p,m2q],[op,int(oq)//gcd(op,oq)]) # modulus are pairwise coprime
print(long_to_bytes(m1) + long_to_bytes(m2))





