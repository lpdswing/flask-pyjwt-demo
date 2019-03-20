#-*- coding:utf-8 -*-
# datetime: 2019/3/20 10:46
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def config_extensions(app):
    db.init_app(app)