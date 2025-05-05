from hytest import CHECK_POINT, STEP, INFO
from lib.webapi import apimgr


class Case_0101:
    name = '列出客户-API-0101'

    def teststeps(self):
        STEP(1, '尝试列出客户，没有携带有效的sessionid')
        headers = {}
        headers['Cookie'] = 'sessionid='
        r = apimgr.customer_list1(10, 1, headers=headers)
        # 验证返回状态码为302
        # CHECK_POINT('返回状态码是302', r.status_code == 302)
        INFO(f'返回状态码是{r.status_code}')
        # 验证返回体
        listRet = r.json()
        INFO(f'listRet{listRet}')
        expected = {
            "ret": 302,
            "msg": "未登录",
            "redirect": "/mgr/sign.html"
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0102:
    name = '列出客户-API-0102'

    def teststeps(self):
        STEP(1, '列出客户')
        r = apimgr.customer_list(10, 1)
        CHECK_POINT('检查状态码', r.status_code == 200)
        # 验证返回体
        listRet = r.json()
        # INFO(f'listRet{listRet}')
        expected = {
                "ret": 0,
                "retlist": [],
                'total': 0
            }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0103:
    name = '列出客户-API-0103'

    def teststeps(self):
        STEP(1, '列出客户')

        r = apimgr.customer_list(10, 'hello', '')
        INFO(f'状态码:{r.status_code}')   # 400
        # CHECK_POINT('检查状态码', r.status_code == 302)
        # 验证返回体
        listRet = r.json()
        INFO(f'listRet{listRet}')  # {'msg': 'bad pagenum:hello', 'ret': 2}
        expected = {
                    "ret": 1,
                    "msg":  "请求参数错误"
                }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0104:
    name = '列出客户-API-0104'

    def teststeps(self):
        STEP(1, '列出客户')
        r = apimgr.customer_list('hello', 10,  '')
        INFO(f'状态码:{r.status_code}')   # 400
        # CHECK_POINT('检查状态码', r.status_code == 302)
        # 验证返回体
        listRet = r.json()
        INFO(f'listRet{listRet}')  # {'msg': 'bad pagesize:hello', 'ret': 2}
        expected = {
                    "ret": 1,
                    "msg":  "请求参数错误"
                }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0105:
    name = '列出客户-API-0105'

    def teststeps(self):
        STEP(1, '列出客户')
        r = apimgr.customer_list(pagesize=10)
        INFO(f'状态码:{r.status_code}')    # 200
        # 验证返回体
        listRet = r.json()
        INFO(f'listRet:{listRet}')  # {"ret":0,"retlist":[],"total":0}

        expected = {
                    "ret": 1,
                    "msg":  "请求参数错误"
                }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0106:
    name = '列出客户-API-0106'

    def teststeps(self):
        STEP(1, '列出客户')
        r = apimgr.customer_list(pagenumber=1)
        INFO(f'状态码:{r.status_code}')
        # 验证返回体
        listRet = r.json()
        INFO(f'listRet:{listRet}')  # {"ret":0,"retlist":[],"total":0}
        expected = {
                    "ret": 1,
                    "msg":  "请求参数错误"
                }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0107:
    name = '列出客户-API-0107'

    def teststeps(self):
        STEP(1, '列出客户')
        r = apimgr.customer_list(pagesize=10, pagenumber=1)
        INFO(f'状态码:{r.status_code}')    # 200
        # 验证返回体
        listRet = r.json()
        INFO(f'listRet:{listRet}')  # {"ret":0,"retlist":[],"total":0}
        expected = {
                    "ret": 1,
                    "msg":  "请求参数错误"
                }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)
