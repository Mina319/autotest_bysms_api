import json
from hytest import CHECK_POINT, STEP
from lib.webapi import apimgr


def suite_teardown():
    # 删除所有客户
    apimgr.customer_del_all()


class Case_0151:
    name = '添加客户-API-0151'

    def teststeps(self):
        STEP(1, '添加一个客户')
        r = apimgr.customer_add('武汉市桥西医院',
                                '13345679934',
                                '武汉市桥西医院北路')
        addRet = r.json()
        self.addedCustomerId = addRet['id']
        CHECK_POINT('返回的ret值=0', addRet['ret'] == 0)

        STEP(2, '检查系统数据')
        r = apimgr.customer_list(10, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [
                {
                    "address": "武汉市桥西医院北路",
                    "id": addRet['id'],
                    "name": "武汉市桥西医院",
                    "phonenumber": "13345679934"
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0153:
    name = '添加客户-API-0153'

    def teststeps(self):
        STEP(1, '添加一个客户')
        r = apimgr.customer_add2({"phonenumber": "13345679934",
                                  "address": "南京市鼓楼北路",
                                  })
        addRet = r.json()
        expected = {
            "msg": "req body format error\nKey: 'Body.Data.Name' Error:Field validation for 'Name' failed on the "
                   "'required' tag",
            "ret": 2}
        CHECK_POINT('返回的ret值', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.customer_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [],
            'total': 0
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0154:
    name = '添加客户-API-0154'

    def teststeps(self):
        STEP(1, '添加一个客户')
        bodyStr = '''{
            "action":"add_customer",
            "data":{
                "name":"武汉市桥西医院",
                "name":"武汉市桥西医院",
                "phonenumber":"13345679934",
                "address":"武汉市桥西医院北路"
            }
        }'''
        r = apimgr.customer_add_json(data=bodyStr)
        addRet = r.json()
        expected = {
            "ret": 1,
            "msg": "请求消息参数错误"
        }
        CHECK_POINT('返回的ret值', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.customer_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [],
            'total': 0
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0155:
    name = '添加客户-API-0155'

    def teststeps(self):
        STEP(1, '添加一个客户')
        raw_body = '''
               {
                   "name": "武汉市桥西医院",
                   "address": "南京市鼓楼北路"
               }
               '''
        r = apimgr.customer_add2(data=json.loads(raw_body))
        addRet = r.json()
        expected = {"msg": "req body format error\nKey: 'Body.Data.Phonenumber' Error:Field validation for "
                           "'Phonenumber' failed on the 'required' tag", "ret": 2}

        # expected = {
        #     "ret": 1,
        #     "msg": "请求消息参数错误"
        # }
        CHECK_POINT('返回的ret值', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.customer_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [],
            'total': 0
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0156:
    name = '添加客户-API-0156'

    def teststeps(self):
        STEP(1, '添加一个客户')
        bodyStr = '''{
                    "action":"add_customer",
                    "data":{
                        "name":"武汉市桥西医院",
                        "phonenumber":"13345679934",
                        "phonenumber":"13345679934",
                        "address":"武汉市桥西医院北路"
                    }
                }'''
        r = apimgr.customer_add_json(data=bodyStr)
        addRet = r.json()
        expected = {
            "ret": 1,
            "msg": "请求消息参数错误"
        }
        CHECK_POINT('返回的ret值', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.customer_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [],
            'total': 0
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)

