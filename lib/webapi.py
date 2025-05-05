import requests
from pprint import pprint
from hytest import INFO


class APIMgr:

    def _printResponse(self, response):
        INFO('\n-------- HTTP response * begin -------')
        INFO(response.status_code)

        for k, v in response.headers.items():
            INFO(f'{k}: {v}')

        INFO('')

        INFO(response.content.decode('utf8'))
        INFO('-------- HTTP response * end -------\n')

    def mgr_login(self, username='byhy', password='88888888', useProxy=False):
        self.s = requests.Session()

        if useProxy:
            self.s.proxies.update({'http': 'http://127.0.0.1:8888'})

        response = self.s.post("http://127.0.0.1/api/mgr/signin",
                               data={
                                   'username': username,
                                   'password': password
                               }
                               )
        self._printResponse(response)
        return response

    def mgr_login1(self, data, raw=False):
        INFO('登录系统')
        if raw:
            response = self.s.post("http://127.0.0.1/api/mgr/signin",
                                   data=data,
                                   headers={'Content-Type': 'application/json'})
        else:
            response = self.s.post("http://127.0.0.1/api/mgr/signin",
                                   data=data)
        self._printResponse(response)
        return response

    def customer_list(self, pagesize=None, pagenumber=None, keywords=None):
        INFO('列出客户')
        response = self.s.get("http://127.0.0.1/api/mgr/customers",
                              params={
                                  'action': 'list_customer',
                                  'pagesize': pagesize,
                                  'pagenum': pagenumber,
                                  'keywords': keywords,
                              })
        self._printResponse(response)
        return response

    def customer_list1(self, pagesize=10, pagenumber=1, keywords=None, headers=None):
        INFO('列出客户')
        response = self.s.get("http://127.0.0.1/api/mgr/customers",
                              params={
                                  'action': 'list_customer',
                                  'pagesize': pagesize,
                                  'pagenum': pagenumber,
                                  'keywords': keywords,
                              }, headers=headers)
        self._printResponse(response)
        return response

    def customer_add(self, name, phonenumber, address):
        INFO('添加客户')
        response = self.s.post("http://127.0.0.1/api/mgr/customers",
                               json={
                                   "action": "add_customer",
                                   "data": {
                                       "name": name,
                                       "phonenumber": phonenumber,
                                       "address": address
                                   }})

        self._printResponse(response)
        return response

    def customer_add2(self, data):
        INFO('添加客户')
        # data 是 Python 字典，正常情况
        response = self.s.post("http://127.0.0.1/api/mgr/customers",
                               json={
                                   "action": "add_customer",
                                   "data": data
                               })
        self._printResponse(response)
        return response

    def customer_del(self, cid):
        INFO(f'删除客户：id={cid}')
        response = self.s.delete("http://127.0.0.1/api/mgr/customers",
                                 json={
                                     "action": "del_customer",
                                     "id": cid
                                 })
        self._printResponse(response)
        return response

    def customer_del_all(self):
        INFO('删除所有客户')
        response = self.customer_list(100, 1)
        theList = response.json()['retlist']  # 将消息体内容转为json格式
        for customer in theList:
            self.customer_del(customer['id'])

    def customer_modify(self, id, name=None, phonenumber=None, address=None):
        INFO('修改客户')

        newdata = {}
        if name is not None:
            newdata["name"] = name
        if phonenumber is not None:
            newdata["phonenumber"] = phonenumber
        if address is not None:
            newdata["address"] = address

        # 发送请求
        response = self.s.put("http://127.0.0.1/api/mgr/customers",
                              json={
                                  "action": "modify_customer",
                                  "id": id,
                                  "newdata": newdata
                              })

        self._printResponse(response)
        return response

    def medicine_del(self, mid):
        INFO(f'删除药品：id={mid}')
        response = self.s.delete("http://127.0.0.1/api/mgr/medicines",
                                 json={
                                     "action": "del_medicine",
                                     "id": mid
                                 })
        self._printResponse(response)
        return response

    def medicine_list(self, pagesize=None, pagenumber=None, keywords=None):
        INFO('列出药品')
        response = self.s.get("http://127.0.0.1/api/mgr/medicines",
                              params={
                                  'action': 'list_medicine',
                                  'pagesize': pagesize,
                                  'pagenum': pagenumber,
                                  'keywords': keywords,
                              })

        self._printResponse(response)
        return response

    def medicine_list1(self, pagesize, pagenumber, keywords=None, headers=None):
        INFO('列出药品')
        # 发送请求
        response = self.s.get("http://127.0.0.1/api/mgr/medicines",
                              params={
                                  'action': 'list_medicine',
                                  'pagesize': pagesize,
                                  'pagenum': pagenumber,
                                  'keywords': keywords,
                              },
                              headers=headers)  # 使用传入的 headers
        # 打印响应内容
        self._printResponse(response)
        return response

    def medicine_add(self, name=None, desc=None, sn=None):
        INFO('添加药品')
        data = {}
        if name is not None:
            data["name"] = name
        if desc is not None:
            data["desc"] = desc
        if sn is not None:
            data["sn"] = sn
        response = self.s.post("http://127.0.0.1/api/mgr/medicines",
                               json={
                                   "action": "add_medicine",
                                   "data": data})
        self._printResponse(response)
        return response

    def medicine_add2(self, data):
        INFO('添加药品')
        response = self.s.post("http://127.0.0.1/api/mgr/medicines",
                               json={
                                   "action": "add_medicine",
                                   "data": data
                               })
        self._printResponse(response)
        return response


    def medicine_del_all(self):
        INFO('所有药品')
        response = self.medicine_list(pagesize=100, pagenumber=1)
        theList = response.json()['retlist']  # 将消息体内容转为json格式
        for one in theList:
            self.medicine_del(one['id'])

    def order_del(self, oid):
        INFO(f'删除订单：id={oid}')
        response = self.s.delete("http://127.0.0.1/api/mgr/orders",
                                 json={
                                     "action": "delete_order",
                                     "id": oid
                                 })
        self._printResponse(response)
        return response

    def order_list(self, pagesize, pagenumber, keywords=None):
        INFO('列出订单')
        response = self.s.get("http://127.0.0.1/api/mgr/orders",
                              params={
                                  'action': 'list_order',
                                  'pagesize': pagesize,
                                  'pagenum': pagenumber,
                                  'keywords': keywords,
                              })

        self._printResponse(response)
        return response

    def order_del_all(self):
        INFO('删除所有订单')
        response = self.order_list(100, 1)
        theList = response.json()['retlist']  # 将消息体内容转为json格式
        for one in theList:
            self.order_del(one['id'])


apimgr = APIMgr()
