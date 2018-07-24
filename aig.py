# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2018/7/23 16:01
# # @Author  : Kaiwen Xue
# # @File    : aig.py
# # @Software: PyCharm
import re
import time
import csv
import requests
from bs4 import BeautifulSoup
#
# dmp = open('/Users/Kevin/Desktop/new/dmp_query_1800.txt')
# aig_p = open('/Users/Kevin/Desktop/new/aig_phone.txt', 'w')
# aig_c = open('/Users/Kevin/Desktop/new/aig_car.txt', 'w')
# aig_e = open('/Users/Kevin/Desktop/new/aigelse.txt', 'w')
#
# count = 0
# for lines in dmp:
#     query = re.findall(r'"query": "(.+?)", "sign', lines)
#     try:
#         type = re.findall(r'"trade": "(.+?)", "query', lines)[0]
#     except IndexError:
#         type = 0
#     url = 'http://10.90.85.37:8830/GraphLinkingService/Linking?query='
#     res = requests.get(url + query[0])
#     res.encoding = 'gb2312'
#     soup = BeautifulSoup(res.text, 'lxml')
#     result = soup.p.get_text()
#
#     if type == 'phone':
#         aig_p.writelines(query[0] + '\t' + str(result))
#
#     elif type == 'car':
#         aig_c.writelines(query[0] + '\t' + str(result))
#
#     else:
#         aig_e.writelines(query[0] + '\t' + str(result))
#
#     time.sleep(0.15)
#     count += 1
#     print(str(count)+'/1800'+'\t'+str(round(count*100/1800,1))+'%')
#
# print('finish!')
# # # csvfile = open('', 'w')
# # csvfile.writelines(['Query', 'DMP', 'AIG', 'DMP_result', 'AIG_result'])
# #
# #
# # for lines in kg:
# #
# #
# #     url = 'http://10.90.85.37:8830/GraphLinkingService/Linking?query='
# #     query = '宝马x1多少钱'
# #
# #     res = requests.get(url+query)
# #     res.encoding = 'gb2312'
# #     soup = BeautifulSoup(res.text, 'lxml')
# #     aig = soup.p.get_text()
# #     time.sleep(0.15)
#
# c_n_v = open('/Users/Kevin/Desktop/new/car_no_version_400.txt')
# c_v = open('/Users/Kevin/Desktop/new/car_version_400.txt')
# p_n_s = open('/Users/Kevin/Desktop/new/phone_no_series_400.txt')
# p_s = open('/Users/Kevin/Desktop/new/phone_series_380.txt')
#
# aig_p_s = open('/Users/Kevin/Desktop/new/aig_p_s.txt', 'w')
# aig_p_n = open('/Users/Kevin/Desktop/new/aig_p_n.txt', 'w')
# aig_c_v = open('/Users/Kevin/Desktop/new/aig_c_v.txt', 'w')
# aig_c_n = open('/Users/Kevin/Desktop/new/aig_c_n.txt', 'w')
# count = 0
#
# for lines in c_n_v:
#     query = lines.strip()
#     url = 'http://10.90.85.37:8830/GraphLinkingService/Linking?query='
#     res = requests.get(url + query)
#     res.encoding = 'gb2312'
#     soup = BeautifulSoup(res.text, 'lxml')
#     result = soup.p.get_text()
#
#     aig_c_n.writelines(query + '\t' + str(result))
#
#     time.sleep(0.15)
#     count += 1
#     print(str(count) + '/1580' + '\t' + str(round(count * 100 / 1580, 1)) + '%')
#
# for lines in c_v:
#     lines = lines.strip()
#     temp = lines.split('[')
#     query = temp[0].strip()
#     url = 'http://10.90.85.37:8830/GraphLinkingService/Linking?query='
#     res = requests.get(url + query)
#     res.encoding = 'gb2312'
#     soup = BeautifulSoup(res.text, 'lxml')
#     result = soup.p.get_text()
#
#     aig_c_v.writelines(query + '\t' + str(result))
#
#     time.sleep(0.15)
#     count += 1
#     print(str(count) + '/1580' + '\t' + str(round(count * 100 / 1580, 1)) + '%')
#
# for lines in p_n_s:
#     query = lines.strip()
#     url = 'http://10.90.85.37:8830/GraphLinkingService/Linking?query='
#     res = requests.get(url + query)
#     res.encoding = 'gb2312'
#     soup = BeautifulSoup(res.text, 'lxml')
#     result = soup.p.get_text()
#
#     aig_p_n.writelines(query + '\t' + str(result))
#
#     time.sleep(0.15)
#     count += 1
#     print(str(count) + '/1580' + '\t' + str(round(count * 100 / 1580, 1)) + '%')
#
# for lines in p_s:
#     lines = lines.strip()
#     temp = lines.split('[')
#     query = temp[0].strip()
#     url = 'http://10.90.85.37:8830/GraphLinkingService/Linking?query='
#     res = requests.get(url + query)
#     res.encoding = 'gb2312'
#     soup = BeautifulSoup(res.text, 'lxml')
#     result = soup.p.get_text()
#
#     aig_p_s.writelines(query + '\t' + str(result))
#
#     time.sleep(0.15)
#     count += 1
#     print(str(count) + '/1580' + '\t' + str(round(count * 100 / 1580, 1)) + '%')

query = open('/Users/Kevin/Desktop/new/dmp_query_1800.txt')
cv = open('/Users/Kevin/Desktop/new/car_version_400.txt')
ps = open('/Users/Kevin/Desktop/new/phone_series_380.txt')

f_f = open('/Users/Kevin/Desktop/new/feed.txt', 'w')

q_l = list()
for lines in ps:
    temp = lines.split('[')[0].strip()
    print(temp)