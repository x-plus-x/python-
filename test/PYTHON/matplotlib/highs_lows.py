import csv
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime  # 写日期用的
import matplotlib.dates as mdate

#获取数据 并存储
def get_data(filename):
    with open(filename) as f:  #打开文件
        reader =  csv.reader(f)     #将文件作为实参传递给csv.reader
        next(reader)  #返回文件的下一行
        '''
        for index,colum_header in enumerate(header_row):  #函数 enumerate可以获取每个元素的索引和值
            print(index,colum_header)
        '''  
        dates,highs,lows = [],[],[] #存储最高温度
        for row in reader:
            try:
                date = datetime.strptime(row[0],'%Y-%m-%d')
                high = int(row[1])  #转换成int
                low = int(row[3])
            except ValueError:  #遇到数据错误时 找到错误的位置 并提示
                print(date,'missing_data')
            else:                    
                dates.append(date)               
                highs.append(high)            
                lows.append(low)
        return dates,highs,lows
#画图
def draw_chart(value_x,value_y1,value_y2,chart_name,distance):
    fig = plt.figure(dpi = 128,figsize=(8,5))
    plt.plot(value_x,value_y1,c = 'red',alpha = 0.5)
    plt.plot(value_x,value_y2,c = 'blue',alpha = 0.5)
    plt.fill_between(value_x,value_y1,value_y2,facecolor='blue',alpha = 0.1) #填充两条折现之间的空白
    #设置图表格式
    plt.title(chart_name, fontsize=24)
    plt.xlabel('', fontsize=16)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
    '''
    参考此链接可以学习怎么设置日期横坐标
    https://blog.csdn.net/ZengHaihong/article/details/70747247?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control
    '''
    plt.xticks(pd.date_range(value_x[0],value_x[len(value_x)-1],freq = distance))#,rotation = 90
    fig.autofmt_xdate()   #自动调整坐标说明的角度
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=5)  #设置坐标轴刻度
    plt.grid()  #显示网格

def main():
    dates,highs,lows = get_data('sitka_weather_07-2014.csv')
    dates2,highs2,lows2 = get_data('sitka_weather_2014.csv')
    dates3,highs3,lows3 = get_data('death_valley_2014.csv')
    draw_chart(dates,highs,lows,"Daily high temperatures - 2014-07",'1d')
    draw_chart(dates2,highs2,lows2,"Daily high temperatures - 2014",'15d')
    draw_chart(dates3,highs3,lows3,'death_valley','15d') #对数据异常进行处理，空字符无法转换成int
    plt.show()

if __name__ == "__main__":
    main()