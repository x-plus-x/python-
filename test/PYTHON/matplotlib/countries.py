import pygal
from pygal.maps.world import COUNTRIES
#获取每个国家的国别码
for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code])
