# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------
# Time     : 2020/4/21 9:19
# Author   : 何喜
# Email    : hexi@wolongdata.com
# File     : api.py
# Software : PyCharm
# ---------------------------------------

from flask import Blueprint, request, jsonify, render_template

music_blueprint = Blueprint('music', __name__)

