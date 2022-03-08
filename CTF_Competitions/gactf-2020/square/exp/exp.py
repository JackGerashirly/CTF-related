# We can get something like pell equation: (4*y+3)^2 - 48*x^2 == 1
# Write it into x^2 - 48*y^2 == 1

"""
for i in range(10000):
    for j in range(10000):
        if i ** 2 - 48 * j ** 2 == 1:
            print(i,j)

Output:
1 0
7 1
97 14
1351 195

Formula: 	
a(m) = 14a(m-1) - a(m-2)
"""

import gmpy2

a = [1,7,97,1351]
x = [1,7,97,1351]
y = [0,1,14,195]
while len(x) <  120:
    ta = 14 * a[-1] - a[-2]
    a.append(ta)
    if ta % 4 == 3:
        x.append(ta)

for i in range(4,len(x)):
    y.append(gmpy2.iroot((x[i]**2-1) // 48,2)[0])

for i in range(4,120):
    x[i] = (x[i] - 3) // 4
x = x[4:]
y = y[4:]


for i,j in zip(x,y):
    print(i,j)


# check pass
for i,j in zip(x,y):
    assert((4*i+3)**2 - 48*j**2 == 1)


