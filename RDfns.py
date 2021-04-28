# import functions
import numpy as np
import matplotlib.pyplot as plt
import math

# generate starting matrices
def starting_mat(N = 100): 
    
    # first some zeros 
    A = np.ones((N, N))
    B = np.zeros((N, N))

    # then some tweaks 
    B[math.floor(N/10):math.floor(N/6), math.floor(N/10):math.floor(N/7)] = 1
    #B[math.floor(N/3):math.floor(N/2), math.floor(N/3):math.floor(N/2)] = 1

    # return them both
    return A, B
    

# compute laplacian
def laplacian(d, laplace_kernel, N = 100): 
    for i in range(N-2): #rows
        for j in range(N-2): #cols

            # just making it easier in my head. 
            x = i+1
            y = j+1 

            # find the 3x3 subset of the data around (x, y) point
            d_sub = d[x-1:x+2, y-1:y+2]

            # convolution with laplacian.
            d[x, y] += np.sum(d_sub*laplace_kernel)

    # return d
    return(d)

## functions for updating A & B 
def update_A(A, B, laplace_kernel, D_A = 1, f = 0.055, t = 1, N = 100):
    A_lap = laplacian(A, laplace_kernel, N)
    A_new = A + (D_A * A_lap - A*B**2 + f*(1 - A)) * t
    return A_new

def update_B(A, B, laplace_kernel, D_B = 0.5, f = 0.055, k = 0.062, t = 1, N = 100):
    B_lap = laplacian(B, laplace_kernel, N) 
    B_new = B + (D_B * B_lap + A*B*B**2 - (k+f)*B) * t
    return B_new

## run one time-step 
def update_both(A, B, laplace_kernel, D_A = 1, D_B = 0.5, f = 0.055, k = 0.062, t = 1, N = 100):
    A_new = update_A(A, B, laplace_kernel, D_A, f, t, N)
    B_new = update_B(A, B, laplace_kernel, D_B, f, k, t, N)
    return (A_new, B_new)

## run the simulation for n time-steps
## not sure how this incorporates at the moment. 
def update_n(A, B, laplace_kernel, D_A = 1, D_B = 0.5, f = 0.055, k = 0.062, t = 1, n_sim = 200, N = 100): 
    # empty list holding images.
    fig, ax = plt.subplots()
    ims = []
    for i in range(n_sim):
        A, B = update_both(A, B, laplace_kernel, D_A, D_B, f, k, t, N)
        im = ax.imshow(B, animated=True)
        if i == 0:
            ax.imshow(B)
        ims.append([im])

    return ims 

## update image function
def updatefig(*args): 
    global A, B
    A, B = update_both(A, B)
    im.set_array(B)
    return im, # not sure about this comma. 