def test(name):
    name = '李文浩'
    print('经过函数操作以后:',name)

name2 = '陈怀勇'
print('原本的name2',name2)
test(name2)
print('调用函数以后的name2',name2)
print('-'*30)
def demo(hero_name,wzry_list):
    wzry_list.append(hero_name)
    print('经过函数操作以后',wzry_list)

name = '阿卡丽'
list1 = []
demo(name,list1)
print('-'*20)
print('函数外面的列表',list1)
    
