# packages
import matplotlib.pyplot as plt
import numpy as np 

# set up figure
fig = plt.figure()

# set up axis 
# this weird thing..
ax = plt.axes(xlim=(-0.5, 99.5), ylim=(-0.5, 99.5))
a=np.random.random((100,100))
im=plt.imshow(a,interpolation='none')
# initialization function: plot the background of each frame
def init():
    im.set_data(np.random.random((100, 100)))
    return [im]

# animation function.  This is called sequentially
def animate(i):
    a=im.get_array()
    a=a*np.exp(-0.001*i)    # exponential decay of the values
    im.set_array(a)
    return [im]

# together 
def run(N = 100): 
    init() 
    for i in range(N): 
        print(i)
        j = i/100
        animate(j)

run()