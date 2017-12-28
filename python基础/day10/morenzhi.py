'''
设计一个带有默认值参数的函数
'''
def test(hero_name,hero_type='法师'):
    print('英雄的名字是',hero_name)
    print('英雄的类型',hero_type)
    #return (hero_name,hero_type)
    #return [hero_name,hero_type]
    #return hero_name
    return 2#可选项   你可以 根据你的需要 你的需求   去返回内容  当然 你也可以布返回如何内容
print('-'*20)
test('1','2')

