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


class Case_0402:
    name = '修改药品-API-0402'

    def teststeps(self):
        STEP(1, '修改药品')
        desc, mid, name, sn = getRetlist().values()
        newName = '叶黄素'
        r = apimgr.medicine_modify(mid=mid, name=newName)
        addRet = r.json()
        expected = {"ret": 0}
        # print('expected-----', addRet)
        CHECK_POINT('返回的ret值=0', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.medicine_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [
                {
                    "desc": desc,
                    "id": mid,
                    "name": newName,
                    "sn": sn
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0403:
    name = '修改药品-API-0403'

    def teststeps(self):
        STEP(1, '修改药品')
        desc, mid, name, sn = getRetlist().values()
        newSn = '091234883801'
        r = apimgr.medicine_modify(mid=mid, sn=newSn)
        addRet = r.json()
        expected = {"ret": 0}
        # print('expected-----', addRet)
        CHECK_POINT('返回的ret值=0', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.medicine_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [
                {
                    "desc": desc,
                    "id": mid,
                    "name": name,
                    "sn": newSn
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0404:
    name = '修改药品-API-0404'

    def teststeps(self):
        STEP(1, '修改药品')
        desc, mid, name, sn = getRetlist().values()
        newDesc = '青霉素 江苏字号1'
        r = apimgr.medicine_modify(mid=mid, desc=newDesc)
        addRet = r.json()
        expected = {"ret": 0}
        # print('expected-----', addRet)
        CHECK_POINT('返回的ret值=0', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.medicine_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [
                {
                    "desc": newDesc,
                    "id": mid,
                    "name": name,
                    "sn": sn
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0405:
    name = '修改药品-API-0405'

    def teststeps(self):
        STEP(1, '修改药品')
        desc, mid, name, sn = getRetlist().values()
        newName, newSn = '叶黄素', '091234883801'
        r = apimgr.medicine_modify(mid=mid, name=newName, sn=newSn)
        addRet = r.json()
        expected = {"ret": 0}
        # print('expected-----', addRet)
        CHECK_POINT('返回的ret值=0', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.medicine_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [
                {
                    "desc": desc,
                    "id": mid,
                    "name": newName,
                    "sn": newSn
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0406:
    name = '修改药品-API-0406'

    def teststeps(self):
        STEP(1, '修改药品')
        desc, mid, name, sn = getRetlist().values()
        newName, newDesc = '叶黄素', '叶黄素 国字号1'
        r = apimgr.medicine_modify(mid=mid, name=newName, desc=newDesc)
        addRet = r.json()
        expected = {"ret": 0}
        # print('expected-----', addRet)
        CHECK_POINT('返回的ret值=0', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.medicine_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [
                {
                    "desc": newDesc,
                    "id": mid,
                    "name": newName,
                    "sn": sn
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0407:
    name = '修改药品-API-0407'

    def teststeps(self):
        STEP(1, '修改药品')
        desc, mid, name, sn = getRetlist().values()
        newSn, newDesc = '091234883801', '叶黄素 国字号1'
        r = apimgr.medicine_modify(mid=mid, sn=newSn, desc=newDesc)
        addRet = r.json()
        expected = {"ret": 0}
        # print('expected-----', addRet)
        CHECK_POINT('返回的ret值=0', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.medicine_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [
                {
                    "desc": newDesc,
                    "id": mid,
                    "name": name,
                    "sn": newSn
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0408:
    name = '修改药品-API-0408'

    def teststeps(self):
        STEP(1, '修改药品')
        desc, mid, name, sn = getRetlist().values()
        newName, newSn, newDesc = '叶黄素', '091234883801', '叶黄素 国字号1'
        r = apimgr.medicine_modify(mid=mid, name=newName, sn=newSn, desc=newDesc)
        addRet = r.json()
        expected = {"ret": 0}
        # print('expected-----', addRet)
        CHECK_POINT('返回的ret值=0', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.medicine_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [
                {
                    "desc": newDesc,
                    "id": mid,
                    "name": newName,
                    "sn": newSn
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)
