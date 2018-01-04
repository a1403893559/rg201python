import pygame
from plane_sprites import *

pygame.init()

# 1、创建游戏主窗口
screen = pygame.display.set_mode((480,700))

# 2、创建英雄精灵组
hero = GameSprite('/home/wengwenyu/vscodeProject/rg201python/2018年新代码存放区域/images/me1.png')
# 3、精灵组 把精灵添加到精灵组
hero_group = pygame.sprite.Group(hero)

# 4、创建游戏时钟对象
clock = pygame.time.Clock()
while True:
    # 设置屏幕刷新帧率
    clock.tick(60)

    # 填充背景颜色 这个代码看不懂没关系
    screen.fill((255,255,255))

    # 让精灵组更新为止并且绘制精灵
    hero_group.update()
    hero_group.draw(screen)


    # 更新屏幕显示
    pygame.display.update()
