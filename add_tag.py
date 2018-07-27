#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 16:45
# @Author  : Kaiwen Xue
# @File    : add_tag.py
# @Software: PyCharm


file = open('/Users/Kevin/Downloads/相机-产品类型.txt')
new = open('/Users/Kevin/Downloads/taged.txt', 'w')

for lines in file:
    tag_dict = dict()
    lines = lines.strip()
    print(lines)
    ipt = input('Input tags: ')
    tags = ipt.split(',')
    lth = len(tags)

    key = 0
    for i in range(0, lth):

        if i %2 == 0:
            key = tags[i]

        else:
            tag_dict[key] = tags[i]

    new.writelines(lines + '\t' + str(tag_dict) + '\n')