# coding=utf-8

import numpy as np
import matplotlib
import scipy
import matplotlib.pyplot as plt

#设置legend: http://bbs.byr.cn/#!article/Python/7705
#mark样式: http://www.360doc.com/content/14/1026/02/9482_419859060.shtml

#国家 融合特征值
x1 = [10, 20, 50, 100, 150, 200, 300]
y1 = [0.615, 0.635, 0.67, 0.745, 0.87, 0.975, 0.49]

#动物
x2 = [10, 20, 50, 70, 90, 100, 120, 150]
y2 = [0.77, 0.62, 0.77, 0.86, 0.87, 0.97, 0.77, 0.47]

#人物
x3 = [10, 20, 50, 70, 90, 100, 120, 150]
y3 = [0.86, 0.86, 0.92, 0.94, 0.97, 0.97, 0.76, 0.46]

#国家
x4 = [10, 20, 50, 70, 90, 100, 120, 150]
y4 = [0.86, 0.85, 0.87, 0.88, 0.95, 1.0, 0.8, 0.49]

plt.title('Entity alignment result')
plt.xlabel('The number of class clusters')
plt.ylabel('Similar entity proportion')

plot1, = plt.plot(x1, y1, '-p', linewidth=2)
plot2, = plt.plot(x2, y2, '-*', linewidth=2)
plot3, = plt.plot(x3, y3, '-h', linewidth=2)
plot4, = plt.plot(x4, y4, '-d', linewidth=2)

plt.xlim(0, 300)
plt.ylim(0.4, 1.0)


#plot返回的不是matplotlib对象本身,而是一个列表,加个逗号之后就把matplotlib对象从列表里面提取出来
plt.legend( (plot1,plot2,plot3,plot4), ('Spot', 'Animal', 'People', 'Country'), fontsize=10)
plt.show()
