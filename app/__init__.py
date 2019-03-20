#-*- coding:utf-8 -*-
# datetime: 2019/3/20 9:21
import os
from flask import Flask, request
from .config import config
from .extensions import config_extensions, db
from .commands import *





def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('app')
    app.config.from_object(config[config_name])
    config_extensions(app)

    # 处理全局Http请求头,允许跨域
    # 这里使用Cors插件更方便
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        if request.method == 'OPTIONS':
            response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
            headers = request.headers.get('Access-Control-Request-Headers')
            if headers:
                response.headers['Access-Control-Allow-Headers'] = headers
        return response

    app.cli.command()(initdb) #注册初始化db命令 使用flask initdb


    return app

from app import common
