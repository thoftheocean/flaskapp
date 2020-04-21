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
from video.api import video_blueprint
from music.api import music_blueprint

app = Flask(__name__)
app.register_blueprint(video_blueprint, url_prefix='/video')
app.register_blueprint(music_blueprint, url_prefix='/music')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
