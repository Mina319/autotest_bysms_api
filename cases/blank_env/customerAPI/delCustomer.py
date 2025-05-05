from hytest import CHECK_POINT, STEP, INFO
from lib.webapi import apimgr


class Case_0251:
    name = '删除客户-API-0251'

    def teststeps(self):
        STEP(1, '删除一个不存在ID的客户')
        r = apimgr.customer_del(1)
        addRet = r.json()
        expected = {"msg": "customer id not exist", "ret": 2}
        CHECK_POINT('返回的ret值=2', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.customer_list(10, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [],
            'total': 0
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)
