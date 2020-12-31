import pygal_maps_world.maps
wm = pygal_maps_world.maps.World() #创建一个worldmap 实例
wm.title = 'North, Central, and South America'
 
wm.add('North America', ['ca', 'mx', 'us'])  #add()接收一个标签和一个列表 前者显示在图例中 后者是我们在地图上要标出的位置
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file('americas.svg')
