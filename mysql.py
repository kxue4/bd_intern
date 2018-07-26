#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/23 14:32
# @Author  : Kaiwen Xue
# @File    : mysql.py
# @Software: PyCharm
import pymysql
import re

db = pymysql.connect(host="localhost", user="root", password="12345678", db="dump", port=3306)
cursor = db.cursor()

amz = open('/Users/Kevin/Downloads/Amazon83K_25May_2016.txt')

fl = amz.readlines()

for lines in fl:
    account = {}

    email = re.findall(r'email\|:\|(.+?)\|', lines)
    password = re.findall(r'password\|:\|(.+?)\|', lines)
    full_name = re.findall(r'full_name\|:\|(.+?)\|', lines)
    city = re.findall(r'city\|:\|(.+?)\|', lines)
    state = re.findall(r'state\|:\|(.+?)\|', lines)
    street = re.findall(r'street\|:\|(.+?)\|', lines)
    zipcode = re.findall(r'zipcode\|:\|(.+?)\|', lines)
    phone = re.findall(r'phone\|:\|(.+?)\|', lines)
    added_on = re.findall(r'added_on\|:{\|\$date\|:\|(.+?)\|', lines)
    last_attempted_at = re.findall(r'last_picked_at\|:{\|\$date\|:\|(.+?)\|', lines)
    last_good_proxy_id = re.findall(r'last_good_proxy_id\|:{\|\$date\|:\|(.+?)\|', lines)
    user_agent = re.findall(r'user_agent\|:\|(.+?)\|', lines)

    s_email = email[0]
    s_password = password[0]
    s_full_name = full_name[0]
    s_city = city[0]
    s_state = state[0]
    s_zipcode = zipcode[0]
    s_phone = phone[0]
    s_last_attempted_at = last_attempted_at[0]
    try:
        s_user_agent = user_agent[0]
    except:
        s_user_agent = '0'
    try:
        s_street = street[0]
    except IndexError:
        s_street = '0'

    try:
        s_added_on = added_on[0]
    except IndexError:
        s_added_on = '0'

    try:
        s_last_good_proxy_id = last_good_proxy_id[0]
    except IndexError:
        s_last_good_proxy_id = '0'

    sql = "insert into amazon(email, password, full_name, state, city, street, zipcode, phone, added_on, last_attempted_at, last_good_proxy_id, user_agent) values('%s','%s','%s','%s','%s','%s','%d','%s','%s','%s','%s','%s')" % (s_email, s_password, s_full_name, s_state, s_city, s_street, s_zipcode, s_phone, s_added_on, s_last_attempted_at, s_last_good_proxy_id, s_user_agent)
    cursor.execute(sql)


print('Finished!')
db.close()