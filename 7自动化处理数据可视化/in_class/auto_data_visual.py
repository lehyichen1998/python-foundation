# pyecharts
import pandas as pd
from pyecharts.charts import Line, Pie, Bar

data = pd.read_csv(r'D:\预科班\7自动化处理数据可视化\7╡┌╞▀┐╬╫╘╢»╗»┤ª└φ╩²╛▌┐╔╩╙╗»\╢╣░Ω╙├╗º╞└╖╓╨┼╧ó.csv', encoding='gbk')
# print(data)

# for i in data:
#     print(i)

sc_data = data['scores']
dc = {}
# li = []
# for i in sc_data:
#     li.append(i)
#     print(i)
# print('total: %s'%len(li))

for i in sc_data:
    if str(i) not in dc:
        dc[str(i)] = 0
    else:
        dc[str(i)] = dc[str(i)] + 1
#
# # print(dc)
# for i in dc.items():
#     print(i,end='')

# (Line Chart)
line = (
    # X,Y
    Line().add_xaxis([k for k in dc]).add_yaxis('星级选择', [dc[n] for n in dc])
).render('lineChart.html')

# print('dc: ', dc)
# print([dc[n] for n in dc])
# Bar Chart
bar = (
    Bar().add_xaxis([k for k in dc]).add_yaxis('星级选择', [dc[n] for n in dc])
).render('BarChart.html')

# Pie Chart
key_list = []
value_list = []
for i in dc:
    key_list.append(i)
    value_list.append(dc[i])

# print('key_list:', key_list)
# print('value_list:', value_list)
pie = (
    Pie().add(series_name='有病影评', data_pair=[i for i in zip(key_list,value_list)])
).render('PieChart.html')
