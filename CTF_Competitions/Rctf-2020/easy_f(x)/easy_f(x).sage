# import hashlib
# import string
# from pwn import *
# s = remote('124.156.140.90', 2333)

# def proof_of_work():
#     s.recvuntil("sha256(XXXX+")
#     suffix = str(s.recvuntil(") == ", drop=True).strip())
#     print("    [+] suffix: " + suffix)
#     res = str(s.recvuntil(") == ", drop=True).strip())
#     print("    [+] res: " + res)
#     dic = string.printable
#     for i in dic:
#         for j in dic:
#             for k in dic:
#                 for m in dic:
#                     if hashlib.sha256((i + j + k + m + suffix).encode()).hexdigest() == res:
#                         print("  [+] Found!: " + i + j + k + m)
#                         s.sendline(i + j + k + m)

# proof_of_work()
# s.interactive()


m = 1243055066351914891786865057775815469842187182541437624288615942480256198835674131987060379262488689299868215969943827204178453469619138296199214083748506783954942205640566551846697644932689213704687955007945414460024560145150234871


x = []
r = []
with open("output.txt") as f:
    for i in range(520):
        t = f.readline()
        t = t.split(')=')
        x.append(int(t[0][2:]))
        print(t)
        r.append(int(t[1]))
    f.close()
# print(len(x))
# print(len(r))  # check pass
# print(r[1])
# print(x[1]) # check pass
# print(m.bit_length()) # check pass
matris = [[0 for i in range(513)] for j in range(513)]  # check pass
for i in range(513):
    for j in range(513):
        matris[i][j] = pow(x[i], j, m)
# print(len(matris[1]))  # check pass
print("Success")
matris = Matrix(GF(m), matris)
r = Matrix(GF(m), r[:513]).transpose()
res = matris.solve_right(r)
print(res[0])
print(res.nrows())
print(res.ncols())
# RCTF{A_e4siest_sh4mlr_s3cr3t_sh4rIng!!}
