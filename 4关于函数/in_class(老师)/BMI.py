'''
python :
    三类：
        1流程控制
        2:条件判断语句
        3循环语句；
    1条件判断语句
        if 条件:      # 条件是一个很抽象的过程；当你条件成立的时候

        elif 条件:

        else:
    2：input()  input函数本身适用于在空调中接受用户输入值
    3：条件判断符号：
        条件判断符号：
           不等于号： != ;     ！(中文的感叹号)    !(英文的感叹号)
           等于号： == ;       # 赋值号  =
           大于号 ：  >  ； 大于等于号 >= ;
           小于号 ：  < ;   小于等于号 <= ;
           False  恒错误；
           True   恒正确；
        链接符号：
            and : #两边的条件都要成立  if (** and **)
            or : # 两边的条件只要成立一个  if (** or **)
    4 ：计算BMI值；
        什么是BMI：衡量一个人的身高体重是否正常
            低于18.5：过轻
            18.5-25：正常
            25-28：过重
            28-32：肥胖
            高于32：严重肥胖

        bmi的计算公式 ：
           体重(kg) / 身高的公尺(m) 平方



'''

'''    if 语法：
# if False:  # True  这个条件表示该条件恒成立！  ，False是错误的意思 ，if False 就不执行 if下面的模块； False 和 True 称为bool类型；
#     print('这个条件成立')
# else:
#     print('这个条件不成立！')

# a = 1
# # if 他是一个 条件判断的关键字：
# if a == 1:
#     print('a是1')
# elif a!=1:
#     print('a不是1')
# else:
#     print('以上回答都不是~')


'''

# 2 input的使用：
# 1；
# user_say = input('请输入你想说的话:')
# print('我猜你说的话是:',user_say)

# 2：认识input函数的相关属性；
# num = int(input('请输入一个数字:'))  # please input nums
# result = num + 1
# print(result)

# input() 这个函数，他可以用来接受控台的数据 ，数据默认是str类型的，而不是int类型；

# a = '1'
# b = 1
#
# print(type(a),type(b))

'''第三部分：
    实现登录系统：
    
'''
# test 模拟登录
# zhanghao = 'chugu@163.com'
# password = '123456'
# countent = input('请输入账号:')
# passwords = input('请输入你的密码:')
# if countent == zhanghao and password == passwords:
#     print('登录成功~')
# else:
#     print('登录失败~')


'''
   这是注释： 注释的快捷键 是 ctrl+/
    注释就是用来提醒，和告诉别人这些代码写了是用来干嘛的。  
   解除注释  也是选中 # 注释的 代码或者文字 再按一次 ctrl+/
   ctrl+ z: 回到上一步操作；
'''

# # 4 计算用户的bmi值；
# hight = float(input('请输入您的身高:'))   # 22  '22'  float == 1.2
# weith = input('请输入您的体重:')
#
# # 计算用户的bmi值；体重(kg) / 身高的公尺(m) 平方  # 变量 variable
# bmi = float(weith) / (hight ** hight)
# print('bmi值为：', bmi)
#
# # 现在我们知道了bmi值 然后 根据bmi值进行判断；
# '''
#     什么是BMI：衡量一个人的身高体重是否正常
#     低于18.5：过轻
#     18.5-25：正常
#     25-28：过重
#     28-32：肥胖
#     高于32：严重肥胖
#
# '''
# if bmi < 18.5 :
#     print('您的bmi值为', bmi, '过轻！')
# elif 18.5 <= bmi <= 25:
#     print('您的bmi值为', bmi, '正常！')
# elif 25 <= bmi <= 28:
#     print('您的bmi值为', bmi, '过重！')
# elif bmi >32:
#     print('您的bmi值为', bmi, '严重肥胖！')


# 计算用户的体脂率，并判断；
# 5 计算用户的bmi值 和 体脂率 ；

# 体脂率计算公式:体脂率的计算：1.2 * bmi + 0.23*年龄-5.4-10.8  *（男1，女0）
hight = float(input('请输入您的身高:'))  # 22  '22'  float == 1.2
weith = float(input('请输入您的体重:'))
age = int(input('请输入您的年龄:'))
gender = input('请输入您的性别:')

# 计算用户的bmi值；体重(kg) / 身高的公尺(m) 平方  # 变量 variable
bmi = float(weith) / (hight ** hight)
# print('bmi值为：', bmi)

# 计算用户的体脂率； 当前这个 result变量保存的就是 体脂率计算的结果
result = ''
if gender == 'male':
    # 这是男性的体脂率；
    result = 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * 1
elif gender == 'female':
    # 女性的体脂率
    result = 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * 0

# 现在我们知道了bmi值 然后 根据bmi值进行判断；
'''
    什么是BMI：衡量一个人的身高体重是否正常
    低于18.5：过轻
    18.5-25：正常
    25-28：过重
    28-32：肥胖
    高于32：严重肥胖

'''
# round 函数 ，该函数会自动 吧小数点取你想保留的小数点；
if bmi < 18.5:
    print('您的bmi值为', round(bmi, 1), '您的体脂率为:', round(result, 1), '过轻！')
elif 18.5 <= bmi <= 25:
    print('您的bmi值为', round(bmi, 1), '您的体脂率为:', round(result, 1), '正常！')
elif 25 <= bmi <= 28:
    print('您的bmi值为', round(bmi, 1), '您的体脂率为:', round(result, 1), '过重！')
elif bmi > 32:
    print('您的bmi值为', round(bmi, 1), '您的体脂率为:', round(result, 1), '严重肥胖！')
