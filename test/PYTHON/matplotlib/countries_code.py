#coding=utf-8
import pygal
from pygal.maps.world import COUNTRIES
def get_country_code(country_name):
    '''根据指定的国家，返回 Pygal 使用的两个字母的国别码'''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有找到指定的国家，就返回 None
    return None