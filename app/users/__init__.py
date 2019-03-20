#-*- coding:utf-8 -*-
# datetime: 2019/3/20 9:21
from flask import Blueprint

auth = Blueprint('auth', __name__)


from . import api