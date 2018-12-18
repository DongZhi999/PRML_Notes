''''''
'''
    编辑一个文件，写几句话
'''
# for i in range(3):
#     if i == 0:
#         with open('learning_python.text','r',encoding='utf-8') as files:
#             content = files.read()
#             print('one')
#             print(content)
#     if i == 1:
#         with open('learning_python.text','r',encoding='utf-8') as files:
#             content = files.read()
#             print('two')
#             print(content)
#     if i == 2:
#         with open('learning_python.text','r',encoding='utf-8') as files:
#             content = files.readlines()
#             print('three')
#             print(content)


'''
    
'''
# 写入内容，并读取新的内容
# file1 = open('learning_python.text','r',encoding='utf-8')
# content1 = file1.read()
# print(content1)
# file1.close()
#
# file2 = open('learning_python.text','w+',encoding='utf-8')
# file2.write(content1.replace('Python','c'))  #利用replace() 去替换内容
# file2.seek(0)    #重置指针到开头
# content2 = file2.read()  #读取所有的内容
# print(content2)
# file2.close()


'''
    访客
'''
while True:
    name = input('请输入你的姓名：')
    if name == 'n':
        break;
    with open('guest.text','a+',encoding='utf-8') as files:
        files.write(name)
        files.write('\n')
        files.seek(0)
        content = files.read()
    print(content)
