# 求1-100之间的素数

L = []
for i in range(2,101):
    mark = 0
    for j in range(2,(i-1)):
        if i%j == 0:
            
            mark = 1
    if mark == 0:
        L.append(i)

print(L)
     
        