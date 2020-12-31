# population_data.json 里的数据是一个很长的列表，列表里的每隔元素是包含四个值的字典：国家名、国别码、年份，人口数量
import json
from countries_code import get_country_code

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f) #load() 将json数据处理成python可以处理的形式
cc_populations = {} #字典类型
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010': #某个键对应的值是否为规定值
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value'])) #包含小数的字符串不能直接转换为int 要先转换成float在转成int
        #print(country_name + ':' + str(population))
        code = get_country_code(country_name)  #获得国家名字对应的码号
        if code:
            cc_populations[code] = population
import pygal_maps_world.maps
wm = pygal_maps_world.maps.World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)
wm.render_to_file('world_population.svg')
        
