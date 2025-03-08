########3  数据分析 他们的价格 ；
# 关于 pyecharts 的柱状图分析；

from pyecharts.charts import Bar
from pyecharts.options import global_options as opts
from itertools import groupby
# 导入商品文件
shop_data = r'D:\新基础课程\lesson_20spider_about\in_clas\商品文字信息.csv'
price_lst = []
with open(shop_data,'r',encoding='utf-8') as r_f:
    r = r_f.readlines()
    for i in r:
        # 切片获取 对应的数值
        price_lst.append(i.split(',')[-3])



# 整理列表；
new_list =[]
lst_data = []
for k, g in groupby(sorted(price_lst), key=lambda x: int(x)//50):
    # 原数据
    # print('{}-{}:{}'.format(int(k) * 10, (int(k) + 1) * 10 - 1, len(list(g))))
    lst_data.append(len(list(g)))  # 出现的次数
    # 将处理好的数据添加值 new_list列表中
    new_list.append(str(int(k)*50)+'-'+str((int(k)+1)*50-1))



bar = (
    Bar()
    # 所有的数据都是根据x轴来衡量定制的，也就是有多少商品才显示有多少数据
    .add_xaxis([i for i in new_list])
    # 分析商家的 金额数据  在y轴上 有多少 统计 当前金额的相关数据；
    .add_yaxis("价格评率", lst_data)
    # 设置标题 的名称主标题，副标题；
    .set_global_opts(title_opts=opts.TitleOpts(title="air force1", subtitle="商家的价格区间"))
)
bar.render('价格区间.html')
