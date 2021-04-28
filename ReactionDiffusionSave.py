# libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import sys
import argparse

## import functions
from RDfns import * # bad practise?
    
## take optional arguments
parser = argparse.ArgumentParser(
    description = "Reaction Diffusion Simulation"
)

## optional arguments. 
parser.add_argument('-n', '--n_sim', help = "number of simulations", type = int)
parser.add_argument('-N', '--N', help = "grid size (N x N)", type = int)
parser.add_argument('-t', '--t', help = "time between each sim", type = float)
args = parser.parse_args()

## if they are not overwritten
## this is terrible obviously. 
if args.n_sim == None: 
    n_sim = 100
else: 
    n_sim = args.n_sim
    
if args.t == None: 
    t = 1
else: 
    t = args.t 

if args.N == None: 
    N = 100
else: 
    N = args.N

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
A, B = starting_mat2(N = N)

# run simulations 
ims = update_n2(A, B, laplace_kernel, t = t, n_sim = n_sim, N = N)

# show animation
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                repeat_delay=300)

writervideo = animation.FFMpegWriter(fps=20)
ani.save(filename = "anims/test3.mp4", writer=writervideo)

# plt show
#plt.show()
