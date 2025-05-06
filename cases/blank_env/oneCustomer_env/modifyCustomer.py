from hytest import CHECK_POINT, STEP
from lib.webapi import apimgr, getRetlist


class Case_0202:
    name = '修改客户-API-0202'
    def teststeps(self):
        STEP(1, '修改客户')
        self.address, self.customerId, self.name1, self.phonenumber = getRetlist().values()
        newName = '武汉市桥西医院北路'.replace('武汉市', '南京市')
        r = apimgr.customer_modify(id=self.customerId, name=newName)
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
                    "address": self.address,
                    "id": self.customerId,
                    "name": newName,
                    "phonenumber": self.phonenumber
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)

    def teardown(self):
        # 如果用例pass，则将客户姓名修改回来
        apimgr.customer_modify(id=self.customerId, name=self.name1)


class Case_0203:
    name = '修改客户-API-0203'
    def teststeps(self):
        STEP(1, '修改客户')
        self.address, self.customerId, self.name1, self.phonenumber = getRetlist().values()
        newphonenumber = '13923567443'
        r = apimgr.customer_modify(id=self.customerId, phonenumber=newphonenumber)
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
                    "address": self.address,
                    "id": self.customerId,
                    "name": self.name1,
                    "phonenumber": newphonenumber
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)

    def teardown(self):
        # 如果用例pass，则将客户phonenumber修改回来
        apimgr.customer_modify(id=self.customerId, phonenumber=self.phonenumber)


class Case_0204:
    name = '修改客户-API-0204'
    def teststeps(self):
        STEP(1, '修改客户')
        self.address, self.customerId, self.name1, self.phonenumber = getRetlist().values()
        newAddress = '镇江市桃花坞123号'
        r = apimgr.customer_modify(id=self.customerId, address=newAddress)
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
                    "id": self.customerId,
                    "name": self.name1,
                    "phonenumber": self.phonenumber
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)

    def teardown(self):
        # 如果用例pass，则将客户address修改回来
        apimgr.customer_modify(id=self.customerId, address=self.address)


class Case_0205:
    name = '修改客户-API-0205'
    def teststeps(self):
        STEP(1, '修改客户')
        self.address, self.customerId, self.name1, self.phonenumber = getRetlist().values()
        newName, newPhonenumber = '镇江市中医院', '1362345887'
        r = apimgr.customer_modify(id=self.customerId, name=newName, phonenumber=newPhonenumber)
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
                    "address": self.address,
                    "id": self.customerId,
                    "name": newName,
                    "phonenumber": newPhonenumber
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)

    def teardown(self):
        # 如果用例pass，则将客户name、phonenumber修改回来
        apimgr.customer_modify(id=self.customerId, name=self.name1, phonenumber=self.phonenumber)


class Case_0206:
    name = '修改客户-API-0206'
    def teststeps(self):
        STEP(1, '修改客户')
        self.address, self.customerId, self.name1, self.phonenumber = getRetlist().values()
        newName, newAddress = '镇江市中医院', '镇江市桃花坞666号'
        r = apimgr.customer_modify(id=self.customerId, name=newName, address=newAddress)
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
                    "id": self.customerId,
                    "name": newName,
                    "phonenumber": self.phonenumber
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)

    def teardown(self):
        # 如果用例pass，则将客户name、address修改回来
        apimgr.customer_modify(id=self.customerId, name=self.name1, address=self.address)


class Case_0207:
    name = '修改客户-API-0207'
    def teststeps(self):
        STEP(1, '修改客户')
        self.address, self.customerId, self.name1, self.phonenumber = getRetlist().values()
        newPhonenumber, newAddress = '1275678433', '镇江市桃花坞666号'
        r = apimgr.customer_modify(id=self.customerId, phonenumber=newPhonenumber, address=newAddress)
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
                    "id": self.customerId,
                    "name": self.name1,
                    "phonenumber": newPhonenumber
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)

    def teardown(self):
        # 如果用例pass，则将客户phonenumber、address修改回来
        apimgr.customer_modify(id=self.customerId, phonenumber=self.phonenumber, address=self.address)


class Case_0208:
    name = '修改客户-API-0208'
    def teststeps(self):
        STEP(1, '修改客户')
        self.address, self.customerId, self.name1, self.phonenumber = getRetlist().values()
        newName, newPhonenumber, newAddress = '镇江市中医院', '1275678433', '镇江市桃花坞666号'
        r = apimgr.customer_modify(id=self.customerId, name=newName, phonenumber=newPhonenumber, address=newAddress)
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
                    "id": self.customerId,
                    "name": newName,
                    "phonenumber": newPhonenumber
                }
            ],
            'total': 1
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)

    def teardown(self):
        # 如果用例pass，则将客户name、phonenumber、address修改回来
        apimgr.customer_modify(id=self.customerId, name=self.name1, phonenumber=self.phonenumber, address=self.address)

