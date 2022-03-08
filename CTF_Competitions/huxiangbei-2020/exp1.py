from Crypto.Util.number import long_to_bytes 
from pylfsr import LFSR
res = []
for i in range(16): 
    iv = [int(j) for j in bin(i)[2:].zfill(4)]
    # print(iv) check pass  
    L = LFSR(fpoly=[4,3],initstate=iv,verbose=False) 
    data = L.runFullCycle() 
    k = b'' 
    for _ in range(len(data)): 
        a = b'' 
        for __ in range(8):
            a += str(L.next()).encode() 
        k += long_to_bytes(int(a,2))
    res.append(k)
    print(k)
ele = []
for i in res:
    for j in range(len(i)):
        if i[j] not in ele:
            ele.append(i[j])
print(ele)
# key = [77, 19, 154, 175, 137, 38, 196]
# ele = [0, 19, 94, 38, 188, 77, 120, 154, 241, 53, 226, 107, 196, 215, 137, 175]
# cipher = enc1[770:]
# candidate: [94, 188, 120, 241, 53, 226, 107, 215]
