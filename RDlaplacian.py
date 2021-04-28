# numpy
import numpy as np

# values for kernel
w_c = -1
w_a = 0.2 
w_d = 0.05

# kernel 
lap_kernel = np.asarray([[w_d, w_a, w_d], [w_a, w_c, w_a], [w_d, w_a, w_d]])

# test data
dimension = 10
d = np.zeros((dimension, dimension))
d[5:9, 5:9] = 1 # ones in the middle

# now apply the kernel 
## for now they just die at the edges
for i in range(dimension-2): #rows
    for j in range(dimension-2): #cols

        # just making it easier in my head. 
        x = i+1
        y = j+1 

        # find the 3x3 subset of the data around (x, y) point
        d_sub = d[x-1:x+2, y-1:y+2]

        # convolution with laplacian.
        d[x, y] += np.sum(d_sub*lap_kernel)

## turn it into a function
def laplacian(d, laplace_kernel, dimensions): 
    for i in range(dimension-2): #rows
        for j in range(dimension-2): #cols

            # just making it easier in my head. 
            x = i+1
            y = j+1 

            # find the 3x3 subset of the data around (x, y) point
            d_sub = d[x-1:x+2, y-1:y+2]

            # convolution with laplacian.
            d[x, y] += np.sum(d_sub*lap_kernel)

            # return d
            return(d)
