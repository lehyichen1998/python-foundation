import csv

import requests

# url = 'https://my.xiapibuy.com/'
url = 'https://my.xiapibuy.com/api/v2/search_items/?by=relevancy&keyword=nike%20force%201&limit=50&newest=0&order=desc&page_type=search&version=2'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
response = requests.get(url=url, headers=header)  # url and header from web inspect
json_str = response.text
# print(json_str)

dc_str = response.json()
# print('dc_str: ',dc_str)

shop_data = dc_str['items']  # form web inspect
# print(shop_data)
lst = []
lst_data = []
for i_dc in shop_data:
    # get data from web
    li = [i_dc['name'], i_dc['price'] / 100000, i_dc['historical_sold'], i_dc['shop_location']]  # from web inspect
    # lst.append(i)
    lst_data.append(li)
    # print(li)
# print('一共有%s数据' % len(lst))
# print(lst_data)
csv_file = 'Nike_data.csv'
with open(csv_file,mode='w',encoding='utf-8',newline='') as w_file:
    li_file_title = ['name', 'price', 'quantity', 'address']
    writer = csv.DictWriter(w_file, fieldnames=li_file_title)
    writer.writeheader()  # writer header

    # write items data
    csv_file = csv.writer(w_file)
    for i in lst_data:
        csv_file.writerow(i)
