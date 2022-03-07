flag="wctf2020{"
part1 = 1
for i in range(1, 2021):
    part1 *= i
part1 = str(hex(int(str(part1)[:8])))[2:]
print part1
flag += part1 + '-'

part2 = pow(520, 1314) + pow(2333, 666)
part2 = str(hex(int(str(part2)[:8])))[2:]
print part2
flag += part2 + '-'


x = 80538738812075974
y = 80435758145817515
z = 12602123297335631
sum = x + y + z
part3 = str(hex(int(str(abs(sum))[:8])))[2:]
print part3
flag += part3 + '-'

_1 = 520
_2 = 1314
part4 = str(hex(int(str(_1 * _2))))[2:]
print part4
flag += part4 + '}'

print flag
