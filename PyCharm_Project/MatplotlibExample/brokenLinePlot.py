import  numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,10) #从-10到10生成等区间的100个数
y = x**2
y1 = 100*np.sin(x)
plt.plot(x,y)
plt.plot(x,y1,c='r',marker='+')
plt.savefig('brokenLineTest')
plt.show()