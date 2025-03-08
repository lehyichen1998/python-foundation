'''

一： 认识 for 循环
    循环和条件语句 都是 Python中常用的 流程控制语句
    for 可迭代变量 in 循环对象:
        循环体内容

二： # 什么是 循环对象 ？

    # 什么是 可迭代变量 ？

    # 什么是 循环体内容？


三： 认识路径；
    # 绝对路径；
    # 相对路径；


四： 导入模块；
    os 模块；
    csv模块；

五：认识 open函数 ； 简述；
'''



'''
一： 认识 for 循环
    循环和条件语句 都是 Python中常用的 流程控制语句
    for 可迭代变量 in 循环对象:
        循环体内容
'''

# 重复做一件事；
# print('hello')
# print('hello')
# print('hello')
# print('hello')
# print('hello')

# 如何使用代码 循环执行打印hello呢？
'''
二： # 什么是 循环对象 ？

    # 什么是 可迭代变量 ？

    # 什么是 循环体内容？

'''
# 举个例子：
'''
for 可迭代变量 in 循环对象:
    print('hello')
能  1    不能  2 
'''
# 以上的例子：   认识 1   不认识 2 ；
# for i in range(5):
#     print('hello')

# 什么是 可迭代变量 ？  英文名称：Iterable variable ； num -
# 可迭代变量 就是 变量的值 会发生变动 ；
# for num in range(5):
#     print(num)
# 1,2,3,4,5   1        5个num  2



# 什么是 循环对象 ？ 1：   2  不能  3
# for num in range(1,100,10):     # range(5)   # 那么param 有什么作用呢？
#     # range(初始值, 终止值,跳转值)  # 你想实现 一个循环  终止值-初始值 = 循环次数；
#     print(num)

# 什么是 循环对象 2？
# s = '123'
# num = [20,30,40]

# for i in num:
#     print(i)

# 什么是 循环体内容？
    # 他指的是 要循环执行的事情；print（’hello‘）

# for i in range(5):
#     print(666)



'''
三： 认识路径；
    # 绝对路径；
    # 绝对路径就是说 ： 从电脑根目录 开始找 ，
       D:\预科班\6自动化办公\plan\疫苗流向城市分布
    # 相对路径；
    # 指的是： 当前 test.py 这个文件 它和 ’疫苗流向城市分布‘之间的一个相对位置；
        疫苗流向城市分布
'''

'''
五：认识 open函数 ； 简述；
'''
# help(open) #  查看任何函数的方法；
# open() 这个函数本省就是用于 读写文件；
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# open() 是一个 操作文件的函数；
#  file  = 文件路径
#  mode = 'r' , 'w' ;
#  encoding = 'utf-8'




