"""
名片管理系统V2.0
1、添加一个新的名片
2、删除一个名片
3、修改一个名片
4、查询一个名片
5、显示所有名片
6、退出系统
"""

# 1、有一个容器来存储名片   这个时候我就用list用来存储数据
card_infors = []

while True:
    # 2、获取用户输入的内容
    num = int(input('请输入操作序号'))

    # 3、根据用户输入的序号，进行相应的操作
    if num == 1:#添加名片
        # 1)用户来添加内容
        new_name = input('请输入新的名字:')
        new_qq = input('请输入新的QQ:')
        new_wechat = input('请输入微信:')
        new_addr = input('请输入地址')
        new_tel = input('请输入电话:')

        # 定义一个新的字典  用来存储 一个新的的名片
      # 方法一
       # new_infor = {}
       # new_infor['name'] = new_name
       # new_infor['qq'] = new_qq
       # new_infor['wechat'] = new_wechat
       # new_infor['addr'] = new_addr
       # new_infor['tel'] = new_tel
      # 方法二
        new_infor= {'name':new_name,'qq':new_qq,'wechat':new_wechat,'addr':new_addr,'tel':new_tel}
       # 吧这个字典 添加到列表里面 
        card_infors.append(new_infor)
       # 添加成功
       #print('添加成功，现在的全部数据是%s'%card_infors)
        for dic in card_infors:
            print('*'*20)
            for k,v in dic.items():
                print('%s:%s'%(k,v))

    elif num == 2:#删除一个名片
        name = input('请输入要删除的名片,在这里我们根据名字来删除')
        index = 0
        for dic in card_infors:
        # 如果用户输入的名字和我们当前这一次循环取出来的key为name的value值相当
            if dic['name']==name:
                del card_infors[index]
            else:
                index+=1
        # 删除操作已经执行完毕
        for dic in card_infors:
            print('姓名\n%s\tQQ\n%s\t'%(dic['name'],dic['qq'])

    elif num == 3:#修改一个名片
        name = input('请输入名字')
        for dic in card_infors:
            if dic['name'] == name:
                name2 = input('请输入你要替换的新名字')
                dic['name'] = name2
    elif num == 4:#查询一个名片
        temp = input('请输入您要查询的名片姓名')    
        for dic in card_infors:
            if temp == dic['name']:
                print('姓名%s\tqq%s\ttel%s\n'%(dic['name'],dic['qq'],dic['tel']))
                
    elif num == 5:#显示所有名片 
        for dic in card_infors:
            print('*'*20)
            for k,v in dic.items():
                print('%s:%s'%(k,v))
       
    else:
        break
        print('退出系统')






