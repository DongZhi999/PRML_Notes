'''
    for 变量 in 序列：
        执行的代码
'''
# list01 = ['jie','susan','jack','Tom']
# # 遍历列表
# for i in list01:  # 遍历list01 这个列表，将列表中的元素一次赋值给i
#     print(i)    #输出变量i  直到将所有的元素遍历完毕，停止遍历


# 用while遍历
# list01 = ['jie','susan','jack','Tom']
# i = 0
# while i < len(list01):  #通过len() 来获取list01的长度
#     print(list01[i])  #通过列表元素下标来获取元素
#     i +=1


# favorite_places = {'张三':['上海','北京','深圳'],'李四':['张家界','九寨沟','鼓浪屿']}
# name = input('请输入姓名：')
# for i in favorite_places:
#     # print(i)   #遍历字典，可以得到字典下标
#     if name == i:  #遍历字典获取key 然后通过key 和输入的值判断
#         print(favorite_places[name])


list01 = ['joe','susan','jack','Tom']
# 遍历列表
for i in list01:  # 遍历list01 这个列表，将列表中的元素一次赋值给i
    if i == 'susan':
        # break  #终止循环
        continue  #终止本次循环
    print(i)    #输出变量i  直到将所有的元素遍历完毕，停止遍历


'''
    pass 不执行任何操作或者命令
'''


