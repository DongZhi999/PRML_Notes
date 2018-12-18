''''''
'''
    继承
'''
# class Animal():
#     def __init__(self,name,food):
#         self.name = name
#         self.food = food
#
#     def eat(self):
#         print('%s爱吃%s'%(self.name,self.food))
#
# # 声明子类，继承animal
# class Dog(Animal):
#     #子类自己的属性
#     def __init__(self,name,food,drink):
#         #加载父类构造方法
#         # Animal.__init__(self,name,food)    # 通过super 进行继承
#         super(Dog,self).__init__(name,food)   #另外一种继承父类
#         self.drink = drink
#     # 子类自己的方法
#     def drinks(self):
#         print('%s爱喝%s'%(self.name,self.drink))
#
# class Cat(Animal):
#     #子类自己的属性
#     def __init__(self,name,food,drink):
#         #加载父类构造方法
#         # Animal.__init__(self,name,food)    # 通过super 进行继承
#         super(Cat,self).__init__(name,food)   #另外一种继承父类
#         self.drink = drink
#     # 子类自己的方法
#     def drinks(self):
#         print('%s爱喝%s'%(self.name,self.drink))
#
# dog1 = Dog('金毛','骨头','可乐')
# dog1.eat()
# dog1.drinks()
#
# cat1 = Cat('波斯猫','秋刀鱼','雪碧')
# cat1.eat()
# cat1.drinks()


'''
    多继承
'''
# class A():
#     def a(self):
#         print('我是A里面的a方法')
#
# class B():
#     def b(self):
#         print('我是B里面的b方法')
#
# class C():
#     def c(self):
#         print('我是C里面的c方法')
#
# class D(A,B,C):
#     def d(self):
#         print('我是D里面的d方法')
#
# dd = D()
# dd.d()  #调用自己的方法
# dd.b()  #调用父类的方法
# dd.c()
# dd.a()

'''
    类属性
    实例属性
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

    #外部要修改私有属性，预留一个接口去访问或者修改私有属性  这是私有属性的正确打开方式
    def getAddre(self,pwd):
        if pwd == '123':
            return self.__address
        else:
            return '权限不够'

# 实例化对象
people01 = person('joe','19','男','上海')   #在实例化的时候传递参数
people01.getName()
print(people01.getAddre())
# 通过对象名，属性名访问私有属性
# print(people01.__address)   #外部无法使用这种方式访问

#强制访问 实例化对象名._类名__属性名  不赞成这样使用
# print(people01._person__address)

# 看上去好像改了，其实没有   你给当前对象声明了属性  也不要这样操作
# people01._person__address = '北京'
# print(people01._person__address)
