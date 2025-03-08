# 定义一个用来计算BMI的文件
def My_Bmi():
    hight = float(input('请输入您的身高:'))  # 22  '22'  float == 1.2
    weith = float(input('请输入您的体重:'))
    age = int(input('请输入您的年龄:'))
    gender = input('请输入您的性别:')
    # 对体脂和bmi进行全方位的判断；  条件是不是更多；
    # pass是一个关键字，起到一个占位符的作用，本身没有任何意义；

    # bmi是一个 衡量人胖瘦的标准；
    bmi = float(weith) / (hight ** hight)

    # 来利用带参数 实现 体脂率的计算；
    def body_fat(bmi, age, gender):
        # if和elif 一套组合 ，当其中一个条件满足，就会返回那个条件满足的那个结果；
        if gender == 'male':
            # 这是男性的体脂率；
            result = 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * 1
            return result
        elif gender == 'female':
            # 女性的体脂率
            result = 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * 0
            return result

    # 优化 胖瘦判断；
    def my_bmi(bmi, body_fat, age, gender):
        # print('这是男性 18到39之间的 胖瘦判断')
        if bmi < 18.5:
            print('您的bmi值为', round(bmi, 1), '您的体脂率为:', round(body_fat(bmi, age, gender), 1), '过轻！')
        elif 18.5 <= bmi <= 25:
            print('您的bmi值为', round(bmi, 1), '您的体脂率为:', round(body_fat(bmi, age, gender), 1), '正常！')
        elif 25 <= bmi <= 28:
            print('您的bmi值为', round(bmi, 1), '您的体脂率为:', round(body_fat(bmi, age, gender), 1), '过重！')
        elif bmi > 32:
            print('您的bmi值为', round(bmi, 1), '您的体脂率为:', round(body_fat(bmi, age, gender), 1), '严重肥胖！')

    if 18 <= age <= 39 and gender == 'male':
        my_bmi(bmi, body_fat, age, gender)
    elif 40 <= age <= 59 and gender == 'male':
        my_bmi(bmi, body_fat, age, gender)
    elif age > 60 and gender == 'male':
        my_bmi(bmi, body_fat, age, gender)
    # 对女性和女性的年龄区间进行判断；
    elif 18 <= age <= 39 and gender == 'female':
        my_bmi(bmi, body_fat, age, gender)
    elif 40 <= age <= 59 and gender == 'female':
        my_bmi(bmi, body_fat, age, gender)
    elif age > 60 and gender == 'female':
        my_bmi(bmi, body_fat, age, gender)

# 没有显示的原因是，没有调用该函数
#调用 计算 BMI的函数
My_Bmi()