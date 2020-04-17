# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------
# Time     : 2020/4/14 14:31
# Author   : 何喜
# Email    : hexi@wolongdata.com
# File     : api.py
# Software : PyCharm
# ---------------------------------------
from flask import Flask, request, jsonify, render_template
from apps.wx import crawler as wx_crawler
from apps.quanmin import crawler as qm_crawler

app = Flask(__name__)


@app.route('/apps/video', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        app_name = request.values.get('apps')
        share_url = request.values.get('url')
        if app_name == 'wx':
            vid = wx_crawler.get_video_id(share_url)
            url = wx_crawler.get_video_url(vid)
        elif app_name == 'quanmin':
            url = qm_crawler.get_video_url(share_url)
        else:
            url = '未获取到视频地址，请查看应用和视频分享地址是否对应!'
        if not url:
            url = '未获取到视频地址，请查看应用和视频分享地址是否对应!'
        result = {'url': url, 'status': 0}
        return jsonify(result)
    else:
        return render_template('wx.html')


# if __name__ == '__main__':
#     apps.run(debug=True,host='0.0.0.0')
