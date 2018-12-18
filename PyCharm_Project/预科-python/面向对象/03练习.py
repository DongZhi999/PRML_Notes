class hero():
    # 定义属性  用构造方法定义
    def __init__(self,name,category,skill,output=1000,score = 0):
        self.name = name
        self.category = category
        self.skill = skill
        self.output = output
        self.score = score

    # 战斗场景1 偷红BUFF
    def red_buff(self):
        self.output -= 300
        print('%s%s到对面野区偷红BUFF,消耗血量300'%(self.category,self.name))

    # 战斗场景2 solo战斗
    def solo(self):
        self.output -= 500
        if self.output < 0:
            print('%s%s,送了一个人头，血染王者峡谷'%(self.category,self.name))
        else:
            if self.score == 0:
                self.score += 1
                print('%s%s solo战斗拿到一血，消耗血量500'%(self.category,self.name))
            else:
                self.score += 1
                print('%s%s solo战斗收割1人头，消耗血量500'%(self.category,self.name))

    # 场景3 加血
    def add_xue(self):
        self.output += 200
        print('奶妈及时奶了一口，加血200')

    # 查看英雄详细信息
    def getInfo(self):
        if self.output <= 0:
            print('%s%s,正在复活，拿到%d个人头'%(self.category,self.name,self.score))
        else:
            print("%s%s超神啦！血量还有%d,拿到%d个人头"%(self.category,self.name,self.output,self.score))

#实例化对象
kai = hero("凯","战士",'疾刃风暴')

#操作
kai.red_buff()
kai.getInfo()
kai.solo()
kai.getInfo()
kai.add_xue()
kai.getInfo()
kai.solo()
kai.getInfo()
