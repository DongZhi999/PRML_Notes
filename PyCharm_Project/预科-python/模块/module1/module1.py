''''''
'''
    import 模块名[,模块名]
    导入整个模块
    通过 模块名.方法名  调用
'''
# import time   #引入time 模块
# print('start')
# # sleep(5)    #错误使用
# # 调用time 模块   调用方式：模块名.函数名
# time.sleep(5)     # 睡眠5秒钟
# print('stop')

'''
    from 模块名 import 函数名
    从指定的模块中导入指定的部分
'''
# from time import sleep
# print('start')
# sleep(5)     # 睡眠5秒钟
# print('stop')

# 导入模块中的所有内容
# from math import *
# print(ceil(1.1))   #向上取整
# print(floor(1.1))  #向下取整


'''
    给导入模块取别名
'''
import math as m
print(m.ceil(1.1))   #向上取整
print(m.floor(1.1))  #向下取整
