import pygame

class GameSprite(pygame.sprite.Sprite):
    
    def __init__(self,image_name,speed=1):
        # 1、调用父类方法
        super().__init__()
        # 2、加载图像
        self.image = pygame.image.load(image_name)
        # 3、设置尺寸
        self.rect = self.image.get_rect()
        # 4、记录速度
        self.speed = speed
    
    def update(self,*args):
        # 默认在垂直方向移动
        self.rect.y += self.speed

