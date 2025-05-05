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


class Case_0409:
    name = '修改药品-API-0409'

    def teststeps(self):
        STEP(1, '获取修改药品的ID')
        mid = getRetlist()["id"]
        STEP(2, '修改药品:修改药品与已经存在的一样')
        r = apimgr.customer_modify(mid, name='青霉素1')
        addRet = r.json()
        print('addRet----', addRet)
        expected = {'msg': 'customer id not exist', 'ret': 2}
        CHECK_POINT('返回的ret值=2', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.medicine_list(2, 1)
        listRet = r.json()
        retlist = []
        for i in range(2, 0, -1):
            ele = {}
            ele['name'] = f'青霉素{i}'
            ele['id'] = mid
            ele['desc'] = f'青霉素 国字号{i}'
            ele['sn'] = f'0998778838{i:02d}'
            mid -= 1
            retlist.append(ele)

        expected = {
            "ret": 0,
            "retlist": retlist,
            'total': 2
        }
        print('expected----', expected)
        print('listRet----', listRet)
        CHECK_POINT('返回的消息体数据正确，未成功修改', listRet == expected)
