import pygame
# 创建游戏主窗口
screen = pygame.display.set_mode((480,700))

# 绘制背景图像
bg = pygame.image.load("/home/wengwenyu/vscodeProject/rg201python/2018年新代码存放区域/images/background.png")
# 绘制英雄图像
hero = pygame.image.load("/home/wengwenyu/vscodeProject/rg201python/2018年新代码存放区域/images/me1.png")

# 绘制在屏幕上
screen.blit(bg,(0,0))
screen.blit(hero,(200,500))


pygame.display.update()

while True:
    pass