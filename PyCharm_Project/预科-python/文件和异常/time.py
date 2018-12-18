'''
    引入time模块
'''
import time
#返回格林威治时间
# print(time.altzone)

#接收时间元组并返回一个可读的形式为“Tue Dec 11 18:07:14 2008”的24个字符的字符串
# print(time.asctime())   #返回可读形式的当前时间
# print(time.asctime((2018,12,12,12,12,12,3,340,1)))

#@@@@返回进程时间
# print(time.clock())
# print(time.clock())
# print(time.clock())

#@@@@返回当前时间的时间戳
# print(time.time())

# times = time.time()
# print(time.ctime(times))   #利用传入时间戳的形式获取当前时间

# print(time.ctime())  #获取度形式的当前时间

# print(time.gmtime())    #@@@@返回一个时间元组， 返回的是格林威治时间，存在时差
# print(time.localtime())    #@@@@返回一个时间元组， 返回的是当前时间

'''
    @@@ 时间戳转换为时间元组，将时间元组转换为时间字符
'''
# 获取当前时间戳
# times = time.time()
#
# #将时间戳转换为时间元组
# print(time.localtime(times))
# formatTime = time.localtime(times)
# #自定义读取形式的时间输出形式
# print(time.strftime('%Y-%m-%d %H:%M:%S',formatTime))


'''
    @@@ time.strptime 将时间字符串转换为时间元组
'''
# times = '2018-05-02 20:19:45'
# #转换为时间元组
# formatTime = time.strptime(times,'%Y-%m-%d %H:%M:%S')
# print(formatTime)
#
# #将时间元组转换为时间戳 mktime
# print(time.mktime(formatTime))


'''
    sleep 推迟调用线程的运行，secs指秒数
'''
# for i in range(1,2):
#     print('让子弹飞一会儿')
#     time.sleep(2)    #延时2秒
#     print('子弹在飞')
#     time.sleep(2)    #延时2秒
#     print('子弹到了')


'''
    作业
'''
# times = '2018-05-03 18:35:50'
# #将字符串转化为时间元组
# formatTime = time.strptime(times,'%Y-%m-%d %H:%M:%S')
# print(formatTime)
# #将时间元组转换为时间戳
# print(time.mktime(formatTime))

# times = '2018-05-03 18:35:50'
# # 将字符串转化为时间元组
# formatTime = time.strptime(times,'%Y-%m-%d %H:%M:%S')
# #将时间元组转换为字符串
# print(time.strftime('%Y-%m-%d %H:%M:%S',formatTime))

#获取当前时间
# now = time.time()
# #将当前时间转化为本地时间
# formatTime = time.localtime(now)
# print(time.strftime('%Y-%m-%d %H:%M:%S',formatTime))

# now = time.time()
# #获取3天前的时间戳
# threeAgo = now-60*60*24*3
# formatTime = time.localtime(threeAgo)
# print(time.strftime('%Y-%m-%d %H:%M:%S',formatTime))
