"""

    1. 定义布尔型变量 has_ticket 表示是
        2. 定义整型变量 knife_length 表示刀的长度，单位：厘米
            3. 首先检查是否有车票，如果有，才允许进行 安检
                4. 安检时，需要检查刀的长度，判断是否超过 20 厘米

                        * 如果超过 20 厘米，提示刀的长度，不允许上车
                                * 如果不超过 20 厘米，安检通过
                                    5. 如果没有车票，不允许进门


"""
has_ticket =int(input("请输入是有车票"))
if has_ticket==True:#表示有车票
    print("可以进入安检程序")
    hnife_length = float(input("请输入刀的长度"))
    if hnife_length >= 20:
        print("不允许上车")
    else:
        print("可以上车")
else:
    print("请去买票")


