import matplotlib.pyplot as plt
#绘制一个平方的折线图  并添加一些细节
input = [1,2,3,4]
squares = [1,4,9,16]

plt.figure(figsize=(15,15))
plt.subplot(2,2,1)
plt.plot(input,squares,linewidth = 5)  #线条粗细
#设置图标标题 并给坐标轴加上标签
plt.title("squares numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("square value",fontsize = 14)
#设置刻度标记大小
plt.tick_params(axis = "both",labelsize = 14)

plt.subplot(2,2,2)
plt.scatter(2, 4, s=200)  #s设置了点的大小
# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.subplot(2,2,3)
x_values = list(range(1,100))  #用列表表示连续的数
y_values = [x **2 for x in x_values]
plt.scatter(x_values, y_values,edgecolors= 'none',s=10,c=(0.8, 0, 0.8)) # edgcolors 点的轮廓  c为rgb设置颜色
plt.axis([0,100,0,10000])  #设置坐标轴的取值范围

plt.subplot(2,2,4)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,edgecolor='none', s=40) # 对y_values使用颜色映射
plt.show()
#第一个实参指定要以什么样的文件名保存图表，这个文件将存储到 scatter_squares.py 所在的目录中；第二个实参指定将图表多余的空白区域裁剪掉。如果要保留图表周围多余的空白区域，可省略这个实参。
plt.savefig("work1.png")
