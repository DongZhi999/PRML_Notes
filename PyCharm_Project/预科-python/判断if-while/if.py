'''
    if 条件表达式： 条件成立，则执行
        执行以下代码

'''
# i = 10
# print('-----------if开始')
# if i < 5:
#     print("我比5大")
# print('-----------if结束')


'''
    if 条件表达式：
        要执行的条件代码块
    else:条件成立
        要执行以下代码块
'''
# i = 0
# print('-----------if开始')
# if i < 5:  #条件成立
#     print("我比5大")
# else:    #条件不成立，所以执行以下代码
#     print("我比5小")
# print('-----------if结束')


'''
    if 条件表达式：
        要执行的条件代码块
    elif:条件成立
        要执行以下代码块
    else:条件成立
        要执行以下代码块 
'''
# piao = '没钱'
#
# if piao == '有票':
#     print('我要坐上火车去拉萨')
# elif piao == '没票':
#     print('我要先去补个票')
# else:
#     print('票都没得补，回家睡觉')


'''
    if elif 嵌套
'''
# x = int(input('请输入第一个数：'))
# y = int(input('请输入第二个数：'))
# z = int(input('请输入第三个数：'))

# 先比较 x和y
# if x > y:
#     if x > z:
#         print('最大的数是：%d'%x)
#     else:
#         print('最大的数是：%d'%z)
# elif x > z:
#      if x > y:
#         print('最大的数是：%d'%x)
#      else:
#         print('最大的数是：%d'%y)
# else:
#     if y > z:
#         print('最大的数是：%d'%y)
#     else:
#         print('最大的数是：%d'%z)


'''
    猜拳游戏
    random.randint(x,y) 返回 x 到y 之间的随机数
'''
# import random
# user = input('请输入石头、剪刀、布：')  #接收用户输入的内容
# cont = ['石头','剪刀','布']  #初始化数据
# num = random.randint(0,2)  #获取0-2随机数
#
# if user == '石头':
#     if cont[num] == '石头':
#         print('用户输入的是%s,电脑输入的是%s，平局'%(user,cont[num]))
#     elif cont[num] == '剪刀':
#         print('用户输入的是%s,电脑输入的是%s，你赢了'%(user,cont[num]))
#     elif cont[num] == '布':
#         print('用户输入的是%s,电脑输入的是%s，电脑赢了'%(user,cont[num]))
# elif user == '剪刀':
#     if cont[num] == '石头':
#         print('用户输入的是%s,电脑输入的是%s，电脑赢了'%(user,cont[num]))
#     elif cont[num] == '剪刀':
#         print('用户输入的是%s,电脑输入的是%s，平局'%(user,cont[num]))
#     elif cont[num] == '布':
#         print('用户输入的是%s,电脑输入的是%s，你赢了'%(user,cont[num]))
# elif user == '布':
#     if cont[num] == '石头':
#         print('用户输入的是%s,电脑输入的是%s，你赢了'%(user,cont[num]))
#     elif cont[num] == '剪刀':
#         print('用户输入的是%s,电脑输入的是%s，你输了'%(user,cont[num]))
#     elif cont[num] == '布':
#         print('用户输入的是%s,电脑输入的是%s，平局'%(user,cont[num]))
# else:
#     print('您的输入有误，拜拜！')


'''
    练习
'''
# score = int(input('请输入分数：'))
# if score >= 90:
#     print('同学你好棒棒!你的成绩是A')
# elif 60 <= score <=89:
#     print('同学表现还不错！你的成绩是B')
# else:
#     print('同学你要加油哟！')

