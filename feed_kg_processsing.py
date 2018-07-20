#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/9 10:30
# @Author  : Kaiwen Xue
# @File    : feed_kg_processsing.py
# @Software: PyCharm
import re

# STEP 1
# phone_s = open('/Users/Kevin/Downloads/phone_s.txt')
# phone_n = open('/Users/Kevin/Downloads/phone_n.txt')
# car_v = open('/Users/Kevin/Downloads/car_v.txt')
# car_n = open('/Users/Kevin/Downloads/car_n.txt')
#
# query_re = '"query": ".*", "sign"'
# series = '0, "value": "(.+?)", "key": "series"'
#
# count = 0
# ex = 0
# for lines in phone_n:
#     try:
#         query = re.findall(r'"query": "(.+?)", "sign', lines)
#         # series = re.findall(r'0, "value": "(.+?)", "key": "series"', lines)
#         print(query[0]) # +'\t'+str(series)
#         count += 1
#     except IndexError:
#         ex += 1
#
# print(count, ex)

# STEP 2
# phone_w = open('/Users/Kevin/Downloads/phone_wrong.txt')
# phone_l = open('/Users/Kevin/Downloads/phone_lost.txt')
# car_w = open('/Users/Kevin/Downloads/car_wrong.txt')
# car_l = open('/Users/Kevin/Downloads/car_lost.txt')
# bc = open('/Users/Kevin/Downloads/car_badcase.txt')
#
# count = 0
# c_b = bc.readlines()
# car_n = open('/Users/Kevin/Downloads/car_n.txt')
#
# for lines in car_n:
#     query = re.findall(r'"query": "(.+?)", "sign', lines)
#
#     for cases in c_b:
#         qy = cases.strip().split('\t')
#         if query[0] == qy[0]:
#             count += 1
#             print(lines)
#
# print(count)

# STEP 3
# a = open('/Users/Kevin/Downloads/未命名文件夹/phone_wrong_111.txt')
# count = 0
# aa = 0
# for lines in a:
#     count += 1
#     lines = lines.strip()
#     bb = lines.split('\n')
#     if count % 2 != 0:
#         print(bb[0])
#         aa+=1
#
# print(count,aa)








import re
import random
# all = open('/Users/Kevin/Downloads/all_444.txt')
# lst = open('/Users/Kevin/Downloads/lst.txt', 'w')
# wr = open('/Users/Kevin/Downloads/wr.txt', 'w')
#
# lost = 0
# wrong = 0
#
# for lines in all:
#     query = re.findall(r'"query": "(.+?)", "sign', lines)
#
#     if re.findall(r'0, "value": "(.+?)", "key": "series"', lines):
#         series = re.findall(r'0, "value": "(.+?)", "key": "series"', lines)
#         wr.writelines(query[0]+'\t'+str(series)+'\n')
#         wrong += 1
#     else:
#         lst.writelines(query[0]+'\n')
#         lost += 1
#
# print(wrong, lost)

# lost 1349151
# wrong 565583

# wrong 156
# sum 556
# need 444

# ll = open('/Users/Kevin/Downloads/lst.txt')
# # badcase = open('/Users/Kevin/Downloads/lost_85.txt')
#
# lost = ll.readlines()
#
# pl = open('/Users/Kevin/Downloads/all_444.txt')
#
# a = 0
# for lines in pl:
#     query = re.findall(r'"query": "(.+?)", "sign', lines)
#     for qs in lost:
#         temp = qs.strip()
#         if query[0] == temp:
#             print(lines.strip())
#             a += 1
#
# print(a)