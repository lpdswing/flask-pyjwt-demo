#-*- coding:utf-8 -*-
# datetime: 2019/3/20 9:25
import jwt, datetime, time
from flask import jsonify
from app.users.model import Users
from app.config import BaseConfig
from .. import common


class Auth():

    @staticmethod
    def encode_auth_token(user_id, login_time):
        """
        生成认证token
        exp: 过期时间
        iat: 发行时间
        :param user_id: int
        :param login_time: int(timestamp)
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0,seconds=10),
                'iat': datetime.datetime.utcnow(),
                'iss': 'ken',
                'data':{
                    'id': user_id,
                    'login_time': login_time
                }
            }
            return jwt.encode(
                payload,
                BaseConfig.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        验证token
        :param auth_token:
        :return:
        """
        try:
            payload = jwt.decode(auth_token, BaseConfig.SECRET_KEY, options={'verify_exp': False})
            if ('data' in payload and 'id' in payload['data']):
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token过期'
        except jwt.InvalidTokenError:
            return '无效Token'

    def authenticate(self, username, password):
        """
        用户登录,成功返回token,失败返回原因,把登录时间写进数据库
        :param username:
        :param password:
        :return: json
        """
        u = Users.query.filter_by(username=username).first()
        if not u:
            return jsonify(common.falseReturn('', '找不到用户'))
        else:
            if Users().check_password(u.password, password):
                login_time = int(time.time())
                u.login_time = login_time
                Users.update(u)
                token = self.encode_auth_token(u.id, login_time)
                return jsonify(common.trueReturn(token.decode(), '登录成功'))
            else:
                return jsonify(common.falseReturn('', '密码错误'))

    def identify(self, request):
        """
        用户鉴权
        :param request:
        :return: list
        """
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_tokenArr = auth_header.split(' ')
            if (not auth_tokenArr or auth_tokenArr[0] != 'JWT' or len(auth_tokenArr) != 2):
                result = common.falseReturn('', '请传递正确的验证头信息')
            else:
                auth_token = auth_tokenArr[1]
                payload = self.decode_auth_token(auth_token)
                if not isinstance(payload, str):
                    u = Users().get(payload['data']['id'])
                    if not u:
                        result = common.falseReturn('', '找不到该用户信息')
                    else:
                        if u.login_time == payload['data']['login_time']:
                            result = common.trueReturn(u.id, '请求成功')
                        else:
                            result = common.falseReturn('', 'token信息更改,请重新登录获取')
                else:
                    result = common.falseReturn('', payload)
        else:
            result = common.falseReturn('', '没有提供认证token')
        return result