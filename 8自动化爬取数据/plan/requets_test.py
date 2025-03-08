'''
爬虫项目：
    目标地址：
    https://my.xiapibuy.com/
    http:
    无状态：协议对客户端没有状态存储，对事物处理没有“记忆”能力，比如访问一个网站需要反复进行登录操作
    无连接：简单快速、灵活
    通信使用明文、请求和响应不会对通信方进行确认、无法保护数据的完整性
    价格便宜
    https:
    基于HTTP协议，通过SSL或TLS提供加密处理数据、验证对方身份以及数据完整性保护
    安全性高，传输效率比http更高

    总结：
        如果学习使用，就购买http协议的服务网站
        如果商用，业务较大，那么可以采用https协议部署网站；

    get请求方式:
        get效率 相对 post低
        GET产生一个TCP数据包；
        简单说get请求没有post请求安全
    post请求方式:
        post效率高
        POST产生两个TCP数据包。
        简单说post要比get安全
    常用爬虫方式
        Scrapy  大而全（一件运行抓取任何网站数据）
        requests  抓包快捷（用于练习）
        selenium  驱动浏览器实现信息抓取（常用于自动化测试）
     今日任务：
        对shopee的商品信息进行爬取；

        商品信息进行爬取，获取商品的名称，价格，地址，销量，以及商品图片

'''
import json
import os
from itertools import groupby
import requests
import csv
from pyecharts.charts import Bar
from pyecharts.options import global_options as opts
# 带他们认识反爬虫
url = 'https://my.xiapibuy.com/api/v2/search_items/?by=relevancy&keyword=nike%20air%20force&limit=50&newest=0&order=desc&page_type=search&version=2'
header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
respones = requests.get(url=url,headers=header)
result = respones.text
# loads()转字典 使用导入json的方法
# dc_str = json.loads(result)
# .json转字典 ,使用自带的json方法
dc_str = respones.json()
# 拿到里面的items的数据，那么items有50条数据
d = dc_str['items']
# name,price,historical_sold,shop_location
lis_txt = []
for i in d:
    li = [i['name'],int(i['price'])//100000,i['historical_sold'],i['shop_location']]
    lis_txt.append(li)
# print(lis_txt)
# 写入到csv中
csv_file = '商品文字信息.csv'
os.mkdir('./商品图片')
image_file = './商品图片'
with open(csv_file,'w',encoding='utf-8',newline='') as w_file:
    # 写入商品 名称 信息
    filename = ["商品名称","商品价格","商品销量","商品地址"]
    writer = csv.DictWriter(w_file, fieldnames=filename)
    writer.writeheader()
    # 写入商品信息 ；
    csv_file = csv.writer(w_file)
    for i in lis_txt:
        print(i)
        csv_file.writerow(i)


'''
根据商品的 价格进行排序 实现数据可视化展示；
'''


# 导入商品文件
# shop_data = r'D:\新基础课程\lesson_20spider_about\in_clas\商品文字信息.csv'
# price_lst = []
# with open(shop_data,'r',encoding='utf-8') as r_f:
#     r = r_f.readlines()  # 一共读到51 条数据；
#     print(r)
#     for i in range(1,len(r)):  # 从列表的第二个元素开始读；
#         # 切片获取 对应的数值，拿到 每个列表中每第3个的元素；
#         print(i) # 这个时候我们发现i是索引
#         price_lst.append((r[i]).split(',')[-3])  # 将处理好的 数据 保存在price_lst中；

# 整理列表；
# new_list =[]
# lst_data = []
# for k, g in groupby(sorted(price_lst), key=lambda x: int(x)//50):
#     # 原数据
#     # print('{}-{}:{}'.format(int(k) * 10, (int(k) + 1) * 10 - 1, len(list(g))))
#     lst_data.append(len(list(g)))  # 出现的次数
#     # 将处理好的数据添加值 new_list列表中
#     new_list.append(str(int(k)*50)+'-'+str((int(k)+1)*50-1))


# bar = (
#     Bar()
#     # 所有的数据都是根据x轴来衡量定制的，也就是有多少商品才显示有多少数据
#     .add_xaxis([i for i in new_list])
#     # 分析商家的 金额数据  在y轴上 有多少 统计 当前金额的相关数据；
#     .add_yaxis("价格评率", lst_data)
#     # 设置标题 的名称主标题，副标题；
#     .set_global_opts(title_opts=opts.TitleOpts(title="air force1", subtitle="商家的价格区间"))
# )
# bar.render('价格区间.html')


# 开始保存页面的图片信息、
# 开始分析页面，首先我们得找到文件夹


# 图片的爬取；
lis_images = []
for i in d:
    r = i['images']
    lis_images.append(r)
    print(r)


for items in lis_images:  # lis_images里面有多少数据，遍历多少次
    for j in items:
        print(j)
        with open(image_file+'/'+j+'.jpg', 'wb') as w_file:
            # 我现在拿到了lis_images,里面每条数据
            print('正在下载图片')
            url = 'https://cf.shopee.com.my/file/'
            # header ={
            #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
            # }
            print(url + j + '_tn')
            # images = requests.get(url=(url+j+'_tn'))
            # w_file.write(images.content)
            # print('已完成图片下载')












