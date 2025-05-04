from lib.webapi import apimgr


# 套件初始化，只执行一次
# 创建8个客户
def suite_setup():
    for i in range(3, 11):
        apimgr.customer_add(f"武汉市桥西医院{i}",
                            f"133456799{i:02d}",
                            f"武汉市桥西医院北路{i}")

# 套件清除，只执行一次
def suite_teardown():
    pass
