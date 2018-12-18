# name = 'joe'
# age = 18
# address = '上海'
# print('大家好我叫%s,今年%d岁，我来自%s'%(name,age,address))   #位置一一对应，%s %d 均为占位符
# print("大家好!我叫%s"%name)


'''
    字符串常用函数
'''
# find
# str = 'i love python'   #返回的是该字符的位置
# print(str.find('o'))     #寻找某个字符
# print(str.find('w'))     #没有则返回-1


# index
# str = 'i love python'   #返回的是该字符的位置
# print(str.index('o'))     #寻找某个字符
# print(str.index('w'))     #没有则返回报错信息


# count
# str = 'i love python o'   #返回的是该字符的个数
# print(str.count('o'))     #寻找某个字符
# print(str.count('o',2,len(str)))  #规定制定位置查找
# print(str.count('w'))     #没有则返回0


# replace
# str = 'i love python o'
# print(str.replace('p','P'))   #字符替换，将小写p替换成大写的P


# split
# str = 'i love python o'
# print(str.split(' '))   #返回一个列表，指定空格为切割符


#lower、upper
# str = 'i love python o'
# print(str.lower())        #将字符串全部转换为小写
# print(str.upper())          #将字符串全部转换为大写


#title
# str = 'i love python o'
# print(str.title())        #将每个单词的首字母大写


#capitlize
# str = 'i love python o'
# print(str.capitalize())        #将字符串的首字母大写


#center
# str = 'hello'
# print(str.center(15))   #将字符串的放在中间
