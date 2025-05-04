from hytest import CHECK_POINT, STEP
from lib.webapi import apimgr


class Case_000x:

    ddt_cases = [
        {
            'name': '登录-0001',
            'para': [{'username': 'byhy', 'password': '88888888'}, {"ret": 0}, False]
        },
        {
            'name': '登录-0002',
            'para': [{'username': 'byhy', 'password': '8888888'}, {"ret": 1, "msg": "用户名或者密码错误"}, False]
        },
        {
            'name': '登录-0003',
            'para': [{'username': 'byhy', 'password': '88888888888888888888'}, {"ret": 1, "msg": "用户名或者密码错误"}, False]
        },
        {
            'name': '登录-0004',
            'para': [{'username': 'b', 'password': '88888888'}, {"ret": 1, "msg": "用户名或者密码错误"}, False]
        },
        {
            'name': '登录-0005',
            'para': [{'username': 'bbbbbbbbbb', 'password': '88888888'}, {"ret": 1, "msg": "用户名或者密码错误"}, False]
        },
        {
            'name': '登录-0006',
            'para': [{'username': None, 'password': '88888888'}, {"ret": 1, "msg": "用户名或者密码错误"}, False]
        },
        {
            'name': '登录-0007',
            'para': [{'username': 'byhy', 'password': None}, {"ret": 1, "msg": "用户名或者密码错误"}, False]
        },
        {
            'name': '登录-0008',
            'para': [
                '''{
                    "username": "byhy",
                    "password": "88888888",
                    "password": "88888888"
                }''',
                {"ret": 1, "msg": "参数格式错误"},
                True
            ]
        }
        ,
        {
            'name': '登录-0009',
            'para': [
                '''{
                    "username": "byhy",
                    "username": "byhy",
                    "password": "88888888"
                }''',
                {"ret": 1, "msg": "参数格式错误"},
                True
            ]
        }
    ]

    def teststeps(self):
        STEP(1, '登录系统')
        # 取出参数
        data, res, raw = self.para
        ret = apimgr.mgr_login1(data, raw=raw)
        CHECK_POINT('检查返回值', res == ret.json())

