''''''
'''
    用户创建一个User的类，包含first_name和last_name
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
if __name__ == '__main__':
    joe = User('joe','black',19,'男','186000000')
    joe.describe_user()
    joe.greet_user()
