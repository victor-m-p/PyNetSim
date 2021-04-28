# import functions
import numpy as np
import matplotlib.pyplot as plt
import math
from tqdm import tqdm

# generate starting matrices
def starting_mat(N = 100): 
    
    # first some zeros & ones
    A = np.ones((N, N))
    B = np.zeros((N, N))

    # initialize some B 
    B[math.floor(N/2):math.floor((N/2)+2), math.floor(N/2):math.floor((N/2)+2)] = 1

    # the same for A
    # not sure about this but conceptually it makes sense. 
    A[math.floor(N/2):math.floor((N/2)+2), math.floor(N/2):math.floor((N/2)+2)] = 0

    # return them both
    return A, B

# this starting matrice is much more crazy..
def starting_mat2(N = 100): 
    
    # first some zeros & ones
    A = np.ones((N, N))
    B = np.zeros((N, N))
    
    # B
    B[math.floor(N/1.5):math.floor((N/1.5)+1), math.floor(N/1.5):math.floor((N/1.5)+1)] = 1
    B[math.floor(N/3):math.floor((N/3)+1), math.floor(N/3):math.floor((N/3)+1)] = 1
    B[math.floor(N/1.5):math.floor((N/1.5)+1), math.floor(N/3):math.floor((N/3)+1)] = 1
    B[math.floor(N/3):math.floor((N/3)+1), math.floor(N/1.5):math.floor((N/1.5)+1)] = 1
    
    # A 
    A[math.floor(N/1.5):math.floor((N/1.5)+1), math.floor(N/1.5):math.floor((N/1.5)+1)] = 1
    A[math.floor(N/3):math.floor((N/3)+1), math.floor(N/3):math.floor((N/3)+1)] = 1
    A[math.floor(N/1.5):math.floor((N/1.5)+1), math.floor(N/3):math.floor((N/3)+1)] = 1
    A[math.floor(N/3):math.floor((N/3)+1), math.floor(N/1.5):math.floor((N/1.5)+1)] = 1
    
    return A, B
        
# compute laplacian
def laplacian(d, laplace_kernel, N = 100): 
    # copy of the matrix
    d_cp = d.copy()
    for i in range(N-2): #rows
        for j in range(N-2): #cols
            
            # just making it easier in my head. 
            x = i+1
            y = j+1 

            # find the 3x3 subset of the data around (x, y) point
            d_sub = d[x-1:x+2, y-1:y+2] # has to be d. 
            
            # convolution with laplacian.
            d_cp[x, y] = np.sum(d_sub*laplace_kernel) # pretty sure it is not +=
    
    # fix the border (not the smartest..)
    for i in range(N-1): 
        d_cp[i, 0] = d_cp[i, 1]
        d_cp[i, N-1] = d_cp[i, N-2]
    for j in range(N):
        d_cp[0, j] = d_cp[1, j]
        d_cp[N-1, j] = d_cp[N-2, j]

    # return d
    return(d_cp)

## functions for updating A & B 
def update_A(A, B, laplace_kernel, D_A = 1, f = 0.055, t = 1, N = 100):
    A_lap = laplacian(A, laplace_kernel, N)
    #first = D_A*A_lap
    #second = A*B*B 
    #third = f*(1-A)
    A_new = A + (D_A * A_lap - (A*B*B) + f*(1 - A)) * t
    #print(f"first_A = {np.round(first, 3)}, \nsecond_A = {np.round(second, 3)}, \nthird_A = {np.round(third, 3)}, \na_old = {np.round(A, 3)} \na_lap = {np.round(A_lap, 3)} \na_new = {np.round(A_new, 3)}")
    return A_new

def update_B(A, B, laplace_kernel, D_B = 0.5, f = 0.055, k = 0.062, t = 1, N = 100):
    B_lap = laplacian(B, laplace_kernel, N) 
    #first = D_B*B_lap
    #second = A*B*B 
    #third = (k+f)*B
    B_new = B + (D_B * B_lap + (A*B*B) - (k+f)*B) * t
    #print(f"first_B = {first}, \nsecond_B = {second}, \nthird_B = {third}, \nb_old = {B} \nb_lap = {B_lap} \nb_new = {B_new}")
    return B_new

## run one time-step 
def update_both(A, B, laplace_kernel, D_A = 1, D_B = 0.5, f = 0.055, k = 0.062, t = 1, N = 100):
    A_new = update_A(A, B, laplace_kernel, D_A, f, t, N)
    B_new = update_B(A, B, laplace_kernel, D_B, f, k, t, N)
    return (A_new, B_new)

## run the simulation for n time-steps
## not sure how this incorporates at the moment. 
def update_n(A, B, laplace_kernel, D_A = 1, D_B = 0.5, f = 0.055, k = 0.062, t = 1, n_sim = 100, N = 100): 
    # empty list holding images.
    fig, ax = plt.subplots()
    ims = []
    for i in tqdm(range(n_sim)):
        print(i)
        A, B = update_both(A, B, laplace_kernel, D_A, D_B, f, k, t, N)
        im = ax.imshow(B)
        ims.append([im])

    return ims 

## try to plot the relative & B.
def update_n2(A, B, laplace_kernel, D_A = 1, D_B = 0.5, f = 0.055, k = 0.062, t = 1, n_sim = 100, N = 100): 
    # empty list holding images.
    fig, ax = plt.subplots()
    ims = []
    for i in tqdm(range(n_sim)):
        A, B = update_both(A, B, laplace_kernel, D_A, D_B, f, k, t, N)
        relative = np.divide(A+0.001, B+0.001) # add small constant to avoid division error. 
        im1 = ax.imshow(relative)
        #im2 = ax.imshow(B)
        ims.append([im1])

    return ims 

'''
## update image function
def updatefig(*args): 
    global A, B
    A, B = update_both(A, B)
    im.set_array(B)
    return im, # not sure about this comma. 
'''