'''
    直接赋值

'''
# a = [1,2,3]
# b = a
# print(id(a))    #通过id查看变量在内存中的地址
# print(id(b))    #a、b 都指向同一个地址
#
# a[0] = 5
# print(a)     #a b都指向一个内存地址，a改变，b也会改变，即b是a的别名
# print(b)


# 浅拷贝
# a = [1,2,3]
# b = [11,22,33]
# c = [111,222,333]
#
# list01 = [a,b,c]
# print(id(list01))
# list02 = list01[:]   #切片导致 新开辟了一个地址
# # 查看list01 和 list02
# print(list01)
# print(list02)
#
# # 检查 list01 和 list02 在内存中的地址
# print(id(list01))
# print(id(list02))
#
# # 修改一下
# a[0] = 5
# # print(a)
# print(list01)  #list01 和list02 列表不同，实际上他们内部的元素相同
# print(list02)

# 深拷贝操作
import copy
a = [1,2,3]
b = [11,22,33]
c = [111,222,333]

list01 = [a,b,c]
print(id(list01))

list02 = copy.deepcopy(list01)    #深拷贝
# 修改一下
a[0] = 5

print(list01)   #list01 改变，而list02 不发生改变
print(list02)

print(id(list01))  #list01 和 list02 不但内存不同，而且他们之间的内存元素也从新开辟一个空间了
print(id(list02))  #深拷贝会递归的拷贝子对象，可变对象一般用深拷贝，避免改变元素，影响原来在用的列表元素值
