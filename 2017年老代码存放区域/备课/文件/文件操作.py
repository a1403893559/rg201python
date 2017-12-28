#f = open('test.txt','a')
#f.write('\n你好李文浩')
#f.close()
f = open('test.txt','r')
#f.write('你好')

xx = f.readlines()
#print(xx)
for x in xx:
    print(x)
f.close()

