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
