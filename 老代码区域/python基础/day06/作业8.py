# 放眼望世界：想出5个你想去旅游的地方
#创建一个列表
citys = ['土耳其','巴黎','东京','台湾','地中海','阿联酋']
# 循环遍历列表   你就理解为循环打印
for name in citys:
    print(name)

# reverse()  列表逆序 
citys.reverse()
print(citys)

# sort()  排序  正序 从小到大
citys.sort()
print(citys)
# sort(reverse=True)
citys.sort(reverse=True)
print(citys)
