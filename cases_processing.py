#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/9 10:30
# @Author  : Kaiwen Xue
# @File    : cases_processing.py
# @Software: PyCharm
import csv
from random import randint


bc = open('/Users/Kevin/Downloads/kg_badcase_167.txt')
lost = open('/Users/Kevin/Downloads/kg_serires-version缺失_193.txt')
wrong = open('/Users/Kevin/Downloads/kg_series-version识别错误_83.txt')
ac = open('/Users/Kevin/Downloads/kg_cases_1824.txt')

bc_c = 0
lost_c = 0
wrong_c = 0
ac_c = 0

for i in bc:
    bc_c += 1

for i in lost:
    lost_c += 1

for i in wrong:
    wrong_c += 1

for i in ac:
    ac_c += 1

print('bad cases:', bc_c)
print('lost:', lost_c)
print('wrong:', wrong_c)
print('all cases:', ac_c)
print('召回:', 1-(bc_c/ac_c))
print('准确:', 1-((lost_c+wrong_c)/(ac_c-bc_c)))
