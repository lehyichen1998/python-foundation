lst = ['第一条数据\n','第二条数据\n','第三条数据\n','第四条数据\n']

# 这是字符串切片
# for i in lst:
#     print(i.split(','))
li = []
# 换行
for i in lst:
    # r = i.replace('\n','')
    li.append(i)


print(li)