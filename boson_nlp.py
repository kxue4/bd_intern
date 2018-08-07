#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/6 17:13
# @Author  : Kaiwen Xue
# @File    : boson_nlp.py
# @Software: PyCharm
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
from prettytable import PrettyTable
import requests


token = '8vE1y5w3.26891.HXpAR_Iogezg'  # 个人API
nlp = BosonNLP(token)

en2cn = {'n': '名词', 'nr': '人名', 'nr1': '中文姓氏', 'nrf': '音译人名', 'ns': '地名', 'nt': '组织机构名',
         'nz': '其他专有名词', 'nl': '名词性惯用语', 't': '时间词', 's': '处所词', 'f': '方位词', 'v': '动词',
         'vd': '副动词', 'vshi': '动词"是"', 'vyou': '动词"有"', 'vi': '不及物动词', 'vl': '动词性惯用语',
         'a': '形容词', 'ad': '副形词', 'an': '名形词', 'al': '形容词性惯用语', 'b': '区别词', 'bl': '区别词性惯用语',
         'z': '状态词', 'r': '代词', 'm': '数词', 'q': '量词', 'd': '副词', 'dl': '副词性惯用语', 'p': '介词',
         'pba': '介词"把"', 'pbei': '介词"被"', 'c': '连词', 'u': '助词', 'uzhe': '助词"着"', 'ule': '助词"了"',
         'uguo': '助词"过"', 'ude': '助词"的"、"地"、"得"', 'usuo': '助词"所"', 'udeng': '助词"等"、"等等"',
         'uyy': '助词"一样"、"似的"', 'udh': '助词"的话"', 'uzhi': '助词"之"', 'ulian': '助词"连"', 'y': '语气词',
         'o': '拟声词', 'h': '前缀', 'k': '后缀', 'nx': '字符串', 'w': '标点符号', 'wkz': '左括号', 'wky': '右括号',
         'wyz': '左引号', 'wyy': '右引号', 'wj': '句号', 'ww': '问号', 'wt': '叹号', 'wd': '逗号', 'wf': '分号',
         'wn': '顿号', 'wm': '冒号', 'ws': '省略号', 'wp': '破折号', 'wb': '百分号千分号', 'wh': '单位符号',
         'email': '电子邮件地址', 'tel': '电话号码', 'id': '身份证号', 'ip': 'ip地址', 'url': '网页链接'}

num2cn = {0: '体育', 1: '教育', 2: '财经', 3: '社会', 4: '娱乐', 5: '军事', 6: '国内', 7: '科技', 8: '互联网', 9: '房产',
          10: '国际', 11: '女人', 12: '汽车', 13: '游戏'}

def check_limits():
    """
    Check limits remaining.
    :return: result dict
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
    :return: [positive rate, negative rate]
    """
    result = nlp.sentiment(query, model=model)[0]
    return result


def tag(query):
    """
    Add tags.
    :param query: input query
    :return: {'word': 'tag', ...}
    """
    result = nlp.tag(query)
    rst = result[0]
    cn_values = []

    for tags in rst['tag']:

        if tags in en2cn:
            cn_values.append(en2cn[tags])

    rst['cn_tag'] = cn_values
    cn_result = dict()

    for x, y in zip(rst['word'], rst['cn_tag']):
        cn_result[x] = y

    return cn_result


def keywords(query, number):
    """
    Find the keywords and the weight of them, the sum of total square of weights is 1.
    :param query: input query
    :return:
    """
    if number == '':
        number = 100

    result = nlp.extract_keywords(query, top_k=number)
    return result


def suggest(word, number):
    """
    Give the similar words of original word
    :param query: input word
    :return: {'scroe': 'word', ...}
    """
    if number == '':
        number = 10

    result = nlp.suggest(word, top_k=number)
    return result


def classify(news):
    """
    Classify news
    :param news: input news title
    :return:
    """
    result = nlp.classify(news)[0]
    return num2cn[result]


if __name__ == '__main__':
    intent = input('Please input your intent: ')

    if intent == 'sentiment':
        query = input('Please input query: ')
        print('There are 6 types of model: general, auto, kitchen, food, news and weibo')
        model = input('Please input model: ')
        result = sentiment(query, model)
        limits = check_limits()['limits']['sentiment']['count-limit-remaining']
        print('\nPositive probability:', result[0])
        print('Negative probability:', result[1])
        print('\nSentiment limit remaining:', limits)

    elif intent == 'tag':
        query = input('Please input query: ')
        result = tag(query)
        limits = check_limits()['limits']['tag']['count-limit-remaining']
        print('')
        print(result)
        print('\nTag limit remaining:', limits)

    elif intent == 'keyword':
        query = input('Please input query: ')
        number = input('Please input the number of keywords(blank=100): ')
        result = keywords(query, number)
        limits = check_limits()['limits']['keywords']['count-limit-remaining']
        print('')

        for i in result:
            print(i[0], i[1])

        print('\nKeywords limit remaining', limits)

    elif intent == 'suggest':
        word = input('Please input a word: ')
        number = input('Please input the number of suggestions(blank=10): ')
        result = suggest(word, number)
        limits = check_limits()['limits']['suggest']['count-limit-remaining']
        print('')

        for score, words in result:
            sug = words.split('/')[0]
            tag = words.split('/')[1]
            if tag in en2cn:
                tag = en2cn[tag]
            print(score, sug, tag)

        print('\nSuggest limit remaining', limits)

    elif intent == 'classify':
        news = input('Please input new title: ')
        result = classify(news)
        limits = check_limits()['limits']['classify']['count-limit-remaining']
        print('')
        print(result)
        print('\nClassify limit remaining', limits)