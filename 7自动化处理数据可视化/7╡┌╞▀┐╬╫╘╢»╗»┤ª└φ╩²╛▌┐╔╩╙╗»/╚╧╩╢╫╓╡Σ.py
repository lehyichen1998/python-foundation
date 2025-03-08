'''
什么是字典？
    dict: 全称：dictionary ，是一种映射类型的数据
    声明方式：# a = {}
    a = {'key':'value'}
    dc = {'name':'楚楚', 'age': 25, 'hobby':['看书','爬山'],'other_hobby':{'sleep': '很晚'}}
'''

# 创建字典
dc = {}

# 认识 字典数据
'''
a = {'key':'value','key':'value'}

    key:值只能为 整数 ，字符串， 或者 浮点数据
    value: 任何对象 
'''

dcs = {'name':'楚楚', 'age': 25, 'hobby':['看书','爬山'],'other_hobby':{'sleep': '很晚'}}
# 字典的 遍历：
# for i in dcs:  # 默认拿到 key
#     print(i)

# for i in dcs.items():  # 当然也可以拿 所有内容；
#     print(i)

# 如何拿到value呢？
# for i in dcs.keys():
#     print(dcs[i])
# 如何将两者呈现出来呢，就是 key：value 这样的排序
# for i in dcs.keys():
#     # 这里可以使用字符串匹配
#     print('%s:%s'%(i,dcs[i]))

