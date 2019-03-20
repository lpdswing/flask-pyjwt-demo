#-*- coding:utf-8 -*-
# datetime: 2019/3/20 9:22
import click
from app import create_app
from app.extensions import db


app = create_app()


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """初始化数据库"""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')
