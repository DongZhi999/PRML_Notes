''''''
'''
   类方法，静态方法 
'''
class person():
    '''
        这是一个人类
    '''
    country = '中国'   # 类属性 并赋值 类属性，每次实例化，都回是相同的 类属性引用用类名
    # 实例属性通过构造方法来声明
    # self  不是关键字，代表的是当前对象
    def __init__(self,name,age,sex,address):   #构造方法
        # 构造方法不需要调用，在实例化的时候自动调用
        # print('我是构造方法，在实例化的时候调用')
        self.name = name    #通过self 创建实例属性，并且赋值     实例属性调用 用self
        self.age = age
        self.sex = sex
        self.__address = address   #下划线开头的属性是私有属性  没有关键字修饰

    # 创建普通方法
    def getName(self):
        # 私有属性在类里面使用正常
        print('我的名字叫%s,我来自%s,我住在%s!'%(self.name,person.country,self.__address))  #在方法里面使用实例属性
        # 对象属性用 self.属性名 引用       类属性用 类名.属性名  引用

    #  创建一个静态方法
    @staticmethod
    def getA():     #静态方法里面不需要传实例
        #静态方法不能访问实例属性
        #静态方法只能访问类属性
        print('我的名字叫%s'%person.country)  #在方法里面使用类属性

    # 创建一个类方法
    @classmethod
    def getB(cls):   #class 也不是关键字
        #类方法不能访问实例属性
        #
        print('我的名字叫%s'%cls.country)  #在类方法里面使用cls调用类属性

# 实例化对象
people01 = person('joe','19','男','上海')   #在实例化的时候传递参数
people01.getName()

#通过对象来调用静态方法
people01.getA()

#通过对象来调用类方法
people01.getB()

#通过类名来调用静态方法
person.getA()

#通过类名来调用类方法
person.getB()
'''
类方法和静态方法，推荐使用类名的形式进行调用
'''
