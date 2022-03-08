

# This file was *autogenerated* from the file renqingxingshi.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_518818742414340 = Integer(518818742414340); _sage_const_28977097 = Integer(28977097); _sage_const_358553002064450 = Integer(358553002064450); _sage_const_128509160179202 = Integer(128509160179202); _sage_const_18195301 = Integer(18195301); _sage_const_169169912654178 = Integer(169169912654178)
from Crypto.Util.number import long_to_bytes
import gmpy2

def gcd(a, b):
	if b == _sage_const_0 :
		return a, _sage_const_0 
	a, b = gcd(b, a % b)
	return a, b

c = _sage_const_169169912654178 
c_1 = _sage_const_128509160179202 
c_2 = _sage_const_518818742414340 
c_3 = _sage_const_358553002064450 

dc_1 = c_1 ** _sage_const_2  - c_2
dc_2 = c_1 ** _sage_const_3  - c_3
n = gcd(dc_1, dc_2)[_sage_const_0 ] / _sage_const_2 
# print(n) # check pass

n.factor()
p = _sage_const_18195301 
q = _sage_const_28977097 
phi = (p - _sage_const_1 ) * (q - _sage_const_1 )

e = discrete_log(Mod(c_1, n), Mod(_sage_const_2 , n))
# print(e)  # check pass

# print(gcd(e, phi)[0])  # check pass
d = gmpy2.invert(e, phi)
m = pow(c, d, n)
print(long_to_bytes(m))

