#coding=utf-8
from die import Die
import pygal
die1 = Die()
die2 = Die(10)

results = []  #存储摇出来的结果
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)
#分析结果
frequencies = []
for value in range(2,die1.num_sides+die2.num_sides + 1): #左闭右开
    frequency = results.count(value)
    frequencies.append(frequency)
print(results)
print(frequencies)
#可视化结果
hist = pygal.Bar()

hist.title = "Result"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Number"
hist.y_title = "Frequency"

hist.add('D6+D10',frequencies)
hist.render_to_file('dices_visual.svg')

    