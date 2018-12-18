'''
    访问列表
    列表是一个可变的类型数据
    允许我们队里面的元素进行修改
'''
# list01 = ['jack','jane','joe','black']
# print(list01[2])   #通过下标进行访问

# list01 = ['jack','jane',['leonado','joe'],'black']
# list01[0] = 'lili'  #通过下标获取到元素，并给其赋新的值
# list01[2][0] = 'susan'  #通过下标获取到元素，并给其赋新的值
# print(list01)  #列表中带列表的访问方法


'''
    列表的操作
        -》 append往列表的末尾增加元素
'''
# append
# list02 = ['jack','jane','joe','black']
# list02.append('susan')   #往list02中末尾添加'susan'
# print(list02)

# insert
# list02 = ['jack','jane','joe','black']
# print('追加前：')
# print(list02)
# print('追加后：')
# list02.insert(1,'susan')   #往list02中下标为1的位置添加'susan'，原来往后挪动
# print(list02)

'''
    删除元素
        -》 pop 默认删除最后一个
        -》 del 通过指定位置删除
        -》 remove 通过元素的值进行删除
'''
# pop
# list03 = ['jack','jane','joe','black']
# print('删除前：')
# print(list03)
# print('删除后：')
# # list03.pop()     #在list02中默认删除最后一个
# print(list03.pop())
# print(list03)
# print('继续删除后：')
# print(list03.pop(0),)  #pop() 可以指定删除元素的位置
# print(list03)
#

# del
# list03 = ['jack','jane','joe','black']
# print('删除前：')
# print(list03)
# print('删除后：')
# del list03[1]   #在list02中指定删除下标为1的元素
# print(list03)

# remove
# list03 = ['jack','jane','joe','black']
# print('删除前：')
# print(list03)
# print('删除后：')
# list03.remove('jane')   #在list02中指定删除'jane'元素
# print(list03)


# 查找元素
# list04 = ['jack','jane','joe','black']
# name = 'jack'
# print(name in list04)     #list04 中有name,返回值我Ture
# print(name not in list04)     #list04 中没有有name,返回值我False


'''
    列表函数
        
'''
list05 = ['jack','jane','joe','black','joe']

#查看列表的长度
# print(len(list05))   #将列表个数读出，返回列表元素的个数

#返回列表元素的最大值 （必须是同类型的数据，才能用来比较大小 ）
# print(list05.count('joe'))

# extend 扩展列表元素
ll = ['aaa','bbb']
list05.extend(ll)
print(list05)
