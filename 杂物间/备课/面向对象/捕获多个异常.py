#try:
#    print(num)
#except IOError:
#    print('产生错误了')
#try:
#    print(num)
#except NameError:
#    print('产生错误了')
#try:
#    print('-----test--1---')
#    open('123.txt','r') # 如果123.txt文件不存在，那么会产生 IOError 异常
#    print('-----test--2---')
#    print(num)# 如果num变量没有定义，那么会产生 NameError 异常
#
#except (IOError,NameError): 
#    #如果想通过一次except捕获到多个异常可以用一个元组的方式
#
#    # errorMsg里会保存捕获到的错误信息
##    print(errorMsg)
#try:
#    print(a)
#except NameError as result:
#    print(result)
#try:
#    open('a.txt')
#except:
#    print('产生了一个异常')
#try:
#    open('a.txt')   
#except Exception as result:
#    print('捕获到了异常')
#    print('异常信息为:',result)
#try:
#    num = 100
#    print(num)
#except expression as identifier:
#    print('产生错误了:%s'%identifier)
#else:
#    print('没有异常真高兴')
import time
try:
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        # 如果在读取文件的过程中，产生了异常，那么就会捕获到
        # 比如按下了 Ctrl+c
        pass
    finally:
        f.close()
        print('关闭文件')
except:
    print('没有这个文件')