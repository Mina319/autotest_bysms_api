from hytest import CHECK_POINT, STEP
from lib.webapi import apimgr, getRetlist


class Case_0252:
    name = '删除客户-API-0252'

    def teststeps(self):
        self.address, self.customerId, self.name1, self.phonenumber = getRetlist().values()
        STEP(1, f'删除客户：id为{self.customerId}')
        r = apimgr.customer_del(cid=self.customerId)
        addRet = r.json()
        expected = {"ret": 0}
        # print('expected-----', addRet)
        CHECK_POINT('返回的ret值=0', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.customer_list(1, 1)
        listRet = r.json()
        expected = {
            "ret": 0,
            "retlist": [],
            'total': 0
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)

    def teardown(self):
        # 如果用例pass，则将删除的客户添加回来
        apimgr.customer_add(address=self.address, name=self.name1, phonenumber=self.phonenumber)


