import random # 系统的模块
import pygame # 第三方模块




# 定义一个常量
SCREEN_RECT = pygame.Rect(0,0,480,700)
# 定义一个事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1



class GameSprite(pygame.sprite.Sprite):
    """精灵基类"""
    def __init__(self,image_name,speed=1):
        # 1、调用父类的方法
        super().__init__()

        # 加载图像
        self.image = pygame.image.load(image_name)

        # 设置尺寸
        self.rect = self.image.get_rect()

        # 记录速度
        self.speed = speed

    def update(self):

        # 默认情况下在垂直方向上移动
        self.rect.y += self.speed
        

class Backgroup(GameSprite):
    """游戏背景精灵"""

    def update(self):

        # 先调用父类的方法
        super().update()

        # 2、 判断是否移除屏幕 如果移出屏幕 将图片设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    """敌机精灵类"""

    def __init__(self):

        # 1 调用父类的方法
        super().__init__('/home/wengwenyu/vscodeProject/rg201python/2018年新代码存放区域/飞机大战/备课/images/enemy1.png')
        
        # 2 设置敌机的随机初始速度
        self.speed = random.randint(1,3)

        # 3 设置敌机初始为止
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):

        # 1 调用父类方法
        super().update()

        # 判断飞机是否飞出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):

        super().__init__('/home/wengwenyu/vscodeProject/rg201python/2018年新代码存放区域/飞机大战/备课/images/me1.png',0)


        # 设置初始为止
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        self.bullets = pygame.sprite.Group()
       

    def update(self):

        # 飞机水平移动
        self.rect.x += self.speed

        # 判断屏幕边界
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print('发射子弹...')
        for i in (0,1,2):
            # 1、创建子弹精灵
            bullet = Bullet()
            # 2 设置精灵的位置
            bullet.rect.bottom = self.rect.y - 20
            bullet.rect.centerx = self.rect.centerx
            
            # 3 创建子弹的精灵组
            self.bullets.add(bullet)

       

class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):

        super().__init__('/home/wengwenyu/vscodeProject/rg201python/2018年新代码存放区域/飞机大战/备课/images/bullet1.png',-2)

    def update(self):

        super().update()

        # 判断是否超出屏幕 如果是  从精灵组删除
        if self.rect.bottom < 0:
            self.kill()
        
    def __del__(self):
        print('子弹被销毁....')
