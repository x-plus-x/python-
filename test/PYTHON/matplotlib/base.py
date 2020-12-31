import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,3,50)
y1 =2*x + 1
y2 = x**2 + 1

#plt.figure(num=3,figsize=(8,5))  # num是figure的号数 size是图像框的大小
#plt.plot(x,y1)

plt.figure(figsize=(10,10))


plt.xlim((-1,2))
plt.ylim((-2,3))

plt.xlabel("im x")
plt.ylabel("im y")

new_ticks = np.linspace(-1,3,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1,1,2],
           [r"$bad$",r"$normal\ \alpha$","good","very good"])
ax = plt.gca()   #gca就是边框
ax.spines['right'].set_color("none")
ax.spines["top"].set_color("none")

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

#ax.spines['bottom'].set_position(('data',-1))
#ax.spines['left'].set_position(('data',0))  #改变坐标轴位置
#legend图例
plt.plot(x,y1,color = "red",linewidth = 1.0,linestyle = '--',label = "up")
plt.plot(x,y2,label = "down")
plt.legend() #内部有很多属性可以设置，自查

# 标出一个点
x0 = 1
y0 = x0**2 + 1
plt.scatter(x0,y0)
plt.plot([x0,x0],[y0,-2],"k--",lw = 2.5)
plt.annotate(r"$x**2+1=%s$"%y0,xy = (x0,y0),xycoords = 'data',xytext = (+30,-30),textcoords = 'offset points',fontsize = 16,arrowprops =dict(arrowstyle = '->',connectionstyle = 'arc3,rad = .2'   ))


plt.show()
  