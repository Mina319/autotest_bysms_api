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


class Case_0108:
    name = '列出客户-API-0108'

    def teststeps(self):
        STEP(1, '列出客户')
        r = apimgr.customer_list(pagenumber=1, pagesize=10)
        # CHECK_POINT('返回状态码是302', r.status_code == 302)
        INFO(f'返回状态码是{r.status_code}')
        # 验证返回体
        listRet = r.json()

        retlist = []
        cid = getRetlist()['id']
        print('cid----', cid)
        for i in range(10, 0, -1):
            ele = {}
            ele['address'] = f'武汉市桥西医院北路{i}'
            ele['id'] = cid
            ele['name'] = f'武汉市桥西医院{i}'
            ele['phonenumber'] = f'133456799{i:02d}'
            cid -= 1
            retlist.append(ele)

        expected = {
            "ret": 0,
            "retlist": retlist,
            'total': 10
        }
        print('expected------', expected)
        print('listRet------', listRet)
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0109:
    name = '列出客户-API-0109'

    def teststeps(self):
        STEP(1, '列出客户')
        r = apimgr.customer_list(pagenumber=2, pagesize=10)
        # CHECK_POINT('返回状态码是302', r.status_code == 302)
        INFO(f'返回状态码是{r.status_code}')
        # 验证返回体
        listRet = r.json()

        expected = {
            "ret": 0,
            "retlist": [],
            'total': 10
        }
        print('expected------', expected)
        print('listRet------', listRet)
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0110:
    name = '列出客户-API-0110'

    def teststeps(self):
        STEP(1, '列出客户')
        r = apimgr.customer_list(pagenumber=3, pagesize=10)
        # CHECK_POINT('返回状态码是302', r.status_code == 302)
        INFO(f'返回状态码是{r.status_code}')
        # 验证返回体
        listRet = r.json()

        expected = {
            "ret": 0,
            "retlist": [],
            'total': 10
        }
        print('expected------', expected)
        print('listRet------', listRet)
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0111:
    name = '列出客户-API-0111'

    def teststeps(self):
        STEP(1, '列出客户')
        r = apimgr.customer_list(pagenumber=3, pagesize=5)
        # CHECK_POINT('返回状态码是302', r.status_code == 302)
        INFO(f'返回状态码是{r.status_code}')
        # 验证返回体
        listRet = r.json()

        expected = {
            "ret": 0,
            "retlist": [],
            'total': 10
        }
        print('expected------', expected)
        print('listRet------', listRet)
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0112:
    name = '列出客户-API-0112'

    def teststeps(self):
        STEP(1, '列出客户')
        r = apimgr.customer_list(pagenumber=1, pagesize=10, keywords='你好')
        # CHECK_POINT('返回状态码是302', r.status_code == 302)
        INFO(f'返回状态码是{r.status_code}')
        # 验证返回体
        listRet = r.json()

        expected = {
            "ret": 0,
            "retlist": [],
            'total': 0
        }
        print('expected------', expected)
        print('listRet------', listRet)
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0113:
    name = '列出客户-API-0113'

    def teststeps(self):
        STEP(1, '列出客户')
        r = apimgr.customer_list(pagenumber=1, pagesize=10, keywords='武汉')
        # CHECK_POINT('返回状态码是302', r.status_code == 302)
        INFO(f'返回状态码是{r.status_code}')
        # 验证返回体
        listRet = r.json()

        retlist = []
        cid = getRetlist()['id']
        print('cid----', cid)
        for i in range(10, 0, -1):
            ele = {}
            ele['address'] = f'武汉市桥西医院北路{i}'
            ele['id'] = cid
            ele['name'] = f'武汉市桥西医院{i}'
            ele['phonenumber'] = f'133456799{i:02d}'
            cid -= 1
            retlist.append(ele)

        expected = {
            "ret": 0,
            "retlist": retlist,
            'total': 10
        }
        print('expected------', expected)
        print('listRet------', listRet)
        CHECK_POINT('返回的消息体数据正确', listRet == expected)
