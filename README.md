![](https://img.shields.io/badge/poweredby-lpdswing-green.svg)

# Flask + PyJwt 实现基于Json Web Token的用户认证授权

PyJWT是一个用来编码和解码JWT（JSON Web Tokens）的Python库，也可以用在Flask上。本Flask项目整合PyJWT来实现基于Token的用户认证授权。

- requirments:

```python
pyjwt : pip install pyjwt
flask : pip install flask
```

程序启动:

```json
flask run
```

初始化数据库:

```json
flask initdb
```

关于跨域的问题可以使用flask-cors

说明: 程序可能有未知bug,仅供参考.在参考文章的基础上, 采用Flask 1.0.2推荐的方式重新编写demo,增加蓝本使用和CLI的使用.

参考文章: https://www.thatyou.cn/flask-pyjwt-%E5%AE%9E%E7%8E%B0%E5%9F%BA%E4%BA%8Ejson-web-token%E7%9A%84%E7%94%A8%E6%88%B7%E8%AE%A4%E8%AF%81%E6%8E%88%E6%9D%83/
