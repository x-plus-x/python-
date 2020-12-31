import matplotlib.pyplot as plt

x_values = list(range(0,5000))
y_values = [x**3 for x in x_values]


plt.scatter(x_values,y_values,c = y_values,s = 10,cmap = plt.cm.Blues)

plt.show()