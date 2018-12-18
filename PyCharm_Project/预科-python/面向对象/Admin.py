''''''
'''
    管理员是一个特殊的用户，编写一个名为Admin的类，
    让他继承你完成User练习
'''
class User():
    '''
        用户类
    '''
    def __init__(self,first_name,last_name,age,sex,phone):
        # 初始化实例属性
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.phone = phone
    # 查看用户信息
    def describe_user(self):
        print('大家好我叫%s %s,我今年%d岁，我的电话是%s'%(self.first_name,self.last_name,self.age,self.phone))
    #个性化问候
    def greet_user(self):
        print('尊敬的%s,恭喜你中了500万!'%self.first_name)

# from User import User
class Admin(User):
    privileges = ['can add post','can delete post','can ban user']
    def __init__(self,first_name,last_name,age,sex,phone,login_attempts=0):
        super(Admin,self).__init__(first_name,last_name,age,sex,phone)   # login_attempts=0

    def show_privileges(self):
        print('管理员：%s%s,具有以下权限。'%(self.first_name,self.last_name))
        for i in Admin.privileges:
            print(i)

admin1 = Admin('su','san','18','女','1586456')
admin1.show_privileges()
