'''
什么是函数？
python中的函数
    其实和大家认知的应该是不一样的
    一个xy方程式
    python 中的函数可以理解方法
    python中内置的函数可以理解成已经写好了方法
    来带大家
    声明函数的语法
'''
#定义无参函数的语法
def p():
    # pass#pass语句相当于占位符
    print('这是我刚定义的函数')
#一定要调用
# p()
def bmi():
    #方法体，就是实现这个函数的代码
    # 身高，体重
    h = float(input('请输入身高(公尺)'))  # =赋值
    w = float(input('请输入体重'))
    sex = input('请输入性别')
    age = input('请输入年龄')
    # age = input('')

    # bmi：公式=w/h*h
    h = h * h
    bmi = (w / h)  # 程序计算的优先级
    print('bmi值为：' + str(round(bmi, 1)))
    # 判断人体体重的轻重
    # 低于18.5：过轻
    # 18.5-25：正常
    # 25-28：过重
    # 28-32：肥胖
    # 高于32：严重肥胖
    if bmi < 18.5:
        print('同学你的BMI值为' + str(round(bmi, 1)) + '过轻')
    elif 18.5 <= bmi < 25:
        print('同学你的BMI值为' + str(round(bmi, 1)) + '正常')
    elif 25 < bmi < 28:
        print('同学你的BMI值为' + str(round(bmi, 1)) + '过重')
    elif bmi > 32:
        print('同学你的BMI值为' + str(round(bmi, 1)) + '超重')
        # 体脂率计算公式:体脂率的计算：
        # 1.2 * bmi +0.23*年龄-5.4-10.8X（男1，女0）
    if sex == '男':  # == 就等于 =,python乘号=* 除号=/
        body = (1.2 * bmi + 0.23 * float(age) - 5.4 - 10.8)
        print('你的体脂率为：' + str(round(body)))
    elif sex == '女':
        body = (1.2 * bmi + 0.23 * float(age) - 5.4)
        print('你的体脂率为：' + str(round(body)))

#retrun,带参

# def add(a,b):
#     return print(a+b)
# #
# def abc():
#     a = 'ab'
#     b = 'cd'
#     return a+b
# print(abc())
#求绝对值,web,从页面接受到了一个数值，数据库’-‘
#在页面中用js， 9
# print(abs(-9))

# print(max(1,20,66,100))
# print(min(1,20,66,100))
# 1,01,0101,二进制
# print(hex(1314))
# a = '同学们晚上好'
# b = '同学们早上好'
#查找这个变量的内存地址
# print(id(a))
# print(id(b))
# a = input('给个数字给我')
# a = [1,2,3,4,5,20,50,60]
# b=0
# for i in a:
#     b +=1
# print(b)
# len()
# import os
# os.mkdir('111111')
# os.rmdir('111111')
#
# print(abs(-9))
# def my_abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x
#
# print(my_abs(-9))
# help(abs(9))
# def classs(name,gender,age='6',city='长沙'):
#     print('name'+name)
#     print('gender'+gender)
#     print('age'+age)
#     print('city'+city)
# classs('小明0','男')


#99乘法表
#循环,for循环，i是变量，i有对应的值，range(5)就是循环的函数,0是初始值，5是终止值
# for i in range(1,10):#这是外层循环
#     for j in range(1,i+1):#内存循环
#         print(str(j)+'*'+str(i)+'='+str(i*j),end=' ')
#     print()
#循环次数终止值-初始值
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('i值'+str(i)+'j值'+str(j)+'='+str(i*j),end=' ')
#     print()
import os
def acount(a):
    if len(a)>11:
        print('该账号不能超过11位数字')
    else:
        print('成功注册')
acounts = input('请输入你的账号不得超过11位数字')
acount(acounts)








