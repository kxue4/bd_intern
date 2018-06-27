#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 16:03
# @Author  : Kaiwen Xue
# @File    : txt_transfer.py
# @Software: PyCharm
import time


def txt_transfer(file, new_file):
    same = set()

    with open(file + '.txt', 'r') as f1:

        with open(new_file + '.txt', 'w') as f2:

            for lines in f1:

                if lines not in same:
                    new_lines = lines + '\n'
                    f2.write(new_lines)
                    same.add(lines)


if __name__ == '__main__':
    file = 'test'
    new_file = 'result'
    print('==============================Script running==============================\n')
    start = time.time()
    txt_transfer(file, new_file)
    ends = time.time()
    print('\n\n\t\t\t\t\t\t\tRunning time:', str(round(ends - start, 2)) + 's')
    print('\n==================================Ends==================================\n')
