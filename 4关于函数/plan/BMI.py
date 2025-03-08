

# html 静态页面；
# 20:00准时开始！ 请同学们准备好电源以及网络！

'''
流程控制语句
    三类
        1流程顺序：
        2条件判断：
        3循环语句：
    if 条件 :
    成立；写根据条件要执行的代码模块
    elif 条件:
        满足elif条件；写根据条件要执行的代码模块
    else:#否则
        不成立；写根据条件要执行的代码模块

    if中的条件判断符
    条件判断符
    !=,==,<,>,<=,>=,True,False（恒成立）
    链接符：
    and :必须要两个条件都要满足
    or :两个条件满足一个就好
'''


'''
#模拟登陆：

countent = int(input('创建账号'))
password = input('创建密码')
print('创建成功')
print('请登录！！！！')
c = int(input('账号'))
p = input('密码')
if c == countent or p == password:
    print('登陆成功！！')
else:
    print('登陆失败！！')
'''
# def BMI(h,w,wex,age):
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

# BMI(1,2,2,2)