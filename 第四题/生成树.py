import numpy as np
# 先输入矩阵A
A = np.array([[0,1,0,1,1,0],
              [1,0,1,0,1,1],
              [0,1,0,0,1,1],
              [1,0,0,0,1,0],
              [1,1,1,1,0,1],
              [0,1,1,0,1,0]], dtype=int)
AD = np.sum(A, axis=0)
# print(AD)
L = np.diag(AD) - A
# print(L)
E, V = np.linalg.eig(L)
L1 = L[:len(L) - 1, :len(L) - 1]
E1, V1 = np.linalg.eig(L1)
s = 1
for i in range(len(E1)):
    s = s * E1[i]
print(s)
