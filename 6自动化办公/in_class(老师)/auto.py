
# 读到 疫苗流向城市分布 里面文件 信息；
# 文件的绝对路径
import os
import csv

file_location = r'D:\预科班\6自动化办公\in_class\疫苗流向城市分布'
# 文件的相对路径
file = '疫苗流向城市分布'

# 如何读到文件夹里面的数据呢？   1    2
# 创建列表 ,理解成一个容器
lst = []
dirs = os.listdir(file_location)
for i in dirs:
    # print(i)
    # file_location+'/'+i  作用是 起到一个拼接作用，  拼接出一个文件绝对 路径
    with open(file=file_location+'/'+i,mode='r',encoding='utf-8') as read_file:
        r = read_file.readlines()  # readlines 以列表的形式返回
        for k in r:
            # print(k)
            a = k.replace('\n','')  #\n 时表示换行；
            # print(a)
            lst.append(a)

# 打印 lst
# print(lst)
# for j in lst:
#     print(j)

# 将所有的文件写入到 一个txt文件中  w  # mode= 'w' 文件路径的那个文件  会自动创建
# with open('整合文件.txt',mode='w',encoding='utf-8') as write_file:
#     for i in lst:
#         write_file.write(i)


# 第二个版本
with open('整合文件.csv',mode='w',encoding='utf-8',newline='') as write_file:
    w_f = csv.writer(write_file)
    for i in lst:
        w_f.writerow(i.split(','))


