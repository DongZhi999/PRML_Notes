''''''
'''
    异常
    try:
    except:
    else:
    finally:
'''
# try:
#     print(aaa) #如果这句话有错，就会捕捉到异常
# except ValueError:
#     pprint('变量未定义')  #对NameError的异常处理
# except NameError:
#     print('变量未定义')  #对NameError的异常处理

#捕获异常的具体信息
# try:
#     print(aaa) #如果这句话有错，就会捕捉到异常
# except NameError as e:
#     print(e)  #打印出NameError的异常信息，输出显示变量未定义

#包含多个异常
# try:
#     files = open('aaa.text','r',encoding='utf-8')  #如果这句话有错，就会捕捉到异常
# except (NameError,FileNotFoundError) as e:
#     print(e)  #打印出NameError的异常信息，输出显示变量未定义

#所有异常
# try:
#     print(aaa) #如果这句话有错，就会捕捉到异常
#     files = open('aaa.text','r',encoding='utf-8')  #如果这句话有错，就会捕捉到异常
# except Exception as e:
#     print(e)  #打印出NameError的异常信息，输出显示变量未定义
# except :
#     print('出错误啦')  #打印出NameError的异常信息，输出显示变量未定义

'''
    else:
        没有异常时要执行的语句
'''
# try:
#     # print(aaa) #如果这句话有错，就会捕捉到异常
#     files = open('aaa.text','r',encoding='utf-8')  #如果这句话有错，就会捕捉到异常
# except Exception as e:  #有异常时执行
#     print(e)  #打印出NameError的异常信息，输出显示变量未定义
# else:         #没有异常时执行
#     print('没什么问题')

'''
    finally:
        不管有没有异常都会执行的代码
'''
# try:
#     print('打开文件')
#     files = open('aaa.text','w',encoding='utf-8')  #如果这句话有错，就会捕捉到异常
#     try:
#         files.write('测试一下行不行')
#     except:
#         print('写入失败')
#     else:
#         print('写入成功')
#     finally:      #不管有没有异常都要执行的代码块
#         print('关闭文件')
#         files.close()
#
# except:
#     print('没什么问题')


'''
    练习
'''
try:
    num1 = int(input('请输入第一个数字：'))
    num2 = int(input('请输入第二个数字：'))
except ValueError:
    print('请分别输入两个整数')
else:
    print(num1+num2)
finally:
    print('执行完毕')