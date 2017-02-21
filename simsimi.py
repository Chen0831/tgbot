#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

uuid = 'wPaQgPrwjSCGJ9N55mtC51tYJJKUiPTrwfp8cvYo2ce'

url = 'http://www.simsimi.com/getRealtimeReq'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22'}

def default():
    text = input('请输入内容:')
    print(simsimi(text))

def simsimi(text):
    params={
    'uuid':uuid,
    'lc':'zh',
    'ft':1,
    'reqText':text
    }

    r_01 = requests.get(url, params=params, headers=headers)

    data = json.loads(r_01.text)

    if r_01.status_code == 200:
        simsimi = data['respSentence']
        return simsimi
    else:
        return '劳资不知道说什么啦！'

if __name__ == '__main__':
    default()
