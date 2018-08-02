#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 14:00
# @Author  : Kaiwen Xue
# @File    : find_query.py
# @Software: PyCharm
import csv
from time import time


dec = open('/Users/Kevin/Downloads/decoration.txt')
new = open('/Users/Kevin/Downloads/dec/4.txt', 'w')

start = time()

tag_1 = 0
tag_2 = 0
tag_3 = 0
tag_m = 0
count = 0

for i in dec:
    qeury = i.split('\t')[0]  # query
    cate = i.split('\t')[1]
    extra = i.split('\t')[5]  # 增值服务
    model = i.split('\t')[6]  # 户型
    area = i.split('\t')[7]  # 面积
    process = i.split('\t')[8]  # 装修过程
    site = i.split('\t')[9]  # 工装场所
    part = i.split('\t')[10]  # 空间局部
    style = i.split('\t')[11]  # 风格
    purpose = i.split('\t')[12]  # 用途
    infor = i.split('\t')[13]  # 信息获取渠道

    furniture_kitchen = i.split('\t')[16]  # 品类(厨房) 集成灶 净水器 门窗 消毒柜
    furniture_bath = i.split('\t')[17]  # 品类(浴室) 洁具 卫浴

    brand_bath = i.split('\t')[19]  # 品牌(浴室)
    brand_ceramic = i.split('\t')[20]  # 品牌(陶瓷)
    brand_door = i.split('\t')[21]  # 品牌(门窗)
    brand_ceiling = i.split('\t')[22]  # 品牌(天花板)
    brand_lamp = i.split('\t')[23]  # 品牌(灯)
    brand_floor = i.split('\t')[24]  # 品牌(地板)
    brand_pipe = i.split('\t')[25]  # 品牌(管材)
    brand_paint = i.split('\t')[26]  # 品牌(油漆)
    brand_waterproof = i.split('\t')[27]  # 品牌(防水)
    brand_dirt = i.split('\t')[28]  # 品牌(硅藻泥)
    brand_stove = i.split('\t')[29]  # 品牌(集成灶)
    dec_comp = i.split('\t')[30]  # 装修公司
    dec_site = i.split('\t')[31]  # 装修平台
    dec_eng = i.split('\t')[32]  # 工装品牌
    intent = i.split('\t')[34]  # 价格(询价) 质量(获取口碑)

    program = i.split('\t')[15]  # 装修项目
    environ = i.split('\t')[14]  # 环保

    tag = 0
    tag_dict = dict()
    if extra != '':
        tag += 1
        tag_dict['增值服务'] = extra
    if model != '':
        tag += 1
        tag_dict['户型'] = model
    if area != '':
        tag += 1
        tag_dict['面具'] = area
    if process != '':
        tag += 1
        tag_dict['装修过程'] = process
    if site != '':
        tag += 1
        tag_dict['工装场所'] = site
    if part != '':
        tag += 1
        tag_dict['空间局部'] = part
    if style != '':
        tag += 1
        tag_dict['风格'] = style
    if purpose != '':
        tag += 1
        tag_dict['用途'] = purpose
    if infor != '':
        tag += 1
        tag_dict['信息获取渠道'] = infor
    if (furniture_bath != '' or furniture_kitchen != '' or brand_bath != '' or brand_ceramic != '' or brand_door != '' or brand_ceiling != '' or brand_lamp != '' or brand_floor != '' or brand_pipe != '' or brand_paint != '' or brand_waterproof != '' or brand_dirt != '' or brand_stove != '' or dec_comp != '' or dec_eng != '' or dec_site != ''):
        tag += 1
        pl = set()
        if furniture_bath != '':
            pl.add(furniture_bath)
        if furniture_kitchen != '':
            pl.add(furniture_kitchen)
        if brand_bath != '':
            pl.add('卫浴')
        if brand_ceramic != '':
            pl.add('陶瓷')
        if brand_door != '':
            pl.add('门窗')
        if brand_ceiling != '':
            pl.add('吊顶')
        if brand_lamp != '':
            pl.add('灯饰')
        if brand_floor != '':
            pl.add('地板')
        if brand_pipe != '':
            pl.add('管材')
        if brand_paint != '':
            pl.add('油漆涂料')
        if brand_waterproof != '':
            pl.add('防水材料')
        if brand_dirt != '':
            pl.add('硅藻泥')
        if brand_stove != '':
            pl.add('集成灶')
        if dec_comp != '':
            pl.add('装修公司')
        if dec_eng != '':
            pl.add('工装品牌')
        if dec_site != '':
            pl.add('装修平台')
        tag_dict['品类'] = pl

    if (brand_bath != '' or brand_ceramic != '' or brand_door != '' or brand_ceiling != '' or brand_lamp != '' or brand_floor != '' or brand_pipe != '' or brand_paint != '' or brand_waterproof != '' or brand_dirt != '' or brand_stove != ''):
        tag += 1
        brand = set()
        if brand_bath != '':
            brand.add(brand_bath)
        if brand_ceramic != '':
            brand.add(brand_ceramic)
        if brand_door != '':
            brand.add(brand_door)
        if brand_ceiling != '':
            brand.add(brand_ceiling)
        if brand_lamp != '':
            brand.add(brand_lamp)
        if brand_floor != '':
            brand.add(brand_floor)
        if brand_pipe != '':
            brand.add(brand_pipe)
        if brand_paint != '':
            brand.add(brand_paint)
        if brand_waterproof != '':
            brand.add(brand_waterproof)
        if brand_dirt != '':
            brand.add(brand_dirt)
        if brand_stove != '':
            brand.add(brand_stove)
        tag_dict['品牌'] = brand

    if '环保' in environ:
        tag += 1
        tag_dict['关注点'] = 'intent:环保'
    if program != '':
        tag += 1
        tag_dict['装修项目'] = program
    if '询价' in intent:
        tag += 1
        tag_dict['关注点'] = 'intent:价格'
    if '获取口碑' in intent:
        tag += 1
        tag_dict['关注点'] = 'intent:质量'

    if tag == 4:
        new.writelines(qeury + '\t' + str(tag_dict) + '\n')
        count += 1

end = time()

print('Time:', round(end-start, 1), 'seconds')
print('Total:', count)

# 预算	0-10万，10-20万，20-30万，30万-50万，50万以上
# 风水		厨房和卫生间对着好吗                                                                       装修的风水注意点