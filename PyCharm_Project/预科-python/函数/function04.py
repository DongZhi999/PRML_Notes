''''''
'''
    变量的作用域
'''
# 局部变量：声明在函数内部的变量是局部变量
# def test1():
#     a = 1
#     print(a)
#     print(id(a))
# def test2():
#     print(a)     #无法使用test1() 中的局部变量
#     print(id(a))
#
# test1()
# a = 1
# test2()
# # print(a)         #局部变量的作用只在于函数中，外部无法使用


'''
    修改全局变量
'''
# def test1():
#     a = 1
#     print(a)
#     print(id(a))
# def test2():
#     a = 2
#     print(a)     #无法使用test1() 中的局部变量
#     print(id(a))
# a = 1
# test1()
# test2()
# print(a)         #局部变量的作用只在于函数中，外部无法使用
# print(id(a))


'''
    练习ATM机
'''
# 登录验证
def login(password):
    pwd = '888888'
    if password == pwd:
        return True
    else:
        return False
# 金额验证
def checkMoney(money):
    if money.isdigit():
        if int(money)%100 == 0 and 0<= money <=1000:
            return money
        else:
            return False
    else:
        return False
def main():
    # 1. 登录验证
    for i in range(3):   #最多输入3次
        password = input('请输入密码：')
        if login(password):
             print('登录成功')
            # 2. 金额验证
             while True:
                 money = input("请输入金额：")
                 money = checkMoney(money)
                 if money:delattr()
                 else:
                     print('你输入的金额有误，请从新输入！')
        else:
            print('密码有误')

