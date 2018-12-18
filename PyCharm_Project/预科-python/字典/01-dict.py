'''
    创建字典
'''
# dict01 = {'name':'joe','age':'18','address':'上海'}
# print(dict01)

'''
    访问字典
'''
dict01 = {'name':'joe','age':'18','address':'上海'}
# print(dict01['name'])   # 指代性很强，很明了
# 修改字典元素，通过找到指定的KEY进行修改
# dict01['name'] = 'jack'
# print(dict01)
dict01['hobby'] = '足球'  #在字典中添加元素
# print(dict01)

'''
    删除字典
'''
# del
# del dict01['address']  #删除字典中指定元素
# del dict01  # 删除了整个字典
# print(dict01)

'''
    字典函数
'''
# str
# str1 = str(dict01)
# print(str1)

# get
# print(dict01.get('name'))
# 如果字典工有该对应的元素，如果没有则输出指定的

print(dict01.keys())   #输出所有元素的下标
print(dict01.values())   #输出所有元素的值
print(dict01.items())    #将键值返回，并以元组保存起来
