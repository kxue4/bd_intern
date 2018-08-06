#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/6 17:13
# @Author  : Kaiwen Xue
# @File    : boson_nlp.py
# @Software: PyCharm
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
import requests
import json


token = '8vE1y5w3.26891.HXpAR_Iogezg'  # 个人API

nlp = BosonNLP(token)


def check_limits():
    """
    Check limits remaining
    """
    HEADERS = {'X-Token': token}
    RATE_LIMIT_URL = 'http://api.bosonnlp.com/application/rate_limit_status.json'
    result = requests.get(RATE_LIMIT_URL, headers=HEADERS).json()
    return result


def sentiment(query, model):
    """
    Sentiment analysis, 500/day
    :param query: input query
    :param model: general, auto, kitchen, food, news, weibo
    :return: positive rate, negative rate
    """
    result = nlp.sentiment(query, model=model)[0]
    return result


def tag(query):
    """
    Add tags
    :param query: input query
    :return: result list
    """
    result = nlp.tag(query)
    return result


if __name__ == '__main__':
    type = input('Please input your intent: ')
    if type == 'sentiment':
        query = input('Please input query: ')
        model = input('Please input model: ')
        result = sentiment(query, model)
        limits = check_limits()['limits']['sentiment']['count-limit-remaining']
        print('Positive probability:', result[0])
        print('Negative probability:', result[1])
        print('Sentiment limit remaining:', limits)

    elif type == 'tag':
        query = input('Please input query: ')
        result = tag(query)
        print(result)