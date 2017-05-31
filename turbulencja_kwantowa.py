import numpy as np
A = np.load("supplies.npy")

import matplotlib.pyplot as plt
nz=400
figure, axes = plt.subplots(figsize=(12,8))
M = np.abs(A)**2
IM = axes.imshow(M[:,:,0], vmin = np.min(M), vmax = np.max(M))
plt.colorbar(IM)
axes.set_title(nz)

def funkcja(nz):
    IM.set_array(M[:,:,nz])
    axes.set_title(nz)
    return IM, axes

import matplotlib.animation as anim

animation = anim.FuncAnimation(figure, funkcja, interval = 10, frames = 1000)
plt.show()