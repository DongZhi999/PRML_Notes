''''''
'''
    函数的返回值
    return关键字实现
'''
# def max(x,y):
#     if x>y:
#         return x   #结束函数的运行 并且将结果返回给调用的地方
#     else:
#         return y   #返回函数值，且后面的代码不执行
#         print(y)   # 没有执行print
# num = max(1,2)   #声明一个变量num  接收调用函数后的返回值
# print(num)


# return 返回多个返回值
# def sum(x: object, y: object) -> object:
#     return x,y
# num = sum(1,2)  #用一个变量取接收多个返回值，会保存在一个元组中
# print(num)

# num1,num2 = sum(1,2)  #接收多个返回值时，将第一个返回值保存在num1中，第二个返回值保存在num2中
# print(num1)
# print(num2)


'''
    return 有什么用？
    在哪里获取返回值？   将结果返回到调用的地方
    return 之后的代码会运行吗？    不会运行
'''

'''
    yield 生成器
    生产一个迭代器
        -》yield 的作用是把一个函数变成一个generator
        -》使用生成器，可以达到延迟操作的效果，所谓延迟操作就是指在需要时产生，
        而不是立即产生就结果，节省资源消耗，和声明一个序列不同的是生成器，在
        不使用的时候，几乎是不占用内存的。
'''

# def getNum(n):
#     i = 0
#     while i <= n:
#         # print(i)   #打印 i
#         # return i     # return 返回一个 i ，结束函数的运行
#         yield i      #将函数变成 generator
#         i += 1
# 调用函数
# print(getNum(5))

# a = getNum(5)    # 把生成器赋值给一个变量a
#  使用生成器，通过 next()方法
# print(next(a))
# print(next(a))
# for 循环遍历一个生成器
# for i in a:
#     print(i)

# a = [x for x in range(10000000)]    #这样生成很多数据的大列表，会占用很多内存
# print(a)

# a = (x for x in range(10000000))    #这样生成很多数据的大列表，会占用很多内存
# print(a)
# print(next(a))


'''
    send
'''
# def gen():
#     i = 0
#     while i <= 5:
#         temp = yield i      # 是赋值操作吗？ 不是
#         #使用例yield 后是一个生成器
#         print(temp)   #因为 yield 之后，返回结果到调用者的地方，暂停运行
#                       #赋值操作并没有运行
#         i +=1
# a = gen()
# print(next(a))
# print(next(a))
# print(a.send('我是a'))   #到可以将值发送到上一次yield 的地方


'''
    迭代器（iterator）
    什么是迭代对象？
    可以用for in 遍历的对象 都可以叫做是迭代对象：Iterable
    list string dict
    凡是可以用作于next() 函数的对象都是iterator
'''
# list01 = [1,2,3,4,5]    # 是一个可迭代对象
# for i in list01:
#     print(i)
# print(next(list01))      #list01 不是迭代器，所以无法调用

# 通过iter() 将一个迭代对象变成迭代器
# a = iter(list01)
# print(a)
# print(next(a))
