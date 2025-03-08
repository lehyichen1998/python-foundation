'''

采集数据为主：
爬虫： scraper ： spider；
    数据 ：音乐，视频，图片 ，文本 ；
    基于爬虫的数据 实现 商品价格区间展示；


爬虫项目：
    目标地址：
    https://my.xiapibuy.com/   # 老版本的虾皮网站
    https://shopee.com.my/    # 新版本 虾皮网站    安全性更高
认识网络传输协议：
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

请求方式 web页面 html ：
    get请求方式:
        get效率 相对 post低
        GET产生一个TCP数据包；
        简单说get请求没有post请求安全
    post请求方式:
        post效率高
        POST产生两个TCP数据包。
        简单说post要比get安全
常用爬虫方式
        Scrapy框架     大而全（一件运行抓取任何网站数据）
        requests -->请求  service    -->  响应 (数据)    抓包快捷（用于练习）
        selenium 库； 驱动浏览器实现信息抓取（常用于自动化测试）
     今日任务：
        对shopee的商品信息进行爬取；

        商品信息进行爬取，获取商品的名称，价格，地址，销量，以及商品图片
'''

# 模拟人去上网
import requests
import csv
# url = 'https://my.xiapibuy.com/'  # <Response [200]>表示响应成功！
url = 'https://my.xiapibuy.com/api/v2/search_items/?by=relevancy&keyword=nike%20air%20force%201&limit=50&newest=0&order=desc&page_type=search&version=2'
# 爬虫是没有头的，不能像人一样打开浏览器 去访问数据，为爬虫代码 制造出一个请求头；
header = {
    # "key":"value",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
}
response = requests.get(url=url, headers=header)
json_str = response.text   #  response.text这个对象就是 json数据
print(type(json_str))   # 默认的数据类型是str

# 第一步： 分析页面D
# 所有网页上的数据绝大部分都是打包在了 json数据中  json = dict    json = {"name":"chugu","age":'25',"hobby":"coding"}
# js 解密： 解除 加密的数据； 爬虫学习

# 第二步：找到这个页面；
# ?by=relevancy&keyword=nike%20air%20force%201&limit=50&newest=0&order=desc&page_type=search&version=2


# 第三步：处理数据；
dc_str = response.json()
# print('dc_str类型:',type(dc_str))

# 取出item中的数据
shop_data = dc_str['items']
# print(shop_data)   # 那么我们还有很多的，商品 名称，价格，地址，销量

# for 循环遍历 shop_data对象
# 床架一个列表统计 所有的商品对象数
lst = []
# 将数据保存起来
lst_data =[]
for i_dc in shop_data:
    # 取出页面的  名称，价格，地址，销量 信息； i
    li = [i_dc['name'],int(i_dc['price'])//100000,i_dc['historical_sold'],i_dc['shop_location']]
    lst_data.append(li)

# print('一共有%s数据'%len(lst))
# print(lst_data)

# 第四部：将数据保存到 文档中
# 找到文档路径，没有则创建一个文档路径
csv_file = 'nike_data.csv'
with open(csv_file,mode='w',encoding='utf-8',newline='') as w_file:
    # 写入商品 信息， 标题
    lis_file_title = ['商品名称','商品价格','商品销量','发货地址']
    wrier = csv.DictWriter(w_file,fieldnames=lis_file_title)
    wrier.writeheader()  # 写入头部信息；

    # 接着我们开始写商品信息
    csv_file = csv.writer(w_file)
    for itemsssssssssssssssssssssssssssssssssssss in lst_data:  # 遍历所有数据
        csv_file.writerow(itemsssssssssssssssssssssssssssssssssssss)












