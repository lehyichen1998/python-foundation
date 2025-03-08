# if statement
'''
a = 1

if a == 1:
    print('a是1')
elif a != 1:
    print('a不是1')
else:
    print('以上都不是答案')
'''

# input statement
'''user_say = input('请输入你想说的话:')
print('我猜你先说的: ',user_say)
'''

# num = int(input('请输入一个数字:'))
# result = num+1
# print(result)

# define string and int
# a = '1'
# b = 1
# print(type(a),type(b))

# login system example
# id = '123'
# password = '456'
# idinput = input('请输入账号:')
# passwordinput = input('请输入密码:')
#
# if idinput == id and passwordinput == password:
#     print('登录成功')
# else:
#     print('登录失败')

# bmi calculation：
# height = float(input('请输入您的身高:'))
# weight = input('请输入您的体重:')
#
# # bmi formula
# bmi = float(weight) / (height * height)
#
# if bmi < 18.5:
#     print('您的BMI值为:', bmi, ' 过轻')
# elif 18.5 < bmi <= 25:
#     print('您的BMI值为:', bmi, ' 正常')
# elif 25 < bmi <= 28:
#     print('您的BMI值为:', bmi, ' 过重')
# elif 28 < bmi <= 32:
#     print('您的BMI值为:', bmi, ' 肥胖')
# elif bmi > 32:
#     print('您的BMI值为:', bmi, '严重肥胖')

# fat calculation
# fat calculation formula: 1.2*bmi+0.25*age-5.4-10.8*(男1,女0)
result = ''
height = float(input('请输入您的身高:'))
weight = input('请输入您的体重:')
age = int(input('请输入您的年龄:'))
gender = input('请输入您的性别:')

# bmi formula
bmi = float(weight) / (height ** height)
if gender == 'man':
    # 男
    result = 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * 1
elif gender == 'female':
    # 女
    result = 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * 0
if bmi < 18.5:
    # print('您的BMI值为:', round(bmi, 1), '您的体脂率为：', round(result, 1), ' 过轻!')
    # print('您的BMI值为%.2f过轻, 您的体脂率%.2f' % (bmi, result))
    print('您的BMI值为:', bmi, '您的体脂率为：', result, ' 过轻!')
elif 18.5 <= bmi < 25:
    # print('您的BMI值为:', round(bmi, 1), '您的体脂率为：', round(result, 1), ' 正常!')
    # print('您的BMI值为%.2f正常, 您的体脂率%.2f' % (bmi, result))
    print('您的BMI值为:', bmi, '您的体脂率为：', result, ' 正常!')
elif 25 <= bmi < 28:
    # print('您的BMI值为:', round(bmi, 1), '您的体脂率为：', round(result, 1), ' 过重!')
    # print('您的BMI值为%.2f过重!, 您的体脂率%.2f' % (bmi, result))
    print('您的BMI值为:', bmi, '您的体脂率为：', result, ' 过重!')
elif 28 <= bmi < 32:
    # print('您的BMI值为:', round(bmi, 1), '您的体脂率为：', round(result, 1), ' 肥胖!')
    # print('您的BMI值为%.2f肥胖!, 您的体脂率%.2f' % (bmi, result))
    print('您的BMI值为:', bmi, '您的体脂率为：', result, ' 肥胖!')
elif bmi > 32:
    # print('您的BMI值为:', round(bmi, 1), '您的体脂率为：', round(result, 1), '严重肥胖!')
    # print('您的BMI值为%.2f严重肥胖!, 您的体脂率%.2f' % (bmi, result))
    print('您的BMI值为:', bmi, '您的体脂率为：', result, '严重肥胖!')
