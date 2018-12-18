'''
    创建元组    不可变类型
'''
tup01 = (1,2,3,4,5)
# print(tup01[1])
#
# tup01[0] = 9  # 不可以改变其中的值，所以会报错
# print(tup01)

# 删除元组
# del tup01   #彻底删除
# print(tup01)
# print(len(tup01))  #输出元组的长度
print(type(tup01))    #输出类型
l = list(tup01)      #将元组转换成列表
print(type(l))
tup02 = tuple(l)     #再将列表转换成元组
print(type(tup02))
