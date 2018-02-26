import sys
import pygame
from Plane_sprites import *

class PlaneGame(object):
    """飞机大战主游戏类"""

    def __init__(self):
        """初始化游戏"""
        # 1 窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3 背景 英雄  敌机 这些精灵
        self.__create_sprites()

    def start_game(self):
        """开始游戏"""
        print('开始游戏')

        while True:
            # 1 设置帧率
            self.clock.tick(60)
            # 2 事件监听
            self.__even_handler()
            # 3 碰撞检测
            self.__check_collide()
            # 4 更新精灵和精灵组
            self.__update_sprites()
            # 5 屏幕显示
            pygame.display.update()
    
    def __even_handler(self):
        """监听事件"""
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                PlaneGame.__game_over()


    
    @staticmethod
    def __game_over():
        pygame.quit()
        sys.exit()

    def __check_collide(self):
        """碰撞检测"""
        pass
    
    def __update_sprites(self):
        """更新精灵和精灵组"""
        for group in [self.bg_group,self.dd_group,self.yy_group]:
            group.update()
            group.draw(self.screen)

    def __create_sprites(self):
        """创建精灵用"""
        
        # 1 背景组
        bg1 = Background
        self.bg_group = pygame.sprite.Group() 
        # 2 敌机组
        self.dd_group = pygame.sprite.Group()
        # 3 英雄组
        self.yy_group = pygame.sprite.Group()

if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 开始游戏
    game.start_game()

