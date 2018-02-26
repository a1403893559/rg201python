# class 人类(object):
    
#     眼睛 = '黑色'
#     __基因 = 'X'

#     def __init__(self):
#         self.名字 = '张三'
#         self.__性取向 = '正常'

# p = 人类()
# print(p.名字)
# print(人类.眼睛)




class People(object):
    address = '福建' #类属性
    num = 0
    def __init__(self):
        self.name = '翁闻宇' #实例（对象）属性
        self.age = 20 # 实例属性
# 翁闻宇
wengwenyu = People()
wengwenyu.age = 30 # 实例属性
print(wengwenyu.age)# 正确 
print(wengwenyu.name) #通过对象调对象属性（通过实例调实例属性）
print(wengwenyu.address) # 通过实例对象调用类属性
print('-'*30)
People.num = People.num+1
# 九妹妹 漂亮的妹妹
jiumeimei = People()
jiumeimei.age = 17
jiumeimei.name = '九妹'
print(jiumeimei.age)# 正确 
People.num = People.num+1
print(jiumeimei.name) #通过对象调对象属性（通过实例调实例属性）
print(jiumeimei.address) # 通过实例对象调用类属性

print('------------------')

print(People.address) # 正确
#print(People.name) #调不到
#People.address = '上海'

print('------------------------')
print(wengwenyu.address)
print(jiumeimei.address) 

print(People.num)






