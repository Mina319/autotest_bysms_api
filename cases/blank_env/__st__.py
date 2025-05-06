from lib.webapi import apimgr


# 套件初始化，只执行一次
def suite_setup():
    apimgr.mgr_login()
    apimgr.order_del_all()
    apimgr.customer_del_all()
    apimgr.medicine_del_all()


# 套件清除，只执行一次
def suite_teardown():
    pass
