'''

能正常看到我屏幕的同学扣1~
数据可视化
pyecharts ==
开源 的软件 。免费商用， 诞生的比较晚

matlab = 美国
不开源，且软件收费
不能免费商用
诞生的i比较早
pip install pandas

10月6号节课

第一预定金抵扣

第二交齐尾款的同学
3999rm  精品小课
在潭州课堂上能搜索道德课程
'''
import pandas as pd
from pyecharts.charts import Bar, Line, Pie

#  使用pands中 的 read读取 豆瓣用户评分信息.csv 中的数据 当然 with open 读也是一样的
data = pd.read_csv('豆瓣用户评分信息.csv', encoding='gbk')  # gbk,,,,utf-8
# 当前data对象拿到的是 csv标题
# for i in data:
#     print(i)

# 循环打印出pl_data 对象  这是可以拿出所有的pl对象；

# 我们取 评论标题；
sc_data = data['scores']
# for i in pl_data:
#     print(i)

# 建立一个字典
dc = {}

# 我们要拿的是scores里面的数据， 经行星级比较，要为每条#每条星级穿插数据
# 但是有些评论中没有星级数据 所以 遍历 sc_data数据
# 实现 星级 累积  1颗星：多少颗 ，2颗星：多少颗，3颗星：多少颗，4颗星：多少颗，5颗星：多少颗
for i in sc_data:
    if str(i) not in dc:  # i是字符串类型的
        # 这是初始化判断 ，一开始 1-5星都没有数据 ，但是这样创建了之后 就会有数据了
        # 这样的一个目的相当于创建一个key ，
        dc[str(i)] = 0
        # print('当前这个数据'+str(i)+'是没有的')
    else:
        # 否则当这个数据在 这个字典中 ，为这个对应的数据 增加一条数据
        dc[str(i)] = dc[str(i)] + 1
        # print('当前这个数据' + str(i) + '是有的，以将此数据插入到字典中')

# 最后我们得到 一个 星级 与 星级数据相对应的 字典数据；
# for key,values in dc.items():
#     print('key:values')
#     print(key,values)


# 打印星级的总数值  dc.keys()获取 字典的key值；
for i in dc.keys():
    print('%s:%s' % (i, dc[i]))
print([dc[i] for i in dc])

#
# print('///////////////////////////////')
# 打印星级 数据
for i in dc:
    print(i, end=' ')
print([i for i in dc])
line = (Line().add_xaxis([i for i in dc]).add_yaxis('', [dc[i] for i in dc])).render('流浪地球折现图.html')
# 柱状图
bar = (Bar().add_xaxis([i for i in dc]).add_yaxis('流浪地球的影评', [dc[i] for i in dc])).render('流浪地球柱状图.html')
# 先将字典的key值转换成列表
list_key = list(dc)
print('list_key:', list_key)
# 再将 字典的value转换成 列表
list_value = []
for i in dc.keys():
    list_value.append(dc[i])
print('list_value', list_value)
pie = (Pie().add(series_name='流浪地球影评', data_pair=[i for i in zip(list_key, list_value)])).render('流浪地球Pie图.html')

# a =['a','b','','c']
# b = []
# b =[ i for i in a]
# print(b)


# d = { 'chugu': 10, 'xionzi': 20, 'Bart': xiaoming, 'xiaowang': 60 }
# sum = 0
# for key, value in d.items():
#     sum = sum + value
#     print(key, ':' ,value)
# print('平均分为:' ,sum /len(d))
