# 求100-200之间的素数
L = []
for i in range(100,201):
    mark = 0
    for j in range(2,i):
        if i%j == 0:
            mark = 1
            break
    if mark == 0:
        L.append(i)

print(L)
        





# 求1-100之间的素数

# L = []
# for i in range(2,101):
#     mark = 0
#     for j in range(2,i):
#         if i%j == 0:
#             mark = 1
#     if mark == 0:
#         L.append(i)

# print(L)





        