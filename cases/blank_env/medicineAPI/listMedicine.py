from hytest import CHECK_POINT, STEP, INFO
from lib.webapi import apimgr


class Case_0301:
    name = '列出药品-API-0301'

    def teststeps(self):
        STEP(1, '尝试列出药品，没有携带有效的sessionid')
        headers = {}
        headers['Cookie'] = 'sessionid='
        r = apimgr.medicine_list1(10, 1, headers=headers)
        INFO(f'返回状态码是{r.status_code}')
        # 验证返回体
        listRet = r.json()
        INFO(f'listRet{listRet}')
        expected = {
            "ret": 302,
            "msg": "未登录",
            "redirect": "/mgr/sign.html"
        }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0302:
    name = '列出药品-API-0302'

    def teststeps(self):
        STEP(1, '尝试列出药品，没有携带有效的sessionid')
        r = apimgr.medicine_list(10, 1)
        INFO(f'返回状态码是{r.status_code}')
        CHECK_POINT('检查状态码', r.status_code == 200)
        # 验证返回体
        listRet = r.json()
        INFO(f'listRet{listRet}')
        expected = {
                    "ret": 0,
                    "retlist": [],
                    'total': 0
                }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0303:
    name = '列出药品-API-0303'

    def teststeps(self):
        STEP(1, '列出药品')
        r = apimgr.medicine_list(pagenumber='hello', pagesize=10)
        INFO(f'返回状态码是{r.status_code}')
        # 验证返回体
        listRet = r.json()
        INFO(f'listRet{listRet}')
        expected = {
                "ret": 1,
                "msg":  "请求参数错误"
                }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0304:
    name = '列出药品-API-0304'

    def teststeps(self):
        STEP(1, '列出药品')
        r = apimgr.medicine_list(pagesize='hello', pagenumber=1)
        INFO(f'返回状态码是{r.status_code}')
        # 验证返回体
        listRet = r.json()
        INFO(f'listRet:{listRet}')
        # listRet{'msg': 'bad pagesize:hello', 'ret': 2}
        expected = {
                "ret": 1,
                "msg":  "请求参数错误"
                }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0305:
    name = '列出药品-API-0305'

    def teststeps(self):
        STEP(1, '列出药品')
        r = apimgr.medicine_list(pagesize=10)
        INFO(f'返回状态码是{r.status_code}')
        # 验证返回体
        listRet = r.json()
        INFO(f'listRet:{listRet}')
        # listRet{'msg': 'bad pagesize:hello', 'ret': 2}
        expected = {
                "ret": 1,
                "msg":  "请求参数错误"
                }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0306:
    name = '列出药品-API-0306'

    def teststeps(self):
        STEP(1, '列出药品')
        r = apimgr.medicine_list(pagenumber=1)
        INFO(f'返回状态码是{r.status_code}')
        # 验证返回体
        listRet = r.json()
        INFO(f'listRet:{listRet}')
        # listRet{'msg': 'bad pagesize:hello', 'ret': 2}
        expected = {
                "ret": 1,
                "msg":  "请求参数错误"
                }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)


class Case_0307:
    name = '列出药品-API-0307'

    def teststeps(self):
        STEP(1, '列出药品')
        r = apimgr.medicine_list(pagenumber=1, pagesize=10)
        INFO(f'返回状态码是{r.status_code}')
        # 验证返回体
        listRet = r.json()
        INFO(f'listRet:{listRet}')
        # listRet{'msg': 'bad pagesize:hello', 'ret': 2}
        expected = {
                "ret": 1,
                "msg":  "请求参数错误"
                }
        CHECK_POINT('返回的消息体数据正确', listRet == expected)

