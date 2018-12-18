''''''
'''
    __name__ :如果放在Moudle中，就表示模块的名字
              如果放在Class类中，就表示类的名字
    __main__ :模块，xxx.py文件本身.被直接执行时，对应的模块名，就是__main__了
              可以在if __name__ == '__main__':
              中添加你自己想要的，用于测试模块，演示模块等代码
'''
def a():
    print('我是A方法')

if __name__ == '__main__':
    a()
print(__name__)   #当前脚本运行，输出 __main__
