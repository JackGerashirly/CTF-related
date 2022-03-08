from Crypto.Util.number import long_to_bytes

n = 0x8bc8479ebf10dc1a4c24d6dfd6effd0437969eebf67654bc5c495bf2577f15226c15b9793ce9363c5986c485c2932fc7e7e6daac8dc108cca6d1b3850353fa2f
e = 0x3
c = 0x87c05b7868cf54a58e19fe7a969a0213101f045e2afbf7547534564e918b62caa8187c773a8168ff464b20c28ce0e33383a600351883bb0938b2ecf0c45d59f3
mbar = 0x666c6167206973203a3739306666373532653338393838613532000000000000000000000000000000
kbits = 120

PR.<x> = PolynomialRing(Zmod(n))
f = (mbar + x)^e - c

x0 = f.small_roots(X=2^kbits, beta=1)[0]  # find root < 2^kbits with factor = n
print("m:", mbar + x0)
m = mbar + x0
print(long_to_bytes(m))