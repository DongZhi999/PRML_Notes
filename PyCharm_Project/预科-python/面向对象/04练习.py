''''''
'''
    银行大玩家
'''
class Bank():
    # 一个银行的类属性
    __Users = {}

    #每个对象都拥有
    def __init__(self,CardId,pwd,name,balance):
        if CardId not in Bank.__Users:
            Bank.__Users[CardId]  = {'pwd':pwd,'Username':name,'Balance':balance}
            self.__CardId = CardId
            self.__pwd = pwd
            self.__name = name
            self.__balance = balance

    #查看本银行的开户总数
    @classmethod
    def nums(cls):
        print('当前用户数是：%d'%(len(cls.__Users)))

    #查看用户的个人信息
    @classmethod
    def get_Users(cls):
        for key ,val in cls.__Users.items():
            print('卡号：%s\n用户名：%s\n密码：%d\n余额：%d'%(key,val['Username'],val['pwd'],val['Balance']))

    #验证方法
    @staticmethod
    def check_User(CardId,pwd):
        if (CardId in Bank.__Users) and (pwd == Bank.__Users[CardId]['pwd']):
            return True
        else:
            return False

    #验证金额
    @staticmethod
    def check_money(money):
        if isinstance(money,int):     #验证是否是整型
            return True
        else:
            return False

    # 取钱（需要卡号和密码验证）
    def q_money(self,CardId,pwd,money):
        if Bank.check_User(CardId,pwd):
            #开始取钱
            if Bank.check_money(money):
                if Bank.__Users[CardId]['Balance'] >= money:
                    Bank.__Users[CardId]['Balance'] -= money
                    print('当前卡号%s,当前取款金额%d,当前余额%d'%(CardId,money,Bank.__Users[CardId]['Balance']))
                else:
                    print('余额不足')
            else:
                print('您输入的金额有误')
        else:
            print('卡号或者密码有误')

    #存钱
    def c_money(self,CardId,pwd,money):
        if Bank.check_User(CardId,pwd):
            #开始存钱
            if Bank.check_money(money):
                Bank.__Users[CardId]['Balance'] += money
                print('当前卡号%s,当前存款金额%d,当前余额%d'%(CardId,money,Bank.__Users[CardId]['Balance']))
            else:
                print('您输入的金额有误')
        else:
            print('卡号或者密码有误')

    # 查看个人详细信息（需要卡号和密码验证）
    def getInfo(self,CardId,pwd):
        if Bank.check_User(CardId,pwd):
            print('当前卡号%s,当前余额%d'%(CardId,Bank.__Users[CardId]['Balance']))
        else:
            print('卡号或者密码有误')

joe = Bank('1001',111111,'joe',100)
Bank.nums()
print('_'*50)
Bank.get_Users()
print('_'*50)
joe.c_money('1001',111111,100)
print('_'*50)
joe.q_money('1001',111111,200)
print('_'*50)
joe.getInfo('1001',111111)
