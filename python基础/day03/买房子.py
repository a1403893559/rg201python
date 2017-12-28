"""
买房子：500万能够买一环的房子，400能够买2环，如果300万能够买3环的房子，如果有200能够买四环的房子，如果小于200万，我只能睡大家
"""
money = int(input("请输入存款金额"))
if money>= 500:
    print("可以购买一环的房子")
elif money>=400:
    print("可以购买二环的房子")
elif money>=300:
    print("可以购买三环的房子")
elif money>=200:
    print("可以购买四环的房子")
else:
    print("睡大街")
