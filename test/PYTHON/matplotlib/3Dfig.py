import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
#Value XY
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
r = np.sqrt(X**2+ Y**2)
Z = np.sin(r)

x0 = 1
y0 = 1
r0 = np.sqrt(X**2+ Y**2)
z0 = np.sin(r0)
ax.scatter(x0,y0,z0,color = 'k',marker = 'o')

ax.plot_surface(X,Y,Z,rstride =1,cstride = 3,cmap = plt.get_cmap("rainbow"))
ax.contourf(X,Y,Z,zdir = 'z',offset = -2,cmap = "rainbow")
ax.set_zlim(-2,2)
plt.show()