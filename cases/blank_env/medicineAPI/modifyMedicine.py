from hytest import CHECK_POINT, STEP
from lib.webapi import apimgr


class Case_0401:
    name = '修改药品-API-0401'

    def teststeps(self):
        STEP(1, '修改一个不存在ID的药品')
        name, desc, sn = "青霉素", "青霉素 国字号", "099877883837"
        r = apimgr.medicine_modify(1, name, desc, sn)
        addRet = r.json()
        expected = {"msg": "medicine id not exist", "ret": 2}
        CHECK_POINT('返回的ret值=2', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.medicine_list(10, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [],
            'total': 0
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)
