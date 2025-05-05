from lib.webapi import apimgr


# 套件初始化，只执行一次
def suite_setup():
    # 添加一个药品
    apimgr.medicine_add("青霉素1",
                        "青霉素 国字号1",
                        "099877883801")


# 套件清除，只执行一次
def suite_teardown():
    apimgr.order_del_all()
    apimgr.medicine_del_all()
