#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 10:37
# @Author  : Kaiwen Xue
# @File    : aig_processing.py
# @Software: PyCharm
import re

bad = open('/Users/Kevin/Desktop/kg_output_result/kg_badcase_167.txt')
path = '/Users/Kevin/Desktop/aig/'

aig_c = open(path + 'aig_c.txt')
aig_p = open(path + 'aig_p.txt')
aig_e = open(path + 'aig_e.txt')

badcase = bad.readlines()
bad = set()
all = set()

a = 0
b = 0
for lines in aig_p:
    all.add(lines.strip())
    query = lines.split('\t')[0]
    for bds in badcase:
        temp = bds.split('\t')[0]
        badone = temp.split('|')[1]
        if query == badone:
            bad.add(lines.strip())

good = all-bad

for lines in good:
    print(lines)

print(len(good))


# aig_c_n = open(path +'aig_c_n.txt')
# aig_c_v = open(path + 'aig_c_v.txt')
# aig_p_n = open(path + 'aig_p_n.txt')
# aig_p_s = open(path + 'aig_p_s.txt')
#
# c_n = open(path + 'c_n .txt', 'w')
# c_v = open(path + 'c_v.txt', 'w')
# p_n = open(path + 'p_n.txt', 'w')
# p_s = open(path + 'p_s.txt', 'w')
#
# for lines in aig_c_n:
#     query = lines.split('\t')[0]
#     desc = re.findall(r'"desc":"(.+?)","import', lines)
#     mention = re.findall(r'"mention":"(.+?)","offset"', lines)
#     c_n.writelines(query + '\t' + str(desc) + '\t' + str(mention) + '\n')
#
# for lines in aig_c_v:
#     query = lines.split('\t')[0]
#     desc = re.findall(r'"desc":"(.+?)","import', lines)
#     mention = re.findall(r'"mention":"(.+?)","offset"', lines)
#     c_v.writelines(query + '\t' + str(desc) + '\t' + str(mention) + '\n')
#
# for lines in aig_p_n:
#     query = lines.split('\t')[0]
#     desc = re.findall(r'"desc":"(.+?)","import', lines)
#     mention = re.findall(r'"mention":"(.+?)","offset"', lines)
#     p_n.writelines(query + '\t' + str(desc) + '\t' + str(mention) + '\n')
#
# for lines in aig_p_s:
#     query = lines.split('\t')[0]
#     desc = re.findall(r'"desc":"(.+?)","import', lines)
#     mention = re.findall(r'"mention":"(.+?)","offset"', lines)
#     p_s.writelines(query + '\t' + str(desc) + '\t' + str(mention) + '\n')
#
# print('Finished!')