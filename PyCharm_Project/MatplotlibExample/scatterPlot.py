import numpy as np
import matplotlib.pyplot as plt

N = 1000
x = np.random.rand(N)
y = -x + np.random.rand(N)*0.5
plt.scatter(x,y,s=200,c='r',marker='*',alpha=.1)
plt.savefig('scatterTest')
#plt.savefig('D:\\python_practice\\导出的图片.png')#保存图片
plt.show()