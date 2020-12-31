# sudo pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple tensorflow
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1,50)
y = x^2 + 1
plt.plot(x,y)
plt.show()

