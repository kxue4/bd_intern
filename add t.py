#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 16:03
# @Author  : Kaiwen Xue
# @File    : add t.py
# @Software: PyCharm
import time

same = set()
print('start')
start = time.time()
with open('car_not_sample.txt', 'r') as f1:
    with open('c_not_sample.txt', 'w') as f2:
        for lines in f1:
            if lines not in same:
                new_lines = lines + '\n'
                f2.write(new_lines)
                same.add(lines)
ends = time.time()

print('time:', ends-start)
print('end')