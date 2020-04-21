# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------
# Time     : 2020/4/21 10:13
# Author   : 何喜
# Email    : hexi@wolongdata.com
# File     : music163.py
# Software : PyCharm
# ---------------------------------------
import re
import requests
import execjs
import jpype
import os
from jpype import *

headers = {
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/80.0.3987.163 Safari/537.36'
}


def get_params():
    # javascript
    # text_js = open('music163.js', 'r', encoding='utf-8').read()
    # print(text_js)
    # ctx = execjs.compile(text_js.replace('\ufffd',''), cwd=r'C:\Users\thoft\AppData\Roaming\npm\node_modules')
    # z = ctx.call('get_params')
    # print(z)
    # java
    jvm_path = get_default_jvm_path()
    print(jvm_path)
    # jvm_path = r'C:\Java\jdk1.8.0_241\jre\bin\server\jvm.dll'
    class_path = 'com/encrypt_utils.java'
    startJVM(jvm_path, '-ea', f'-Djava.class.path{class_path}')
    encrypt_utils_class = jpype.JClass('EncryptUtils')
    utils = encrypt_utils_class()
    c = utils.encrypt({'data': 'df'})
    print(c)
    jpype.shutdownJVM()


def get_music_url(url):
    data = {
        'params': '',
        'encSecKey': ''
    }


if __name__ == '__main__':
    url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
    # get_music_url(url)
    get_params()
