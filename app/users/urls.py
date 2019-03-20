#-*- coding:utf-8 -*-
# datetime: 2019/3/20 15:14
from . import auth
from .api import User
from flask import jsonify


@auth.route('/register', methods=['POST'])
def register():
    return jsonify(User().register())


@auth.route('/login', methods=['POST'])
def login():
    return jsonify(User().login())


@auth.route('/user', methods=['GET'])
def get():
    return jsonify(User().get())