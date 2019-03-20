#-*- coding:utf-8 -*-
# datetime: 2019/3/20 9:22
def trueReturn(data, msg):
    return {
        'status': 'success',
        'data': data,
        'msg': msg
    }


def falseReturn(data, msg):
    return {
        'status': 'error',
        'data': data,
        'msg': msg
    }