# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------
# Time     : 2020/4/21 9:13
# Author   : 何喜
# Email    : hexi@wolongdata.com
# File     : quanmin.py
# Software : PyCharm
# ---------------------------------------
import re
import requests

headers = {
    'Host': 'quanmin.hao222.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/80.0.3987.163 Safari/537.36'
}


def get_video_url(url):
    r = requests.get(url, headers=headers)
    if not r:
        return
    url_list = re.findall('<meta property="og:videosrc" content="(.*?)">', r.text, re.S)
    if url_list:
        return url_list[0]
    else:
        return


if __name__ == '__main__':
    url = 'https://quanmin.hao222.com/sv2?source=share-h5&pd=feed&vid=5608530950810114910&shared_cuid=_P2kagus2u_cPvtWgOvl8j8ova_Ya-8Rlu2Jig8xH8KoLqqqB&shared_uid=_avTiYugvfGqQqqqB&nid=sv_5608530950810114910&uk=SvMvJVv5xts606R3L3wgvA'
    get_video_url(url)
