from itertools import groupby
# 导入商品文件
shop_data = r'D:\新基础课程\lesson_20spider_about\in_clas\商品文字信息.csv'
price_lst = []
with open(shop_data,'r',encoding='utf-8') as r_f:
    r = r_f.readlines()
    for i in r:
        # 切片获取 对应的数值
        price_lst.append(i.split(',')[-3])

# price_lst = [10,20,30,50,100,100,150,120,130,110,140,200,180,190,150,150,140,30,50]

# for k,g in groupby(price_lst):   k: 10 g: <itertools._grouper object at 0x0000020FD7D66198>
#     print('k:',k,'g:',g)


# sorted函数自动对 该列表进行排序 ，并将 重复元素过滤
# for k,g in groupby(sorted(price_lst)):
#     print('k:',k,'g:',g)

# 那么我们要 拿 1-50 区间的数值 ，50-100之间的数值该怎么去拿？
# for k,g in groupby(sorted(price_lst),key=lambda x:int(x)//50):   # 根据50 为一个区间进行排序
#     print('k:',k,'g:',g)     # 我们可以拿到 5个区间对象  k: 0 g: <itertools._grouper object at 0x000002360C376160>


# 将 列表中的str 类型一行转成 int类型；
price_lst = [int(i) for i in price_lst]
# 那么 他们的区间我们拿到了 他们的条数在哪里呢？
for k,g in groupby(sorted(price_lst),key=lambda x: int(x)//50):
    # print('k:',k,'g:',g)
    # 其实我们已经拿到了数据，只是在对象中我们看不出来而已~,让我们将它展示出来
    # 第一个k的区间       编写算法实现第二个 区间       总体个数；
    # print(int(k)*50, '-', (int(k)+1)*50-1, ':', len(list(g))) # 第一种写法
    # 第二种写法
    print('{}-{}:{}'.format(int(k) * 50, (int(k) + 1) * 50 - 1, len(list(g))))

# 整理列表；
new_list = []    # 保存区间数据
lst_data = []   # 保存价位区间数据
# groupby 是一种排序的 方法 根据list进行安排续 ；
# for k, g in groupby(sorted(price_lst), key=lambda x: int(x)//50):
#     # 原数据
#     print('{}-{}:{}'.format(int(k) * 50, (int(k) + 1) * 50 - 1, len(list(g))))
#     # lst_data.append(len(list(g)))  # 出现的次数
#     # 将处理好的数据添加值 new_list列表中
#     # new_list.append(str(int(k)*50)+'-'+str((int(k)+1)*50-1))
#     print('k:',k,'g:',g)
#     pass
