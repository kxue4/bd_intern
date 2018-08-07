#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 14:23
# @Author  : Kaiwen Xue
# @File    : 3c_processing.py
# @Software: PyCharm
import json


# cc = open('/Users/Kevin/Downloads/3c_2000.txt')

count = 0

for i in cc:
    count += 1

    data = json.loads(i.split('\t')[2])['result']
    data_length = len(data)
    tag_list = []

    query = data[0]['query']
    category = data[0]['category']
    trade = data[0]['trade']
    property = data[0]['properties']
    property_length = len(property)
    tag_list.append('category: ' + category)

    for j in range(0, property_length):

        if property[j]['key'] != 'category':
            tag_list.append(property[j]['key']+': ' + property[j]['value'])

        rst = ' '.join(tag_list)

    print(query + '\t' + rst)

print(count)