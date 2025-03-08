height = float(input('请输入您的身高:'))
weight = input('请输入您的体重:')
age = int(input('请输入您的年龄:'))
gender = input('请输入您的性别:')
bmi = float(weight) / (height ** height)
result = ''


def body_fat(bmi, age, gender):
    if gender == 'man':
        # 男
        result = 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * 1
        return result
    elif gender == 'female':
        # 女
        result = 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * 0
        return result


def my_bmi(bmi, body_fat, age, gender):
    if bmi < 18.5:
        # print('您的BMI值为:', round(bmi, 1), '您的体脂率为：', round(result, 1), ' 过轻!')
        # print('您的BMI值为%.2f过轻, 您的体脂率%.2f' % (bmi, result))
        print('您的BMI值为:', bmi, '您的体脂率为：', body_fat(bmi, age, gender), ' 过轻!')
    elif 18.5 <= bmi < 25:
        # print('您的BMI值为:', round(bmi, 1), '您的体脂率为：', round(result, 1), ' 正常!')
        # print('您的BMI值为%.2f正常, 您的体脂率%.2f' % (bmi, result))
        print('您的BMI值为:', bmi, '您的体脂率为：', body_fat(bmi, age, gender), ' 正常!')
    elif 25 <= bmi < 28:
        # print('您的BMI值为:', round(bmi, 1), '您的体脂率为：', round(result, 1), ' 过重!')
        # print('您的BMI值为%.2f过重!, 您的体脂率%.2f' % (bmi, result))
        print('您的BMI值为:', bmi, '您的体脂率为：', body_fat(bmi, age, gender), ' 过重!')
    elif 28 <= bmi < 32:
        # print('您的BMI值为:', round(bmi, 1), '您的体脂率为：', round(result, 1), ' 肥胖!')
        # print('您的BMI值为%.2f肥胖!, 您的体脂率%.2f' % (bmi, result))
        print('您的BMI值为:', bmi, '您的体脂率为：', body_fat(bmi, age, gender), ' 肥胖!')
    elif bmi > 32:
        # print('您的BMI值为:', round(bmi, 1), '您的体脂率为：', round(result, 1), '严重肥胖!')
        # print('您的BMI值为%.2f严重肥胖!, 您的体脂率%.2f' % (bmi, result))
        print('您的BMI值为:', bmi, '您的体脂率为：', body_fat(bmi, age, gender), '严重肥胖!')


if 18 <= age <= 39 and gender == 'male':
    my_bmi(bmi, body_fat, age, gender)

elif 40 <= age <= 59 and gender == 'male':

    my_bmi(bmi, body_fat, age, gender)

elif age > 60 and gender == 'male':

    my_bmi(bmi, body_fat, age, gender)

elif 18 <= age <= 39 and gender == 'female':

    my_bmi(bmi, body_fat, age, gender)

elif 40 <= age <= 59 and gender == 'female':

    my_bmi(bmi, body_fat, age, gender)

elif age > 60 and gender == 'female':

    my_bmi(bmi, body_fat, age, gender)
