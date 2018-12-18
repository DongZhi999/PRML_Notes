#  lambda [参数]：表达式（默认返回）

#没有参数的的匿名函数
# s = lambda :'hahaha'
# print(s())   # 调用

# 没有参数的的匿名函数
# s = lambda x,y:x+y
# print(s(2,9))

# 矢量化的三元运算符
# s = lambda x,y:x if x>2 else y
# print(s(0,100))

# 字典排序
dic = {'a':1,'c':3,'b':2}
# dic.sort() 错误，不能直接对字典元素用sort 进行排序
# 通过内置函数 sorted 进行排序
dic = sorted(dic)
# 内置函数，有返回值
print(dic)
# 返回key ,形成列表

'''
    高阶函数
'''
# map 高阶函数
# list01 = [1,2,3,4,5]
# list02 = [2,4,6,8,10]
# new_list = map(lambda x,y:x*y,list01,list02)   #对应元素的乘积
# print(list(new_list))

#filter 高阶函数
# list02 = [2,4,6,8,10]
# new_list = filter(lambda x:x>4,list02)  #过滤
# print(list(new_list))

#reduce
# from functools import reduce
# list02 = [2,4,6,8,10]
# new_list = reduce(lambda x,y:x+y,list02)  #第一次把2,4分别给x,y  把x+y的结果给下一次的x，把6给下一次的y
# print(new_list)

'''
    示例
'''
name = ['joe','susan','black','lili']
age = [18,19,20,21]
sex = ['m','w','m','w']
#格式化用户的英文名，要求首字母大写，其他字母小写
# new_name = map(lambda x:x.title(),name)
# new_name = list(new_name)
# print(new_name)

#将用户英文名，年龄，性别三个集合的数据结合到一起，形成一个元组列表
# new_users = map(lambda x,y,z:(x,y,z),name,age,sex)
# new_users = list(new_users)
# print(new_users)

#过滤性别为男性的用户
# new_users = map(lambda x,y,z:(x,y,z),name,age,sex)
# new_users = list(new_users)
# new_users = filter(lambda x:x[2]=='m',new_users)
# new_users = list(new_users)
# print(new_users)

#求性别为男的用户的平均年龄
# from functools import reduce
# total_age = reduce(lambda x,y:x+y[1],new_users,0)
# print(total_age/len(new_users))
