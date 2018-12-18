''''''
'''
    类定义
    class 类名（）：
        #类文档说明
        属性
        方法
'''
class person():
    '''
        这是一个人类
    '''
    country = '中国'   # 类属性 并赋值 类属性，每次实例化，都回是相同的
    # 实例属性通过构造方法来声明
    # self  不是关键字，代表的是当前对象
    def __init__(self,name,age,sex):   #构造方法
        # 构造方法不需要调用，在实例化的时候自动调用
        # print('我是构造方法，在实例化的时候调用')
        self.name = name    #通过self 创建实例属性，并且赋值
        self.age = age
        self.sex = sex

    # 创建普通方法
    def getName(self):
        print('我的名字叫%s,我来自%s!'%(self.name,person.country))  #在方法里面使用实例属性
        # 对象属性用 self.属性名 引用       类属性用 类名.属性名  引用

# 实例化对象
people01 = person('joe','19','男')   #在实例化的时候传递参数
# 这个people01 就要具有三个属性，并且可以使用

# 访问属性
# print(people01.name)    #通过  对象名.属性名    查看实例属性
# print(people01.sex)
# print(people01.age)

# 通过内置方法 访问属性
# print(getattr(people01,'name'))
# print(getattr(people01,'age'))
# print(getattr(people01,'sex'))

# 通过内置方法 检查属性是否存在
# print(hasattr(people01,'name'))  #返回 Ture

# 通过内置方法 设置属性
# setattr(people01,'name','susan') #更改实例属性值
# print(people01.name)

# 通过内置方法 删除属性
# delattr(people01,'name')  #删除实例属性值
# print(people01.name)

# 通过对象调用实例方法
# people01.getName()

'''
    内置属性
'''
# print(people01.__dict__)     # 会将实例对象的 属性和值 通过字典的形式返回
# print(people01.__doc__)     # 会将实例对象的 属性和值 通过文档的形式返回
# print(person.__name__)     # 返回类名
# print(person.__bases__)

# 新实例化一个对象
people02 = person('susan','19','女')   #在实例化的时候传递参数
people02.getName()

people01 = person('joe','19','男')   #在实例化的时候传递参数
people01.getName()


