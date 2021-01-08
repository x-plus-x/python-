import csv
import pandas as pd
import numpy as np
import xlrd
import os


def make_df(file_name):
    #file_name = r'test\20516505_2020-11-18 07-39-44-139.csv'
    data = pd.read_csv(file_name,encoding='utf-16',sep='\t') #加上sep = '\t'才能输出表格形式 否则会有制表符干扰
    #由于原表中有两个石灰列，需要对两列的值进行加和并放在一个列里头
    for i in range(data.shape[0]):
        data.iat[i,15] = data.iat[i,15] + data.iat[i,18]
    #选择所需列数据组成新表
    select_data= data[["炉次号",'炉次状态','吹氧时间','总氧',"枪位",'氧气压力','石灰','高镁灰','污泥球','渣钢粒','矿石','石灰石']]
    select_data = select_data[select_data["炉次状态"]=='吹氧冶炼']

    total_oxy = select_data['总氧'].max()  #获得总氧

    proportion_oxy = [] #吹氧百分比
    #计算吹氧百分比
    for value in select_data['总氧']:  
        proportion_oxy.append(round(value/total_oxy,2))
    #插入吹氧百分比的列
    select_data.insert(2,'吹氧百分比',proportion_oxy)
    #创建新表
    new_data = pd.DataFrame(columns=['吹氧比例','枪位','氧压','石灰','高镁灰','污泥球','渣钢粒','矿石','石灰石'])
    #创建一个临时表 用来传递值 因为df得传递series
    temp1 = pd.DataFrame(columns=['吹氧比例','枪位','氧压','石灰','高镁灰','污泥球','渣钢粒','矿石','石灰石'],data=[[1,1,1,1,1,1,1,1,1]])
    #将每百分一氧作为一行 
    for i in range(101):
        i=i+1
        temp = select_data[select_data["吹氧百分比"]>(i-1)/100]
        temp = temp[temp["吹氧百分比"]<(i+1)/100]
        temp1['吹氧比例'] = i-1
        temp1['枪位'] = temp['枪位'].mean()  #枪位和氧压取平均值
        temp1['氧压'] = temp['氧气压力'].mean()
        temp1['石灰'] = temp['石灰'].max()
        temp1['高镁灰'] = temp['高镁灰'].max()
        temp1['污泥球'] = temp['污泥球'].max()
        temp1['渣钢粒'] = temp['渣钢粒'].max()
        temp1['矿石'] = temp['矿石'].max()
        temp1['石灰石'] = temp['石灰石'].max()
        new_data = new_data.append(temp1) # 将一行添加给new_data
    #处理new_data中的加料
    new_data.set_index(['吹氧比例'],inplace = True) #将吹氧比例设置为列索引
    for k in range(99,0,-1):
        new_data.at[k,'石灰'] = new_data.at[k,'石灰'] - new_data.at[k-1,'石灰']
        new_data.at[k,'高镁灰'] = new_data.at[k,'高镁灰'] - new_data.at[k-1,'高镁灰']
        new_data.at[k,'污泥球'] = new_data.at[k,'污泥球'] - new_data.at[k-1,'污泥球']
        new_data.at[k,'渣钢粒'] = new_data.at[k,'渣钢粒'] - new_data.at[k-1,'渣钢粒']
        new_data.at[k,'矿石'] = new_data.at[k,'矿石'] - new_data.at[k-1,'矿石']
        new_data.at[k,'石灰石'] = new_data.at[k,'石灰石'] - new_data.at[k-1,'石灰石']
    #将石灰和镁灰转成百分比
    total_shihui = new_data['石灰'].sum()
    total_meihui = new_data['高镁灰'].sum()
    for k in range(99):
        new_data.at[k,'石灰'] = new_data.at[k,'石灰'] / total_shihui
        new_data.at[k,'高镁灰'] = new_data.at[k,'高镁灰'] / total_meihui
    return new_data

#def main():
path = r'D:\Plus\龙钢\静态模型\test'
file_names = os.listdir(path)
# 创建每张小表要填入的dataframe
lance_pos = pd.DataFrame()
oxy_press = pd.DataFrame()
shihui = pd.DataFrame()
meihui = pd.DataFrame()
wuniqiu = pd.DataFrame()
slagsteel = pd.DataFrame()
ore = pd.DataFrame()
shihuishi = pd.DataFrame()
for i in range (len(file_names)):
    file_name = file_names[i]
    number = file_name[0:8]
    file_path = os.path.join(path, file_name)
    data = make_df(file_path) # 读取每一张做好的表
    # 制作每张小表
    temp_lance_pos = data['枪位']
    lance_pos = pd.concat([lance_pos,temp_lance_pos],axis = 1)
    lance_pos = lance_pos.rename(columns = {'枪位':number})

    temp_oxy_press = data['氧压']
    oxy_press = pd.concat([oxy_press,temp_oxy_press],axis = 1)
    oxy_press = oxy_press.rename(columns = {'氧压':number})

    temp_shihui = data["石灰"]
    shihui = pd.concat([shihui,temp_shihui],axis = 1)
    shihui = shihui.rename(columns = {'石灰':number})

    temp_meihui = data['高镁灰']
    meihui = pd.concat([meihui,temp_meihui],axis = 1)
    meihui = meihui.rename(columns = {'高镁灰':number})

    temp_wuniqiu = data['污泥球']
    wuniqiu = pd.concat([wuniqiu,temp_wuniqiu],axis = 1)
    wuniqiu = wuniqiu.rename(columns = {'污泥球':number})

    temp_ore = data['矿石']
    ore = pd.concat([ore,temp_ore],axis = 1)
    ore = ore.rename(columns = {'矿石':number})

    temp_slagsteel = data['渣钢粒']
    slagsteel = pd.concat([slagsteel,temp_slagsteel],axis = 1)
    slagsteel = slagsteel.rename(columns = {'渣钢粒':number})

    temp_shihuishi = data['石灰石']
    shihuishi = pd.concat([shihuishi,temp_shihuishi],axis = 1)
    shihuishi = shihuishi.rename(columns = {'石灰石':number})
#   把每个dataframe 
lance_pos.to_csv('枪位.csv',encoding = 'gbk')
oxy_press.to_csv('氧压.csv',encoding = 'gbk')
shihui.to_csv('石灰.csv',encoding = 'gbk')
meihui.to_csv('高镁灰.csv',encoding = 'gbk')
wuniqiu.to_csv('污泥球.csv',encoding = 'gbk')
ore.to_csv('矿石.csv',encoding = 'gbk')
slagsteel.to_csv('渣钢粒.csv',encoding = 'gbk')


    
    
    












    

