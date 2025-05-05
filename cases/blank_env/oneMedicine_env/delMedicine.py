from hytest import CHECK_POINT, STEP
from lib.webapi import apimgr


def getRetlist():
    # 获取系统中药品信息
    r = apimgr.medicine_list(1, 1)
    ret = r.json()
    retlist = ret['retlist'][0]
    print('retlist:', retlist)
    #  {'desc': '青霉素 国字号1', 'id': 103, 'name': '青霉素1', 'sn': '099877883801'}
    return retlist


class Case_0452:
    name = '删除药品-API-0452'

    def teststeps(self):
        desc, mid, name, sn = getRetlist().values()
        STEP(1, f'删除药品：id为{mid}')
        r = apimgr.medicine_del(mid=mid)
        addRet = r.json()
        expected = {"ret": 0}
        # print('expected-----', addRet)
        CHECK_POINT('返回的ret值=0', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.medicine_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [],
            'total': 0
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)

