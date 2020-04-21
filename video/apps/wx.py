# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------
# Time     : 2020/4/21 9:13
# Author   : 何喜
# Email    : hexi@wolongdata.com
# File     : wx.py
# Software : PyCharm
# ---------------------------------------
import re
import requests

headers = {
    'Host': 'mp.weixin.qq.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/80.0.3987.163 Safari/537.36'
}


def get_video_id(url=None):
    r = requests.get(url, headers=headers)
    vid_list = re.findall("window.cgiData.vid = '(.*?)';", r.text, re.S)
    if vid_list:
        return vid_list[0]
    else:
        return


def get_video_url(vid=None):
    if not vid:
        return
    url = f'https://mp.weixin.qq.com/mp/videoplayer?action=get_mp_video_play_url&vid={vid}'
    r = requests.get(url, headers=headers)
    try:
        result = r.json()
        item = {
            'title': result['title'],
            'url': result['url_info'][0]['url']
        }
    except Exception as e:
        print(e)
        print(r.text)
        item = {'url': '', 'title': ''}
    return item


if __name__ == '__main__':
    video_id = get_video_id()
    get_video_url(video_id)
