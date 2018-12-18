''''''
'''
    自定义模块
'''
# import test   #引入同级目录的test模块
# print(test.test_add(2,3))

# from test import test_add
# print(test_add(2,3))


'''
    跨模块引入1
'''
# import study.test2   #模块名.函数名
# print(study.test2.test2_add(2,3))

# from study import test2
# print(test2.test2_add(2,3))


'''
    跨模块引入2
'''
# import sys      #查看路径变量
# print(sys.path)
# 添加目标路径到当前环境中
# sys.path.append('..\\')   #返回上一级目录
# import msg.send
# msg.send.sendMsg()

# from msg import send,recv  #可以同时引入多个模块
# send.sendMsg()
# recv.sendMsg()

# import math as m    #引入的是标准模块
# print(m.ceil(1.1))   #向上取整
# print(m.floor(1.1))  #向下取整

#覆盖标准模块
# from msg import math   #自定义的模块
# print(math.ceil(1.1))   #向上取整
# print(math.floor(1.1))  #向下取整
# math.math()


'''
    dir
    用于按模块名搜索模块定义，他返回一个字符串类型的存储列表
    该列表列出了所有类型的名称：变量，模块，函数，等等
'''
# print(dir())


'''
    python中的包
'''
import sys      #查看路径变量
# print(sys.path)
# 添加目标路径到当前环境中
sys.path.append('..\\')   #返回上一级目录

# 通过import 方式 逐个导入模块
# import msg.send
# msg.send.sendMsg()
# import msg.recv
# msg.recv.sendMsg()

#通过from 方式，一次性导入所有的模块
#做一个包一定要创建一个__init__.py  这个文件中要设置 __all__ = ['运行导入的模块名']
# from msg import *
# send.sendMsg()
# recv.sendMsg()


'''
    重新加载
    
'''
import test
# import test   # 引入两遍只输入一句 haha
import imp
imp.reload(test)  #重新导入test模块
