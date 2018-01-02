# b = []
# for x in range(0,11):
#     print(x)
#     b.append(x)
# print('b=',b)
# print('华丽分割线')

# # 列表推导式
# a = [x for x in range(0,11)]
# print(a)

# c = [x for x in range(2,15)]
# print(c)


# d = [(x,y) for x in range(1,4) for y in range(5,8)]
# print(d)

# e = []
# for x in range(1,4):
#     for y in range(5,8):
#         a = (x,y)
#         e.append(a)
# print(e)

# f = []
# for x in range(1,11):
#     # 奇数
#     if x%2 != 0:
#         f.append(x)
# print('f=',f) 

# j = [x for x in range(1,11) if x%2 != 0]
# print('j=',j)

# k = [(x,y,z) for x in range(0,3) for y in range(1,4) for z in range(5,8)]
# print(k)

# M = [1,2,3,4,5,6,6,7,7]
# L = set(M)
# print(L)

# print('华丽分割线')
# N = [22,22,22]
# N = set(N)
# print(N)

n = [[x,y,z] for x in range(1,100,3) for y in range(x+1,x+2,2) for z in range(x+2,x+3,2)]
print(n)
#L = (1,2)
#L = list(L)
#print(L)
#
p = [(x,x+1,x+2) for x in range(1,100,3)]
print(p)