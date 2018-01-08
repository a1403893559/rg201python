import pygame

# 游戏屏幕的大小
SCREEN_RECT = pygame.Rect(0,0,480,700)

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



