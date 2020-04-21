# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------
# Time     : 2020/4/21 9:11
# Author   : 何喜
# Email    : hexi@wolongdata.com
# File     : api.py
# Software : PyCharm
# ---------------------------------------
from flask import Blueprint, request, jsonify, render_template
import video.apps.wx as wx_crawler
import video.apps.quanmin as qm_crawler

video_blueprint = Blueprint('video', __name__)


@video_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template('video.html')


@video_blueprint.route('/submit', methods=['POST'])
def submit():
    app_name = request.values.get('app')
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
