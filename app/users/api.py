#-*- coding:utf-8 -*-
# datetime: 2019/3/20 9:25
from flask import jsonify, request
from ..users.model import Users
from ..auth.auths import Auth
from .. import common

class User():

    def register(self):
        """
        用户注册
        :return: json
        """
        dic = request.get_json()
        user = Users(username=dic['username'],password=Users().set_password(dic['password']),email=dic['email'])
        result = Users().add(user)
        if user.id:
            returnUser = dict(user)
            returnUser.pop('password')
            return common.trueReturn(returnUser, '用户注册成功')
        else:
            return common.falseReturn('', '用户注册失败')

    def login(self):
        """
        用户登录
        :return: json
        """
        dic = request.get_json()
        if not dic['username'] or not dic['password']:
            return common.falseReturn('', '用户名和密码不能为空')
        else:
            return Auth().authenticate(dic['username'], dic['password'])

    def get(self):
        """
        获取用户信息
        :return: json
        """
        result = Auth().identify(request)
        if result['status'] and result['data']:
            user = Users().get(result['data'])
            returnUser = dict(user).pop('password')
            res = common.trueReturn(returnUser, '请求成功')
            return res

