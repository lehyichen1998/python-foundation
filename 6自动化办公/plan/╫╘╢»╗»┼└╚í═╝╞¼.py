#自动化爬取网页图片
from selenium import webdriver
import time
from  lxml import etree
import os
import requests

web = webdriver.Chrome()
web.get('https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E6%AC%A7%E9%98%B3%E5%A8%9C%E5%A8%9C')
#模拟人翻动网页
for i in range(5):
    time.sleep(1)
    js = 'var a = document.documentElement.scrollTop=4000'
    web.execute_script(js)
#将页面的代码转换成python能懂得代码
html = etree.HTML(web.page_source)
#通过循环来找

li =[]
div = html.xpath('.//div[@class="imgpage"]/ul/li')
for j in div:
    img = j.xpath('.//img[@class="main_img img-hover"]/@data-imgurl')[0]
    li.append(img)
    print(img)
#新建一个文件夹
os.mkdir('./欧阳娜娜')
for k in li:
    s= k.split('/')[-1]
    name ='./欧阳娜娜/'+s
    with open(name,'wb') as dc:
        result = requests.get(k)
        dc.write(result.content)
web.close()





