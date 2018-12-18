''''''
'''
    函数：
        -》组织好的，可重复使用的、用户实现单一或者关联功能的代码段。
        
        函数代码块定义：
            def 函数名（[参数]）：
                #函数说明
                要封装的代码块
        调用函数：
'''
# def Pname():
#     '''
#         获取姓名
#     :return:
#     '''
    # print('大家好，我是小明同学！')

# 显然没有参数，直接调用
# Pname()   #调用函数，执行函数里面的代码
# pri = Pname()  #将函数名赋值给另一个变量，给当前函数取一个别名
# pri()


# def getNum():    #定义函数
#     print('100')  #函数代码块
# getNum()   #调用函数


'''
    函数的参数
'''
# def Pname(userName):      #userName是形参   形参的名字是自定义的
#     '''
#         获取姓名
#     :return:
#     '''
#     print('大家好，我是%s同学！'%userName)
#
# Pname('刘德华')   #传递了一个实参   '刘德华'


# 必备参数
# def getInfo(name,aadders):
#     print('大家好，我叫%s,我来自%s！'%(name,aadders))
#
# getInfo('刘德华','香港')      #有两个形参，对应也得有两个实参，且要一一对应


# 关键字参数
# def getInfo(name,aadders):    #有默认值参数尽量往右边放
#     print('大家好，我叫%s,我来自%s！'%(name,aadders))
# getInfo(name='刘德华',aadders='香港')   #给实参加上关键字    关键字对应形参


# 不定长参数
# def getInfo(name,aadders,*args,**args2):    #有默认值参数尽量往右边放   args带* 是接收所有未命名的参数
#     print('大家好，我叫%s,我来自%s！'%(name,aadders))
#     print(args)    # *args 是一个元组  将未命名的参数a,b,c,d（不带关键字） 以元组的形式放到args中
#     print(args2)   # **args2 是一个字典  将未命名的参数 age=18(带关键字)  以字典的形式放到args2中
#
# getInfo('刘德华','香港','a','b','c','d',age = 18)


'''
    可变对象与不可变对象的传递
'''
#标记函数
def sign():
    print('_'*50)

# 值传递，不可变对象的传递
# def fun(args):
#     args = 'hello'  # 重新赋值hello
#     print(args)      # 输出hello
#
# str1 = 'baby'   #声明一个字符串的变量    不可变数据类型
# fun(str1)        #将字符串传递到函数中
# sign()
# print(str1)      #还是 baby 并没有改变

# 引用传递 ： 可变对象的传递
# def fun(args):
#     # args[0] = 'hello'  # 重新赋值hello
#     print(args)      # 输出hello
#
# list01 = ['baby','come on']   #声明一个列表的变量    可变数据类型
# fun(list01)        #将列表传递到函数中
# sign()
# print(list01)      #传递的是对象本身，函数里面被修改了值，原对象也会跟着修改


