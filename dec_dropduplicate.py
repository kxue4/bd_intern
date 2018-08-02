#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 16:17
# @Author  : Kaiwen Xue
# @File    : dec_dropduplicate.py
# @Software: PyCharm

gd = open('/Users/Kevin/Downloads/dec/good_query_828.txt')

count = 0
for i in gd:
    tag = i.split('\t')[1]
    if '质量' in tag:
        print(i)
        count += 1

print(count)

# 增值服务
# 户型
# 面积
# 装修过程
# 工装场所
# 空间局部
# 风格
# 用途
# 信息获取渠道
# 品牌
# 品类
# 装修项目
# 环保
# 价格
# 质量
# 关注点