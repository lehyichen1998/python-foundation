import csv
import os

file_location = r'D:\预科班\6自动化办公\In_Class\╥▀├τ┴≈╧≥│╟╩╨╖╓▓╝'
file = '╥▀├τ┴≈╧≥│╟╩╨╖╓▓╝'

# can read whole file in directory
lst = []
dirs = os.listdir(file_location)
for i in dirs:
    with open(file=file_location + '/' + i, mode='r', encoding='utf-8') as result:
        r = result.readlines()
        for k in r:
            a = k.replace('\n', ' ')
            lst.append(a)

# only can read one file in directory
# file_location = r'D:\预科班\6自动化办公\In_Class\╥▀├τ┴≈╧≥│╟╩╨╖╓▓╝\─■╧─╗╪╫σ╫╘╓╬╟°.csv'
# file = '╥▀├τ┴≈╧≥│╟╩╨╖╓▓╝'
# with open(file=file_location, mode='r', encoding='utf-8') as result:
#     r = result.read()
#     print(r)
# 1st version
# with open('writeFile.txt', mode='w', encoding='utf-8') as write_file:
#     for i in lst:
#         write_file.write(i)
# 2nd version
# with open('writeFile.txt', mode='w', encoding='utf-8') as write_file:
#     w_f = csv.writer(write_file)
#     for i in lst:
#         write_file.write(i)

#  3rd version
# with open('writeFile3.txt', mode='w', encoding='utf-8',newline='') as write_file:
#     w_f = csv.writer(write_file)
#     for i in lst:
#         w_f.writerow(i.split(','))

# 4nd version
with open('writeFile3.txt', mode='w', encoding='utf-8', newline='') as write_file:
    for i in lst:
        a = i.replace('\n', ' ')
        write_file.write(a)
