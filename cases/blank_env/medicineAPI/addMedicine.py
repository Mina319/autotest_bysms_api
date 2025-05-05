from hytest import CHECK_POINT, STEP, INFO
from lib.webapi import apimgr


class Case_0351:
    name = '添加药品-API-0351'

    def teststeps(self):
        STEP(1, '添加一个药品')

        name, desc, sn = "青霉素", "青霉素 国字号", "099877883837"
        r = apimgr.medicine_add(name, desc, sn)
        addRet = r.json()
        print('addRet-----', addRet)
        CHECK_POINT('返回的ret值=0', addRet['ret'] == 0)

        STEP(2, '检查系统数据')
        r = apimgr.medicine_list(1, 1)
        listRet = r.json()
        print('listRet-----', listRet)
        expected = {
            "ret": 0,
            "retlist": [{
                    "name": name,
                    "desc": desc,
                    "sn": sn,
                    "id": addRet["id"]
                }],
            "total": 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0353:
    name = '添加药品-API-0353'

    def teststeps(self):
        STEP(1, '添加一个药品')

        name, desc, sn = "青霉素", "青霉素 国字号", "099877883837"
        r = apimgr.medicine_add(desc=desc, sn=sn)
        addRet = r.json()
        print('addRet-----', addRet)
        #  {'msg': "req body format error\nKey: 'Body.Data.Name' Error:Field validation for 'Name' failed on the 'required' tag", 'ret': 2}
        CHECK_POINT('返回的ret值=2', addRet['ret'] == 2)

        STEP(2, '检查系统数据')
        r = apimgr.medicine_list(1, 1)
        listRet = r.json()
        print('listRet-----', listRet)
        expected = {
            "ret": 0,
            "retlist": [],
            "total": 0
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0354:
    name = '添加药品-API-0354'

    def teststeps(self):
        STEP(1, '添加一个药品')
        raw_body = '''
                       {
                           "name": "青霉素",
                           "name": "青霉素",
                           "desc": "青霉素 国字号",
                           "sn": "099877883837"
                       }
                       '''
        r = apimgr.medicine_add2(data=raw_body)
        addRet = r.json()
        print('addRet-----', addRet)
        #  {'msg': "req body format error\nKey: 'Body.Data.Name' Error:Field validation for 'Name' failed on the 'required' tag", 'ret': 2}
        CHECK_POINT('返回的ret值=2', addRet['ret'] == 2)

        STEP(2, '检查系统数据')
        r = apimgr.medicine_list(1, 1)
        listRet = r.json()
        print('listRet-----', listRet)
        expected = {
            "ret": 0,
            "retlist": [],
            "total": 0
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0355:
    name = '添加药品-API-0355'

    def teststeps(self):
        STEP(1, '添加一个药品')

        name, desc, sn = "青霉素", "青霉素 国字号", "099877883837"
        r = apimgr.medicine_add(name=name, desc=desc)
        addRet = r.json()
        print('addRet-----', addRet)
        #  {'msg': "req body format error\nKey: 'Body.Data.Name' Error:Field validation for 'Name' failed on the 'required' tag", 'ret': 2}
        CHECK_POINT('返回的ret值=2', addRet['ret'] == 2)

        STEP(2, '检查系统数据')
        r = apimgr.medicine_list(1, 1)
        listRet = r.json()
        print('listRet-----', listRet)
        expected = {
            "ret": 0,
            "retlist": [],
            "total": 0
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0356:
    name = '添加药品-API-0356'

    def teststeps(self):
        STEP(1, '添加一个药品')
        raw_body = '''
                       {
                           "name": "青霉素",
                           "desc": "青霉素 国字号",
                           "sn": "099877883837"
                           "sn": "099877883837"
                       }
                       '''
        r = apimgr.medicine_add2(data=raw_body)
        addRet = r.json()
        print('addRet-----', addRet)
        #  {'msg': "req body format error\nKey: 'Body.Data.Name' Error:Field validation for 'Name' failed on the 'required' tag", 'ret': 2}
        CHECK_POINT('返回的ret值=2', addRet['ret'] == 2)

        STEP(2, '检查系统数据')
        r = apimgr.medicine_list(1, 1)
        listRet = r.json()
        print('listRet-----', listRet)
        expected = {
            "ret": 0,
            "retlist": [],
            "total": 0
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)
