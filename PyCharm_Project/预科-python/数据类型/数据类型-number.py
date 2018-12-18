# int 类型
""""
    int类型
"""
# a = 1
# print(type(a))  #type是python中用来查看数据类型的函数
"""
    bool类型
    对true 不为零  错false
"""
# a = True
# print(type(a))
"""
    字符串
    单引号或者双引号
"""
# a = '刘德华'
# print(type(a))
# a = "刘德华"
# print(type(a))
# name = "黎明"
# print(type(a))

# num1 = '1'
# num2 = 'True'  # 带引号的都是字符串，不管是单引号还是双引号
# print(type(num1))
# print(type(num2))

# str1 = '"nihao"'  #双引号成了字符串本身
# print(str1)

# str1 = 'aaa\'bbb'   #反斜杠转义用的，最外面的单引号是一对
# print(str1)

# str = 'abcdefg'  #从0开始，位置下标
# print(str)
# print(str[2:5])   #字符串的截取
# print(str[-1])    #-1是最后一位，-2是倒数第二位
# print(str[2:])    #从三位到最后
# print(str[:4])    #第0位开始到第三位，注意：包头不包位

# print(str[1:5:2])   #第1位开始到底4位，步长为2
# print(str[5:1:-2])   #第5位开始到底2位，步长为-2，反着截取

'''
    加号运算符：+
'''
# num1 = 10
# num2 = 3
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)
# print(num1%num2)    #取余数
# print(num1//num2)   #取模
# print(num1**num2)   #幂次运算

'''
    赋值运算符
'''
# str = 'a'       #等号赋值
# num = 1
# num += 1
# num -= 1
# num *= 2
# num /= 2
# num **= 2
# print(num)

'''
    比较运算符
'''
# a = 10
# b = 5
# print(a == b)
# print(a != b)
# print(a > b)
# print(a > b)


'''
    逻辑运算符
'''
# a = 10
# b = 5
# print(a>b and a<b)   #逻辑与，两个为真，则是真，否则为假
# print(a>b or a<b)   #逻辑或，两个为假，则是假，否则为真
# print(not a>b)      #逻辑取反


# str = ''     #空字符串返回bool false
# str = []     #空的列表 返回bool false
# str = ()     #空的元组 返回bool false
# str = {}     #空的字典返回bool false
# num = 0      #0 返回bool false
# print(bool(num))


'''
    位运算符
'''
# a = 4   #转换成二进制0100
# b = 2   #转换成二进制0010
# print(a & b)  # & 按位逐次取与
# print(a | b)  # | 按位逐次取或
# print(a ^ b)  # ^ 按位逐次取异或
# print(~a )  # ~ 按位逐次取反，也就是直接取负数再减1


