#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 11:38
# @Author  : Kaiwen Xue
# @File    : phone_query_expand.py
# @Software: PyCharm
from time import time


def phone_query_expand():
    results = []
    hot_phone_lists = ['红米4X', '红米Note4X', '荣耀畅玩6', '荣耀畅玩6x', '华为nova', 'iPhone6s', '荣耀10', 'iPhone8', 'iPhone X',
                   '华为畅享6', '华为Mate10', 'iPhone7', '小米6X', '荣耀V10', '华为P10', '华为P10 Plus', '荣耀9青春版', '坚果3',
                   '小米Mix2', '华为P20', '小米8', '红米Note5', '荣耀畅玩7x', '小米Note3', '360 N7', '坚果Pro2', '三星S9',
                   'vivoX21', '诺基亚7', '坚果R1', '荣耀畅玩7A', 'vivoY75', '360 N6', '小米5', 'vivoY69', '魅族Pro7',
                   '三星S8', '华为畅享8 Plus', 'OPPOR11', 'OPPOR15', '荣耀9', '小米Max2', '魅蓝5s', 'OPPOA3', 'vivoY85',
                   'OPPOA1', '美图V6', '华为麦芒5', '魅蓝6', '红魔游戏手机', 'vivoX20', '魅蓝Note6', '努比亚Z17', '美图T8',
                   '魅族Pro6', 'OPPOA73', '三星Note8', '一加6', '联想S5', '诺基亚X6', '三星GalaxyS9', '魅族15', 'vivoZ1',
                   '联想Z5', '华为nova3e', '小米7', '荣耀Play', '小米MIX 2s', 'vivoY83', '黑鲨游戏手机', 'vivoY71',
                   '联想K5 Note', '华为畅享8e', '荣耀9i', '联想A5', '小米5X', 'vivoX9s', '华为畅享7', 'OPPOA57', '华为麦芒6',
                   '华为nova2', 'vivoY66', '美图M8s']
    phone_description = ['多少钱', '报价', '价格', '配置', '今日报价', '参数', '图片', '全网通', '售价', '跑分', '续航', '拍照',
                         '像素', '怎么样']
    brand_lists = ['vivo', 'OPPO', '三星', '华为', '荣耀', '苹果', '一加', '努比亚', '国美', '联想', '小米', '魅族', 'Moto',
                   '锤子', '中兴', '360', '诺基亚', '金立', '黑鲨', 'HTC', '索尼']
    brand_description = ['手机怎么样', '手机价格', '新款手机', '手机报价', '手机官网', '手机大全']

    for phone in hot_phone_lists:

        for words in phone_description:

            results.append(phone + words)

    for brand in brand_lists:

        for words in brand_description:

            results.append(brand + words)

    return set(results)


if __name__ == '__main__':
    print('==============================Script running==============================\n')
    start = time()

    lists = phone_query_expand()
    print(len(lists))

    for query in lists:
        print(query)

    ends = time()
    print('\n\n\t\t\t\t\t\t\tRunning time:', str(round(ends - start, 2)) + 's')
    print('\n==================================Ends==================================\n')