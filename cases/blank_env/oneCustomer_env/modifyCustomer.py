from hytest import CHECK_POINT, STEP
from lib.webapi import apimgr


def getRetlist():
    # 获取系统中客户信息
    r = apimgr.customer_list(1, 1)
    ret = r.json()
    retlist = ret['retlist'][0]
    print('retlist:', retlist)
    # {'address': '武汉市桥西医院北路', 'id': 284, 'name': '武汉市桥西医院', 'phonenumber': '13345679934'}
    return retlist


class Case_0202:
    name = '修改客户-API-0202'

    def teststeps(self):
        STEP(1, '修改客户')
        address, customerId, name, phonenumber = getRetlist().values()
        newName = '南京市桥西医院'
        r = apimgr.customer_modify(id=customerId, name=newName)
        addRet = r.json()
        expected = {"ret": 0}
        # print('expected-----', addRet)
        CHECK_POINT('返回的ret值=0', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.customer_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [
                {
                    "address": address,
                    "id": customerId,
                    "name": newName,
                    "phonenumber": phonenumber
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0203:
    name = '修改客户-API-0203'

    def teststeps(self):
        STEP(1, '修改客户')
        address, customerId, name, phonenumber = getRetlist().values()
        newphonenumber = '13923567443'
        r = apimgr.customer_modify(id=customerId, phonenumber=newphonenumber)
        addRet = r.json()
        expected = {"ret": 0}
        # print('expected-----', addRet)
        CHECK_POINT('返回的ret值=0', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.customer_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [
                {
                    "address": address,
                    "id": customerId,
                    "name": name,
                    "phonenumber": newphonenumber
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0204:
    name = '修改客户-API-0204'

    def teststeps(self):
        STEP(1, '修改客户')
        _, customerId, name, phonenumber = getRetlist().values()
        newAddress = '镇江市桃花坞123号'
        r = apimgr.customer_modify(id=customerId, address=newAddress)
        addRet = r.json()
        expected = {"ret": 0}
        # print('expected-----', addRet)
        CHECK_POINT('返回的ret值=0', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.customer_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [
                {
                    "address": newAddress,
                    "id": customerId,
                    "name": name,
                    "phonenumber": phonenumber
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0205:
    name = '修改客户-API-0205'

    def teststeps(self):
        STEP(1, '修改客户')
        address, customerId, _, _ = getRetlist().values()
        newName, newPhonenumber = '镇江市中医院', '1362345887'
        r = apimgr.customer_modify(id=customerId, name=newName, phonenumber=newPhonenumber)
        addRet = r.json()
        expected = {"ret": 0}
        # print('expected-----', addRet)
        CHECK_POINT('返回的ret值=0', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.customer_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [
                {
                    "address": address,
                    "id": customerId,
                    "name": newName,
                    "phonenumber": newPhonenumber
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0206:
    name = '修改客户-API-0206'

    def teststeps(self):
        STEP(1, '修改客户')
        address, customerId, name, phonenumber = getRetlist().values()
        newName, newAddress = '镇江市中医院', '镇江市桃花坞666号'
        r = apimgr.customer_modify(id=customerId, name=newName, address=newAddress)
        addRet = r.json()
        expected = {"ret": 0}
        # print('expected-----', addRet)
        CHECK_POINT('返回的ret值=0', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.customer_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [
                {
                    "address": newAddress,
                    "id": customerId,
                    "name": newName,
                    "phonenumber": phonenumber
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0207:
    name = '修改客户-API-0207'

    def teststeps(self):
        STEP(1, '修改客户')
        address, customerId, name, phonenumber = getRetlist().values()
        newPhonenumber, newAddress = '1275678433', '镇江市桃花坞666号'
        r = apimgr.customer_modify(id=customerId, phonenumber=newPhonenumber, address=newAddress)
        addRet = r.json()
        expected = {"ret": 0}
        # print('expected-----', addRet)
        CHECK_POINT('返回的ret值=0', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.customer_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [
                {
                    "address": newAddress,
                    "id": customerId,
                    "name": name,
                    "phonenumber": newPhonenumber
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0208:
    name = '修改客户-API-0208'

    def teststeps(self):
        STEP(1, '修改客户')
        address, customerId, name, phonenumber = getRetlist().values()
        newName, newPhonenumber, newAddress = '镇江市中医院', '1275678433', '镇江市桃花坞666号'
        r = apimgr.customer_modify(id=customerId, name=newName, phonenumber=newPhonenumber, address=newAddress)
        addRet = r.json()
        expected = {"ret": 0}
        # print('expected-----', addRet)
        CHECK_POINT('返回的ret值=0', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.customer_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [
                {
                    "address": newAddress,
                    "id": customerId,
                    "name": newName,
                    "phonenumber": newPhonenumber
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


