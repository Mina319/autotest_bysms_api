from hytest import CHECK_POINT, STEP, INFO
from lib.webapi import apimgr


def getRetlist():
    # 获取系统中客户信息
    r = apimgr.customer_list(1, 1)
    ret = r.json()
    retlist = ret['retlist'][0]
    print('retlist:', retlist)
    # {'address': '武汉市桥西医院北路', 'id': 284, 'name': '武汉市桥西医院', 'phonenumber': '13345679934'}
    return retlist


class Case_0253:
    name = '删除客户-API-0253'

    def teststeps(self):
        STEP(1, '删除一个已绑定订单的客户')
        address, cid, name, phonenumber = getRetlist().values()
        r = apimgr.customer_del(cid=cid)
        delRet = r.json()
        print('delRet----', delRet)
        expected = {"msg": "medicine id not exist", "ret": 2}
        # CHECK_POINT('返回的ret值=2', addRet == expected)

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
