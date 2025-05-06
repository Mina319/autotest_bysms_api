from hytest import CHECK_POINT, STEP, INFO
from lib.webapi import apimgr, getRetlist


class Case_0253:
    name = '删除客户-API-0253'

    def teststeps(self):
        STEP(1, '删除一个已绑定订单的客户')
        address, cid, name, phonenumber = getRetlist().values()
        r = apimgr.customer_del(cid=cid)
        delRet = r.json()
        print('delRet----', delRet)
        expected = {"msg": "删除记录失败，或许需要先删除相关订单", "ret": 2}
        CHECK_POINT('返回的ret值=2', delRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.customer_list(10, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [{
                'address': address,
                'id': cid,
                'name': name,
                'phonenumber': phonenumber
            }],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)

