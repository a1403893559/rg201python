#打开一个已经存在的文件
f = open('test2.txt','r')
str = f.read(5)
print('读取的数据是:',str)


#查找当前的位置
position = f.tell()
print('当前文件位置:',position)


