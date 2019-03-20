#-*- coding:utf-8 -*-
# datetime: 2019/3/20 13:35
import click
from .extensions import db
from .users.model import Users


@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """初始化数据库"""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')