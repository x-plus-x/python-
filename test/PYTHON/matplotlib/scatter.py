import numpy as np
import matplotlib.pyplot as plt

n = 12 
X = np.arange(n)
print(X)

Y1 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)  
Y2 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)
print(Y1)

plt.bar(X,+Y1)
plt.bar(X,-Y2)

for x,y in zip(X,Y1):
    plt.text(x,y,"%.2f"%y,ha = 'center',va = 'bottom')

plt.xlim(-.5,n)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())

plt.figure()
data = np.random.random(size=(3,3))
print(data)
plt.imshow(data,interpolation="nearest",cmap = 'bone',origin='upper')
plt.colorbar(shrink = 0.9)
plt.show()