from Crypto.Util.number import long_to_bytes
import gmpy2

def gcd(a, b):
	if b == 0:
		return a, 0
	a, b = gcd(b, a % b)
	return a, b

c = 169169912654178
c_1 = 128509160179202
c_2 = 518818742414340
c_3 = 358553002064450

dc_1 = c_1 ** 2 - c_2
dc_2 = c_1 ** 3 - c_3
n = gcd(dc_1, dc_2)[0] / 2
# print(n) # check pass

n.factor()
p = 18195301
q = 28977097
phi = (p - 1) * (q - 1)

e = discrete_log(Mod(c_1, n), Mod(2, n))
# print(e)  # check pass

# print(gcd(e, phi)[0])  # check pass
d = gmpy2.invert(e, phi)
m = pow(c, d, n)
print(long_to_bytes(m))

