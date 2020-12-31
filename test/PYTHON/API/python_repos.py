import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行 API 调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:Go&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)  #响应对象r中的属性status_code知道响应状态 200 表示响应成功    

# 将 API 响应存储在一个变量中
response_dict = r.json()
#print(response_dict.keys())
print("Total repositories:", response_dict['total_count'])  #获得相应的值
# 探索有关仓库的信息
def get_dicts(response_dict):
    repo_dicts = response_dict['items']  # items就是一个包含各种项目信息字典的列表 
    print("Repositories returned:", len(repo_dicts))
    print("\nSelected information about each repository:")
    for repo_dict in repo_dicts: 
        print('\nName:', repo_dict['name'])
        print('Owner:', repo_dict['owner']['login'])
        print('Stars:', repo_dict['stargazers_count'])
        print('Repository:', repo_dict['html_url'])
        print('Description:', repo_dict['description'])
'''
# 研究第一个仓库
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
print("\nSelected information about first repository:")
print('Name:', repo_dict['name']) #项目名称
print('Owner:', repo_dict['owner']['login']) # 所有者和所有者登录名 
print('Stars:', repo_dict['stargazers_count']) #获得的星星
print('Repository:', repo_dict['html_url'])# 获得地址
print('Created:', repo_dict['created_at'])#创建时间
print('Updated:', repo_dict['updated_at'])#更新时间
print('Description:', repo_dict['description'])#描述信息
'''
def visual(response_dict):
    names,stars = [] , []
    repo_dicts = response_dict['items']
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        stars.append(repo_dict['stargazers_count'])
    #       绘制可视化图
    my_style = LS('#333366', base_style=LCS) # LightenStyle 类（别名 LS ）定义了一种样式，并将其基色设置为深蓝色
    # 对pygal进行配置
    my_config = pygal.Config()
    my_config.x_label_rotation = 90  #x轴标签旋转 X 度
    my_config.show_legend = False  #不显示图例
    my_config.title_font_size = 24  #  标题字体大小
    my_config.label_font_size = 14 #副标签字体大小（x轴和y轴大部分内容）
    my_config.major_label_font_size = 18  # 主标签（y轴上为5000的整数倍的内容）
    my_config.truncate_label = 15  #将较长的项目名缩短为15字
    my_config.show_y_guides = False  # 隐藏图标中的水平线
    my_config.width = 1000  #自定义图表宽度
    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-Starred GO Projects on GitHub'
    chart.x_labels = names  #将x轴设置为names
    chart.add('', stars) #  添加数据  按顺序添加 所以与names一一对应
    chart.render_to_file('Go_repos.svg')

def main():
    visual(response_dict)

if __name__ == "__main__":
    main()