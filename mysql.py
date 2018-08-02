#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/23 14:32
# @Author  : Kaiwen Xue
# @File    : mysql.py
# @Software: PyCharm
import pymysql
import re

# db = pymysql.connect(host="localhost", user="root", password="12345678", db="dump", port=3306)
# cursor = db.cursor()

amz = open('/Users/Kevin/Downloads/Amazon83K_25May_2016.txt')
amazon = open('/Users/Kevin/Downloads/Amazon.txt', 'w')

fl = amz.readlines()

mx = 0
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
    last_good_proxy_id = re.findall(r'last_good_proxy_id\|:\|(.+?)\|', lines)
    user_agent = re.findall(r'user_agent\|:\|(.+?)\|', lines)

    s_email = email[0]
    s_password = password[0]
    s_full_name = full_name[0]
    s_city = city[0]
    s_state = state[0]
    s_zipcode = int(zipcode[0])
    s_phone = phone[0]
    s_last_attempted_at = last_attempted_at[0]

    try:
        s_user_agent = user_agent[0]
    except:
        s_user_agent = 'NULL'

    try:
        s_street = street[0]
    except IndexError:
        s_street = 'NULL'

    try:
        s_added_on = added_on[0]
    except IndexError:
        s_added_on = 'NULL'

    try:
        s_last_good_proxy_id = last_good_proxy_id[0]
    except IndexError:
        s_last_good_proxy_id = 'NULL'

    # sql = """insert into amazon values('%s','%s','%s','%s','%s','%s','%d','%s','%s','%s','%s','%s');""" % (s_email, s_password, s_full_name, s_state, s_city, s_street, s_zipcode, s_phone, s_added_on, s_last_attempted_at, s_last_good_proxy_id, s_user_agent)
    # cursor.execute(sql)
    amazon.writelines(s_email + '\t' + s_password + '\t' + s_full_name + '\t' + s_state + '\t' + s_city + '\t' + s_street + '\t' + str(s_zipcode) + '\t' + s_phone + '\t' + s_added_on + '\t' + s_last_attempted_at + '\t' + s_last_good_proxy_id + '\t' + s_user_agent + '\n')


print('Finished!')
# db.close()
