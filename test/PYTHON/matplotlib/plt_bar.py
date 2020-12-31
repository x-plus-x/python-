from die import Die
import matplotlib.pyplot as plt
#创建一个色子
die = Die()
results = []  #存储摇出来的结果
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
#分析结果
frequencies = []
for value in range(1,die.num_sides+1): #左闭右开
    frequency = results.count(value)
    frequencies.append(frequency)
print(results)
print(frequencies)
#可视化结果

plt.bar(range(1,7),frequencies,align='center')
plt.xlabel("number")
plt.ylabel("Frequncy")
'''
前边设置的x、y值其实就代表了不同柱子在图形中的位置（坐标），通过for循环找到每一个x、y值的相应坐标——a、b，
再使用plt.text在对应位置添文字说明来生成相应的数字标签，而for循环也保证了每一个柱子都有标签。
其中，a, b+0.05表示在每一柱子对应x值、y值上方0.05处标注文字说明， 
'%.0f' % b,代表标注的文字，即每个柱子对应的y值， ha='center', va= 'bottom'代表horizontalalignment（水平对齐）、
verticalalignment（垂直对齐）的方式，fontsize则是文字大小。
链接：https://www.jianshu.com/p/5ae17ace7984
'''
for x,y in zip(range(1,7),frequencies):  #设置数字标签
    plt.text(x,y+0.05,'%.0f'%y,ha = 'center',va='bottom')
plt.grid()
plt.show()