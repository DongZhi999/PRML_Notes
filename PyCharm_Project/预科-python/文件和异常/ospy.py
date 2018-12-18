
'''
    文件与文件夹的操作
'''
import os
# 获取当前路径
print(os.getcwd())  #获取绝对路径

# 列出当前或指定目录下的文件和文件夹
# print(os.listdir())    #打印出当前文件夹下的文件

#判断是否是一个文件夹
# print(os.path.isfile('.\\demo.text'))  #返回True 说明是一个文件

# 判断文件是否存在
# print(os.path.exists('.\\demo.text'))  #返回True 说明文件存在

#重命名文件
# os.rename('demo.text','demo1.text')

#删除文件
# os.remove('demo1.text')

#将文件和路径区分出来，并分别打印出来
# print(os.path.split('E:/DongzhiProjects/PyCharm_Project/预科-python/文件和异常/ospy.py'))

#创建文件夹
# os.mkdir('study')

#删除文件夹
# os.rmdir('study')
