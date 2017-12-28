f = open('test.txt','r')

content = f.readline()
print('1:%s'%content)

content = f.readlines()
print('2:%s'%content)

f.close()
