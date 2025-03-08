# for i in range(0,5):
#     print(str(i)+',外层',end='')
#     for j in range(0,5):
#         print(str(j)+',内层')

'''

python中的自动化
    web自动化，selenium, xpath
    excel 自动合并文件
    上节课的  循环弄懂了吗？
    for 循环，，还有函数
'''
# a = [10,20,30,40,50,60,70]
# # for i in range(1,10):#外层循环 终止值-初始值 =循环次数
# #     #外层循环执行一次,内层循环全部执行完毕
# #     print('i值'+str(i))
# #     for j in range(1,i+1):#内层循环
# #         print('j值'+str(j),end='')
#
# for i in a:#这是循环的一个用法
#     print(i)
#
# 自动合并文件,pip install csv
import os
import csv


#首先要让python找到要合并的相关文件
location = './疫苗流向城市分布'
_csv = os.listdir(location)
#创建一个列表
li = []
for i in _csv:#读取里面的所有文件名
    print(str(i))
    with open(location+'/'+i,'r',encoding='utf-8') as r:
        #通过realines()方法读取每一条数据
        for j in r.readlines():
            j = j.replace('\n','')
            print(j)
            li.append(j)

    with open('中国所有的疫苗流向文件.csv','a+',encoding='utf-8',newline='') as f:
        f_csv = csv.writer(f)
        for k in li:
            f_csv.writerow(k.split(','))















