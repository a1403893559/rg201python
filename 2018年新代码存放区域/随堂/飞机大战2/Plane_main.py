# 使用pygame 我们要先导入这个包
import pygame
from Plane_sprites import *

class PlaneGame(object):
    """飞机大战主游戏"""
    def __init__(self):
        print('游戏初始化')

        # 1 创建游戏窗口 pygame.display.set_mode 创建游戏窗口 需要穿宽和高 会给我们返回一个窗口
        # .size 取宽高  .x取x轴的值   .y取y轴的值
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2 创建游戏时钟 pygame.time.Clock()会给我们返回一个时钟对象
        self.clock = pygame.time.Clock()
        # 3 调用私有方法 里面的创建精灵和精灵组
        self.__create_sprites()

    def start_game(self):
        print('开始游戏')

        while True:
            # 1、设置帧率
            self.clock.tick(60)
            # 2、事件监听
            self.__event_handler()
            # 3、碰撞检测
            self.__check_collide()
            # 4、更新精灵组
            self.__update_sprites()
            # 5、更新屏幕显示
            pygame.display.update()
    
    def __create_sprites(self):
        """创建精灵和精灵组"""
        # pygame.sprite.Group()可以创建一个精灵组
        # 1、背景精灵组
        bg1 = Backgroup('/home/wengwenyu/vscodeProject/rg201python/2018年新代码存放区域/飞机大战/备课/images/background.png')
        bg2 = Backgroup('/home/wengwenyu/vscodeProject/rg201python/2018年新代码存放区域/飞机大战/备课/images/background.png')
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1,bg2)
        # 2、敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 3、英雄精灵组
        self.hero_group = pygame.sprite.Group()

    def __event_handler(self):
        """事件监听的方法"""
        # pygame.event.get()获取监听事件的列表
        # 获取完列表以后  我写了一个for循环 循环这个列表
        for event in pygame.event.get():
            # 当列表里面有pygame.QUIT这个值的时候 说明用户点了关闭按钮
            if event.type == pygame.QUIT:
                # 调用静态私有方法
                PlaneGame.__game_over()



    def __check_collide(self):
        """碰撞检测的方法"""
        pass
    
    def __update_sprites(self):
        """更新精灵组"""
        for group in [self.back_group,self.enemy_group,self.hero_group]:
            # 更新精灵组里面所有精灵的位置
            group.update()
            # 绘制到屏幕上
            group.draw(self.screen)


    @staticmethod
    def __game_over():
        """游戏结束了"""
        print('游戏结束')
        pygame.quit()
        exit()
        pass







# 一般情况下 比如有一个场景 测试
if __name__ == "__main__":
    # 1 创建游戏对象
    game = PlaneGame()
    # 2 调用开始游戏的方法
    game.start_game()
