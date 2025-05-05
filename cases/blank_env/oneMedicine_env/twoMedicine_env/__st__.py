from lib.webapi import apimgr


# 套件初始化，只执行一次
def suite_setup():
    # 添加一个药品
    apimgr.medicine_add("青霉素2",
                        "青霉素 国字号2",
                        "099877883802")


# 套件清除，只执行一次
def suite_teardown():
    pass
