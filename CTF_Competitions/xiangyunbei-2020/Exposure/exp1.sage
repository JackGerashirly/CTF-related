n = 140376049134934822153964243403031201922239588054133319056483413311963385321279682186354948441840374124640187894619689719746347334298621083485494086361152915457458004998419817456902929318697902819798254427945343361548635794308362823239150919240307072688623000747781103375481834571274423004856276841225675241863
e = 7621
c = 46735962204857190520476434898881001530665718155698898882603422023484998388668858692912250418134186095459060506275961050676051693220280588047233628259880712415593039977585805890920089318643002597837000049626154900908543384761210358835843974072960080857150727010985827690190496793207012355214605393036388807616
pdp = 1153696846823715458342658568392537778171840014923745253759529432977932183322553944430236879985
d_h = pdp << 200
p_h = e * d_h - 1
#print(p_h)
PR.<x> = PolynomialRing(Zmod(n))
f = x + p_h
x0 = f.small_roots(X=2^214, beta=0.4)[0]  # find root < 2^kbits with factor >= n^0.4
x0 = int(x0)
"""
print(x0.bit_length())
p = p_h - x0
for i in range(1,e+1):
    if p % e == 0:
        print(p//e)
"""
d0 = 0
for k in range(e):
    if (x0 - k) % e == 0:
        d0 = (x0 - k) // e
        print(d0)
        print(d0.nbits())
dp = d0 + d_h
print(dp)
print(dp.nbits())


