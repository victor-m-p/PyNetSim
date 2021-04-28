import numpy as np 
import matplotlib.pyplot as plt 

N = 5
A = np.ones((N, N))
A[1,1] = 2
A[1,2] = 2
A[1,3] = 2
A[2,1] = 2
A[2,2] = 2
A[2,3] = 2
A[3,1] = 2
A[3,2] = 2
A[3,3] = 2
A

for i in range(N-1): 
    A[i, 0] = A[i, 1]
    A[i, N-1] = A[i, N-2]
for j in range(N):
    A[0, j] = A[1, j]
    A[N-1, j] = [N-2, j]

A
