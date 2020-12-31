from random import choice
import matplotlib.pyplot as plt
def get_step(direction,distance):
    step = direction * distance
    return step

class RandomWalk():
    '''生成一个随机漫步的类'''
    def __init__(self,num_points = 5000):
        '''初始化随机漫步的属性'''
        self.num_points = num_points
        # 所有随机步 都始于（0,0）
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        while len(self.x_values) <= self.num_points:
            #决定前进方向以及沿着这个方向前进的距离
            x_direction = choice([1,-1])  # 方向 1 或 -1
            x_distance = choice([0,1,2,3,4])  # 步幅
            x_step = get_step(x_direction,x_distance)
              
            y_direction = choice([-1,1])  #choice 的功能就是随机选择一个列表中的值
            y_distance = choice([0,1,2,3,4])
            y_step = get_step(y_direction,y_distance)
            # 拒绝原地踏步
            if x_step and y_step == 0:
                continue
            #计算下一个点的x 和 y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
def main():
    flag = True
    while flag:
        rw = RandomWalk(5000)
        rw.fill_walk()
        plt.figure(figsize=(15,15))
        plt.scatter(0,0,c = 'red',s = 50)# 标出起点
        plt.plot(rw.x_values,rw.y_values,linewidth = 1)  #画线用plot  画点用scatter 
        plt.scatter(rw.x_values[-1],rw.y_values[-1],c = 'red',s = 10) #标出终点
        #隐藏坐标轴
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.show()
        keep_running = raw_input("make another walk?:")
        if keep_running == 'n':
            flag = False
if __name__ == "__main__":
    main()
         

