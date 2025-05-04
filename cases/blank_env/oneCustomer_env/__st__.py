from lib.webapi import apimgr


# 套件初始化，只执行一次
def suite_setup():
    apimgr.customer_add("武汉市桥西医院1",
                        "13345679901",
                        "武汉市桥西医院北路1")


# 套件清除，只执行一次
def suite_teardown():
    apimgr.order_del_all()
    apimgr.customer_del_all()
