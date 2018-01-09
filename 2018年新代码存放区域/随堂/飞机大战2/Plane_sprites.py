import random
import pygame

# 游戏屏幕的大小
SCREEN_RECT = pygame.Rect(0,0,480,700)
# 敌机的定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

class GameSprite(pygame.sprite.Sprite):
    """游戏精灵的基类"""

    def __init__(self,image_name,speed = 1):

        # 调用父类的初始化方法
        super().__init__()

        # 加载图像 pygame.image.load()加载图像
        self.image = pygame.image.load(image_name)
        
        # 设置尺寸 self.image.get_rect()返回图片的宽和高
        self.rect = self.image.get_rect()

        # 记录一下速度
        self.speed = speed

    def update(self):

        # 默认在垂直方向移动
        self.rect.y += self.speed

class Backgroup(GameSprite):
    """背景精灵组"""
    def update(self):
        # 1、调用父类的方法
        super().update()

        # 判断是否移除屏幕 如果移除屏幕 将图片移动到上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵类"""
    def __init__(self):
        
        # 1 调用父类的方法，创建敌机精灵，并且指定敌机的图像
        super().__init__('/home/wengwenyu/vscodeProject/rg201python/2018年新代码存放区域/飞机大战/备课/images/enemy1.png')

        # 2 设置敌机的随机初始速度
        self.speed = random.randint(1,3)


        # 3 设置敌机的随机初始位置
        self.rect.bottom = 0
        
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)



    def update(self):

        # 1 调用父类的方法 让敌机在垂直方向运动
        super().update()

        # 2 判断是否飞出屏幕 如果是 需要将敌机从精灵组 删除
        if self.rect.y >= SCREEN_RECT.height:
            
            self.kill()

    
    def __del__(self):
        print('敌机挂掉了%s'%self.rect)


