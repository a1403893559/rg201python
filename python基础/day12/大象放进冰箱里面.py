'''
平时大家上课都很累 为了增加学习中的欢乐气氛 我们来做个游戏
游戏的名字就叫把大象关进冰箱里 游戏很简单  就是把指定物品放进冰箱里面
我们都知道 把大象放进冰箱里面 分为三个步骤
第一步 打开冰箱
第二步 把大象放进去
第三步 关上冰箱
但是 首先你要有一头大象 所以 人为又加了第0步 准备大象
为了保证游戏的欢乐性  我们规定游戏者 在第二步把大象放进去的时候   需要有不同的动作表情
'''
# 李文浩感觉好玩 开始了游戏


class Play_Lwh():
    def __init__(self):
        ele_object = None

    # 李文浩去泰国买大象
    def buyEle(self):
        self.ele_object = '大象'
        print('准备一只大象，李文浩去泰国买了一只', self.ele_object)

    def step_one(self):
        print('打开冰箱')

    def step_two(self):
        print('蹦蹦跳跳哭着，把大象放进冰箱')

    def step_three(self):
        print('关上冰箱')


start = Play_Lwh()
start.buyEle()
start.step_one()
start.step_three()
