#open()
#write()
#read()
#close()
# w写 r读   
# 如果 有这个文件就打开  如果没有这个文件就创建
f = open('heziguo.txt','r+')
b = f.readlines()
print(b)
f.close()

