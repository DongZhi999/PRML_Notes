'''
    while 条件表达式： 当条件为Ture的时候进入循环
        要执行的代码块  #执行完里面的代码块则回到条件表达式 进行条件判断
'''
# i= 1
# while i <= 100:  #对初始化条件进行判断 判断成立则进入循环
#     print('i love you')
#     i+=1  #这里对变量进行累加 i = i+1   python中没有i++
# print(i)  #当i自增到5，不满足条件，退出


'''
    计算1-100的和
    1+2+3+...+100
'''
# sum = 0
# i = 1
# while i <= 100:
#     sum += i
#     i +=1
# print('1+2+3+...+100的和为: %d'%sum)


'''
    while循环嵌套
'''
# i = 0
# while i <5:
#     print('这个是外面循环的第%d遍'%i)
#     m = 0
#     while m < 5:
#         print('这个是里面的循环第%d遍'%m)
#         m +=1
#     i +=1
#     print('_'*20)


# i = 0
# while i <5:
#     m = 0
#     while m < 5:
#         print('*'*5)
#         m +=1
#     i +=1
#     print('_'*20)


# i = 0
# while i <5:   # 控制行数
#     m = 0
#     while m <= i:   # 控制个数
#         print('*',end = ' ')  #表示print的结束符为空格 默认是换行
#         m +=1
#     i +=1
#     print()   #print() 默认输出为换行结尾


'''
    while-else语句
    
        while 条件：
            条件成立的代码块
        else:
            条件不成立的代码块
'''
# a = 0   # 初始化变量
# while a < 5:
#     print('爱你一万年')
#     a +=1  # 进行循环，每一次循环自动加1
# else:     #当条件不成立的时候
#     print(a)
#     print('我是至尊宝')


'''
    跳转语句
    break:终止循环，不管循环条件是否为真，都不再循环下去
'''
# a = 0   # 初始化变量
# while a < 5:    #判断条件 a = 0
#     if a == 3:   #判断条件 当a = 3，输出print 跳出循环
#         print('紫霞仙子：别说话，吻我！')
#         break   #直接跳出循环
#     print('至尊宝：爱你一万年')
#     a +=1  # 进行循环，每一次循环自动加1


'''
    示例
'''
# while True:   #给个条件
#     flag = input('你是否要退出程序（y/n）：')
#     print(flag)
#     if flag == 'y':   #当用户的输入等于y时 进入if 跳出循环
#         break


'''
    continue
    跳出当前循环，直接开始下一次循环
'''
a = 0
while a < 10:
    a +=1
    print('第%d圈开始'%a)
    print('好累哈')
    if a == 5:
        print('趁老师不注意，后半圈没跑，直接开始第%d圈'%a)
        continue
    print('第%d圈结束'%a)


    '''
        break:跳出整个循环，不管条件是否为真
        continue:跳出当前循环，直接回到起点开始下一次循环
    '''

