import numpy as np
import  matplotlib.pyplot as plt
import matplotlib

'''N = 5
y = [20,10,30,25,15]
index = np.arange(N)

pl = plt.bar(index,height=y,color='red',width=0.5,orientation = 'horizootal')
plt.show()'''


# 设置中文字体和负号正常显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

label_list = ['2014', '2015', '2016', '2017']    # 横坐标刻度显示值
num_list1 = [20, 30, 15, 35]      # 纵坐标值1
num_list2 = [15, 30, 40, 20]      # 纵坐标值2
x = range(len(num_list1))
"""
绘制条形图
left:长条形中点横坐标
height:长条形高度
width:长条形宽度，默认值0.8
label:为后面设置legend准备
"""
rects1 = plt.bar(left=x, height=num_list1, width=0.4, alpha=0.8, color='red', label="一部门")
rects2 = plt.bar(left=[i + 0.4 for i in x], height=num_list2, width=0.4, color='green', label="二部门")
plt.ylim(0, 50)     # y轴取值范围
plt.ylabel("数量")
"""
设置x轴刻度显示值
参数一：中点坐标
参数二：显示值
"""
plt.xticks([index + 0.2 for index in x], label_list)
plt.xlabel("年份")
plt.title("某某公司")
plt.legend()     # 设置题注
# 编辑文本
for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
plt.savefig('barChartTest1')
plt.show()


price = [39.5, 39.9, 45.4, 38.9, 33.34]
"""
绘制水平条形图方法barh
参数一：y轴
参数二：x轴
"""
plt.barh(range(5), price, height=0.7, color='steelblue', alpha=0.8)      # 从下往上画
plt.yticks(range(5), ['亚马逊', '当当网', '中国图书网', '京东', '天猫'])
plt.xlim(30,47)
plt.xlabel("价格")
plt.title("不同平台图书价格")
for x, y in enumerate(price):
    plt.text(y + 0.2, x - 0.1, '%s' % y)
plt.savefig('barChartTest2')
plt.show()


label_list = ['2014', '2015', '2016', '2017']
num_list1 = [20, 30, 15, 35]
num_list2 = [15, 30, 40, 20]
x = range(len(num_list1))
rects1 = plt.bar(left=x, height=num_list1, width=0.45, alpha=0.8, color='red', label="一部门")
rects2 = plt.bar(left=x, height=num_list2, width=0.45, color='green', label="二部门", bottom=num_list1)
plt.ylim(0, 80)
plt.ylabel("数量")
plt.xticks(x, label_list)
plt.xlabel("年份")
plt.title("某某公司")
plt.legend()  #设置主题
plt.savefig('barChartTest3')
plt.show()