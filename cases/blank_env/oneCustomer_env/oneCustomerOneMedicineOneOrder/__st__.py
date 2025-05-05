from lib.webapi import apimgr


def getRetlist():
    # 获取系统中客户信息
    r = apimgr.customer_list(1, 1)
    ret = r.json()
    retlist = ret['retlist'][0]
    print('retlist:', retlist)
    # {'address': '武汉市桥西医院北路', 'id': 284, 'name': '武汉市桥西医院', 'phonenumber': '13345679934'}
    return retlist


# 套件初始化，只执行一次
def suite_setup():
    # 新建一个药品、一个订单
    r = apimgr.medicine_add("青霉素1",
                            "青霉素 国字号1",
                            "099877883801")
    mid = r.json()["id"]
    r1 = apimgr.order_add("订单1", getRetlist()["id"],
                     medicinelist=[{"id": mid, "amount": "5", "name": "青霉素1"}])
    print('r1.json()----', r1.json())


# 套件清除，只执行一次
def suite_teardown():
    # 删除所有订单和药品
    apimgr.order_del_all()
    apimgr.medicine_del_all()
    pass
