import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

## import functions
from RDfns import * # bad practise?

## initialize fig
fig, ax = plt.subplots()

## https://www.karlsims.com/rd.html

#### hyper-parameters
D_A = 1 # diffusion for A
D_B = .5 # diffusion for B 

## f & k vary for different patterns 
f = .055 # feed (adding A)
k = .062 # kill (removing B)

## laplacian: https://www.youtube.com/watch?v=R6kHZX7B2UA
## laplacian/kernel: https://homepages.inf.ed.ac.uk/rbf/HIPR2/log.htm

#### initialize
## grid initialized with A = 1, B = 0 & small area B = 1
## Laplacian with 3x3 convolution with: 
## --> center weight: -1
## --> adjacent neighbors: .2
## --> diagonals = .05

# values for kernel
w_c = -1
w_a = 0.2 
w_d = 0.05

# kernel 
laplace_kernel = np.asarray([[w_d, w_a, w_d], [w_a, w_c, w_a], [w_d, w_a, w_d]])

# starting matrices
A, B = starting_mat()

# run simulations 
ims = update_n(A, B, laplace_kernel)

# show animation
ani = animation.ArtistAnimation(fig, ims, interval=200, blit=True, repeat_delay=1000)

# show the plot
plt.show()