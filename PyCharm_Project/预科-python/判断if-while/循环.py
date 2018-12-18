''''''

'''
    循环：
        while 循环： 通过条件进行循环
        for:遍历一个序列
        
    跳转语句：
        break: 直接跳出循环，不管条件是否为真，都不继续循环
        continue: 跳出本次循环，直接开始下一次循环
'''

'''
    if 练习 
    利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60~89分之间用B表示，<60用C表示
'''
# score = int(input('请输入成绩：'))
# if score >= 90:
#     print('成绩为A')
# elif 60<= score <= 89:
#     print('成绩为B')
# else :
#     print('成绩为C')

'''
    for
    创建一个名为favorite_places的字典
    在这个字典中，将三个人的名字用作键，对于其中每个喜欢的人，都存储他喜欢的1~3个地方，朋友指出他们
    喜欢的一个地方（input）。遍历这个字典，并将其中每个人的名字及其喜欢的输出
'''
# 创建字典
# favorite_places = {'张三':['上海','北京','广州'],'李四':['九寨沟','张家界','鼓浪屿']}
# name = input('请输入你的名字：')

# for k in favorite_places:
#     # print(k)
#     if name == k:
#         print(favorite_places[name])
# print(favorite_places.items())  #遍历整个字典，获取到字典的key 和value 组成的元组
# for k,v in favorite_places.items():
#     print(k,v)


'''
    用for 循环打印99乘法表
    while 循环
    1x1=1
    1x2=2  2x2=4
    1x3=3  2x3=6  3x3=9
'''
# num = [1,2,3,4,5,6,7,8,9]
# for i in range(1,10) :
#     for j in range(1,i+1):
#         print('%d x %d = %d'%(j,i,(j*i)),end='      ')
#     print('\n')  #默认以换行结尾，再加换行符
    # for j in (1,i)

# i = 1
# while i < 10:
#     # print(i)
#     j = 1
#     while j <= i:
#         print('%d x %d = %d'%(i,j,(i*j)),end='      ')
#         j +=1
#     i += 1
#     print()  #默认换行


""""
    1~100的和
    1+2+3+...+100=？
"""
# sum = 0
# for i in range(1,101):
#     sum += i
#     print(sum)
# print()
# print(sum)


'''
    从键盘输入一个字符串，将小写字母全部转换成大写字母，
    将字符串以列表的形式输出（如果字符串包含整数，转为整形）？
'''
# str1 = input('请输入一个字符串：')
# list1 = []   #建立一个空列表
# for i in str1:    #遍历输入的字符串
#     if i.isdecimal() == True:   #判断当前字符是否是数字
#         list1.append(int(i))     #将数字转换为int型，然后插入列表中
#     else:
#         list1.append(i.upper())   #将当前字符转换为大写，然后追加到列表中
# print(list1)


'''
    随机输入8位以内的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''
# num = input('请输入一个8位数以内的正整数：')
# if len(num) <= 8:
#     print('这个数是%d位数'%len(num))
#     print(num[::-1])
# else:
#     print('输入有误')


'''
    一个球从n米（自己输入）高度自由落下，每次落地后反跳回原高度的一半；
    再落回，求他第10次下落时，共经过多少米？第10次反弹多高？
'''
# h = float(input('请输入球第1次落下的高度：'))
# i = 1
# sum = h
# while i < 10:
#     sum += float(h/i)
#     i += 1
#     print('下落过程共经过%f米'%sum)
# print('下落过程共经过%f米'%sum)
# h = float(h/(2*i))
# print('第10次反弹高度为：%f米'%h)


# n = float(input('请输入球第1次落下的高度：'))
# m = 0
# for i in range(1,4):
#     if i == 1:
#         m += n
#     else:
#         n/=2
#         m +=n*2
# print('下落过程中共经过%f米'%m)


'''
 输入一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数。
'''
# str1 = input('请输入字符：')
# zf = 0
# num = 0
# space = 0
# other = 0
# for i in str1:
#     if i.isalpha():
#         zf +=1
#     elif i.isdigit():
#         num +=1
#     elif i.isspace():
#         space +=1
#     else:
#         other +=1
# print('当前字母的个数是：%d,当前数字的个数是：%d，当前空格个数是：%d，其他字符的个数是：%d'%(zf,num,space,other))


'''
    找出名字中字符长度大于4的名字，组成列表打印出来。
    过滤掉长度大于5的字符串列表，并将剩下的转换成大写字母
'''
# names = ['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe',
        # 'Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']
# name = []
# for i in names:
#     if len(i) > 4:
#         name.append(i)
# print(name)

# name = [i.upper() for i in names if len(i) > 4 ]     #依次为变量、for循环、if判断条件；生产一个列表
# print(name)


'''
    求M、N中矩阵对应元素的和，元素的乘积
    M = [[1,2,3],[4,5,6],[7,8,9]]
    N = [[2,2,2],[3,3,3],[4,4,4]]
'''
# m = [[1,2,3],[4,5,6],[7,8,9]]
# n = [[2,2,2],[3,3,3],[4,4,4]]

# for i in range(3):
#     for j in range(3):
#         print(m[i][j]+n[i][j])
# num = [m[i][j]+n[i][j] for i in range(3) for j in range(3)]
# print(num)
# num = [m[i][j]*n[i][j] for i in range(3) for j in range(3)]
# print(num)


'''
    列表推导式
'''
# list03 = []
# for i in range(3,10):
#     if i % 2 == 0:
#         list03.append(i)
# print(list03)

# list03 = [i for i in range(3,10) if i % 2 ==0]
# print(list03)


'''
    嵌套列表推导
'''
# names = [['Tom','Billy','Jefferson','Andrew','Wesley','Joe'],
#          ['Alice','Jill','Ana','Wendy','Jennifer','Eva']]
# print(names[0][0])
# list04 = []
# for i in range(0,2):
#     for n in names[i]:
#         list04.append(n)    #将元素添加到列表
# print(list04)

# list04 = [n for i in range(0,2) for n in names[i]]
# print(list04)


'''
    打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，
    其各位数字立方和等于该数本身。
'''
# 153 = 1**3 + 5**3 + 3**3
# 遍历 100--1000
# 获取每一位数的百位，十位，各位
# 分别**3 然后相加，判断与当前数是否相等
# for i in range(100,1000):
#     a = i // 100      #取百位
    # a = int(i/100)   #取百位
    # b = i%100//10      #取十位，先取余数，再取模
    # b = int((i-a*100)/10)   #取十位
    # c = i%100%10      #取个位，取余数，再取余数
    # c = int(i-a*100-b*10)    #取个位
    # if a**3 + b**3 + c**3 == i:
    #     print(i)


'''
    打印菱形
'''
# i = '*'
# m = '***'
# list01 = ['*','***','*****','*******']
# print(i.center(7))
# print(m.center(7))
# for i in range(1,5,1):
#     print(list01[i-1].center(7))
#     if i == 4:
#         for i in range(4,0,-1):     #利用range的步长
#                 print(list01[i-1].center(7))


'''
    一个5位数，判断它是不是回文数，即12321是回文数
'''
# list01 = input('请输入一个5位数：')
# if len(list01) == 5:
#         if list01[0] == list01[4] and list01[1] == list01[3] :
#             print('该数是回文数.')
#         else:
#             print('该数不是回文数.')
# else:
#     print('输入位数不正确，请从新输入5位数！')

#另外一种方法
# list01 = input('请输入一个数：')
# if list01 == list01[::-1]:
#     print('该数是回文数.')
# else:
#     print('该数不是回文数.')


'''
    求一个3*3的矩阵的对角元素之和
'''
# m = [[1,2,3],[4,5,6],[7,8,9]]
# x = 0
# y = 0
# for i in range(0,3):
#     x +=m[i][i]
# print('主对角元素的和为：%d'%x)
# for j in range(0,3):
#     y +=m[j][2-j]
# print('副对角元素的和为：%d'%y)


'''
    题目：有4个数字：1、2、3、4 能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
# for x in range(1,5):
#     for y in range(1,5):
#             for z in range(1,5):
#                 if x != y and x != z and y != z :    #判断三个数字互不相同
#                     print(x*100+y*10+z)
# num = [x*100+y*10+z  for x in range(1,5)  for y in range(1,5) for z in range(1,5) if x != y and x != z and y != z]
# print(num)      #打印出列表的数字


'''
    设一组账号和密码不少于两个
    通过输入账号和密码，如果输入正确则显示登录成功
    若账号或者密码错误则显示登录失败，最多可以输入3次
'''
# user = {'张三':'123456','李四':'654321'}
# name = input('请输入账号：')
# pwd = input('请输入密码：')
# for i in range(3):
#     if name in user:
#         if pwd == user[name]:
#             print('登录成功！')
#             break
#         else:
#             if i == 2:
#                 print('你的账号已冻结！')
#             print('你的密码有误！')
#     else:
#         print('你的账号有误！')


'''
    求阶乘，用while 和 for 分别实现
'''
# num = int(input('请输入一个数：'))
# x = 1
# for i in range(1,num+1):
#     x  *= i
# print('该数的阶乘为：%d'%x)

# num = int(input('请输入一个数：'))
# x = 1
# y = 1
# while x <= num:
#     y *= x
#     x += 1
# print('该数的阶乘为：%d'%y)


'''
    冒泡排序
'''
list01 = [2,6,4,9,3,10]
for i in range(len(list01)):
    for j in range(1,len(list01)):
        if list01[j] > list01[j-1]:
            list01[j],list01[j-1] = list01[j-1],list01[j]
    print(list01)
    print('_'*20)
print(list01)

