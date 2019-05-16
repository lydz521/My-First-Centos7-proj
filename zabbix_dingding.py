#!/usr/bin/python2.7
# -*-coding:utf-8 -*-
# Author: xiaojie


import requests
import json
import sys
import datetime
import os

headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "https://oapi.dingtalk.com/robot/send?access_token=d542b346842a1dd090dbd5888c8a34d4db205d1167de41391073b91df4b91599"


def msg(text):
    json_text= {
    "msgtype": "text",
    "at":{
        "atMobiles":
            #添加多个群艾特的人 写到下面的列表中
                ["17717765166"],
                #艾特全体 False改成True
        "isAtAll":True
            },
        "text": {
            "content": text
        }
    }
    requests.post(api_url,json.dumps(json_text),headers=headers).content


if __name__ == '__main__':
    text = sys.argv[1]
    msg(text)

