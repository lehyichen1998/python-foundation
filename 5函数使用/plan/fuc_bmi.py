# 这里我们发现 体脂率是变化的；
def fat_rate(sex,age):
    '''接收一些参数实现功能复用'''
    result = ''
    if sex == '女':
        result = (1.2 * bmi + 0.23 * float(age) - 5.4)
    elif sex == '男':
        result = (1.2 * bmi + 0.23 * float(age) - 5.4 -10.8)
    return result



h = float(input('输入身高'))
w = float(input('输入体重'))
sex = (input('输入性别'))
age = int((input('输入年龄')))


bmi = (w/(h**h))
print ('BMI值为:'+str(round(bmi,2)))
'''
体脂率计算
男性： 
18-39 5-10% 瘦，11-21%正常，22-26偏胖，27-45 胖
40-59 5-11% 瘦，12-22%正常，23-27偏胖，28-45 胖
60    5-13% 瘦，14-24%正常，25-29偏胖，30-45 胖
女性：
18-39 5-20% 瘦，21-34%正常，35-39偏胖，40-45 胖
40-59 5-21% 瘦，22-35%正常，36-40偏胖，41-45 胖
60    5-22% 瘦，23-36%正常，37-41偏胖，42-45 胖
'''
if 18<=age<39 and sex =='男':
    if bmi <= 18.5:
        print('你的BMI值为' + str(round(bmi, 2)) + '过轻'+','+'体脂率为:' + str(round(fat_rate(age,age),1))+'过轻')
    elif 18.5 < bmi < 25:
        print('你的BMI值为' + str(round(bmi, 2)) + '正常'+','+'体脂率为:' + str(round(fat_rate(age,age),1))+'正常')
    elif 25 < bmi < 28 | age > 60:
        print('你的BMI值为' + str(round(bmi, 2)) + '偏胖'+','+'体脂率为:' + str(round(fat_rate(age,age),1))+'偏胖')
    elif bmi > 32:
        print('你的BMI值为' + str(round(bmi, 2)) + '胖'+','+'体脂率为:' + str(round(fat_rate(age,age),1))+'很胖')
elif 40<=age<59 and sex =='男':
    if bmi <= 18.5:
        print('你的BMI值为' + str(round(bmi, 2)) + '过轻'+','+'体脂率为:' + str(round(fat_rate(age,age),1))+'过轻')
    elif 18.5 < bmi < 25:
        print('你的BMI值为' + str(round(bmi, 2)) + '正常'+','+'体脂率为:' + str(round(fat_rate(age,age),1))+'正常')
    elif 25 < bmi < 28 | age > 60:
        print('你的BMI值为' + str(round(bmi, 2)) + '偏胖'+','+'体脂率为:' + str(round(fat_rate(age,age),1))+'偏胖')
    elif bmi > 32:
        print('你的BMI值为' + str(round(bmi, 2)) + '胖'+','+'体脂率为:' + str(round(fat_rate(age,age),1))+'很胖')
elif age>=60 and sex == '男':
    if bmi <= 18.5:
        print('你的BMI值为' + str(round(bmi, 2)) + '过轻' + ',' + '体脂率为:' + str(round(fat_rate(age,age), 1)) + '过轻')
    elif 18.5 < bmi < 25:
        print('你的BMI值为' + str(round(bmi, 2)) + '正常' + ',' + '体脂率为:' + str(round(fat_rate(age,age), 1)) + '正常')
    elif 25 < bmi < 28 | age > 60:
        print('你的BMI值为' + str(round(bmi, 2)) + '偏胖' + ',' + '体脂率为:' + str(round(fat_rate(age,age), 1)) + '偏胖')
    elif bmi > 32:
        print('你的BMI值为' + str(round(bmi, 2)) + '胖' + ',' + '体脂率为:' + str(round(fat_rate(age,age), 1)) + '很胖')
elif 18<=age<39 and sex == '女':
    if bmi <= 18.5:
        print('你的BMI值为' + str(round(bmi, 2)) + '过轻' + ',' + '体脂率为:' + str(round(fat_rate(age,age), 1)) + '过轻')
    elif 18.5 < bmi < 25:
        print('你的BMI值为' + str(round(bmi, 2)) + '正常' + ',' + '体脂率为:' + str(round(fat_rate(age,age), 1)) + '正常')
    elif 25 < bmi < 28 | age > 60:
        print('你的BMI值为' + str(round(bmi, 2)) + '偏胖' + ',' + '体脂率为:' + str(round(fat_rate(age,age), 1)) + '偏胖')
    elif bmi > 32:
        print('你的BMI值为' + str(round(bmi, 2)) + '胖' + ',' + '体脂率为:' + str(round(fat_rate(age,age), 1)) + '很胖')
elif 40<=age<59 and sex == '女':
    if bmi <= 18.5:
        print('你的BMI值为' + str(round(bmi, 2)) + '过轻' + ',' + '体脂率为:' + str(round(fat_rate(age,age), 1)) + '过轻')
    elif 18.5 < bmi < 25:
        print('你的BMI值为' + str(round(bmi, 2)) + '正常' + ',' + '体脂率为:' + str(round(fat_rate(age,age), 1)) + '正常')
    elif 25 < bmi < 28 | age > 60:
        print('你的BMI值为' + str(round(bmi, 2)) + '偏胖' + ',' + '体脂率为:' + str(round(fat_rate(age,age), 1)) + '偏胖')
    elif bmi > 32:
        print('你的BMI值为' + str(round(bmi, 2)) + '胖' + ',' + '体脂率为:' + str(round(fat_rate(age,age), 1)) + '很胖')
elif age>=60 and sex == '女':
    if bmi <= 18.5:
        print('你的BMI值为' + str(round(bmi, 2)) + '过轻' + ',' + '体脂率为:' + str(round(fat_rate(age,age), 1)) + '过轻')
    elif 18.5 < bmi < 25:
        print('你的BMI值为' + str(round(bmi, 2)) + '正常' + ',' + '体脂率为:' + str(round(fat_rate(age,age), 1)) + '正常')
    elif 25 < bmi < 28 | age > 60:
        print('你的BMI值为' + str(round(bmi, 2)) + '偏胖' + ',' + '体脂率为:' + str(round(fat_rate(age,age), 1)) + '偏胖')
    elif bmi > 32:
        print('你的BMI值为' + str(round(bmi, 2)) + '胖' + ',' + '体脂率为:' + str(round(fat_rate(age,age), 1)) + '很胖')



