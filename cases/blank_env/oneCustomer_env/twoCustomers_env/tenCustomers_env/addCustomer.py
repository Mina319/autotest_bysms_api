from hytest import CHECK_POINT, STEP, INFO
from lib.webapi import apimgr


class Case_0152:
    name = '添加客户-API-0152'

    def teststeps(self):
        STEP(1, '添加一个客户')
        name, phone, address = '南京市桥东医院', '12245789934', '南京市桥东医院北路'
        r = apimgr.customer_add(name, phone, address)
        addRet = r.json()
        self.customerId = addRet['id']
        print('self.cid----', self.customerId)
        CHECK_POINT('返回的ret值=0', addRet['ret'] == 0)

        STEP(2, '检查系统数据')
        r = apimgr.customer_list(pagesize=11, pagenumber=1)
        listRet = r.json()
        retlist = []

        retlist.append({
            'address': address,
            'id': self.customerId,
            'name': name,
            'phonenumber': phone
        })
        cid = self.customerId
        for i in range(10, 0, -1):
            cid -= 1
            ele = {}
            ele['address'] = f'武汉市桥西医院北路{i}'
            ele['id'] = cid
            ele['name'] = f'武汉市桥西医院{i}'
            ele['phonenumber'] = f'133456799{i:02d}'
            retlist.append(ele)

        expected = {
            "ret": 0,
            "retlist": retlist,
            'total': 11
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)

    def teardown(self):
        # 删除 刚刚添加的客户
        apimgr.customer_del(self.customerId)

