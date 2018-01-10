import pygame
# 创建游戏主窗口
screen = pygame.display.set_mode((480,700))

# 绘制背景图像
<<<<<<< HEAD
bg = pygame.image.load("C:\Users\wengw\Documents\VSCodeProject\2018年新代码存放区域\images\background.png")
# 绘制英雄图像
hero = pygame.image.load("C:\Users\wengw\Documents\VSCodeProject\2018年新代码存放区域\images\background.png")
=======
bg = pygame.image.load("/home/wengwenyu/vscodeProject/rg201python/2018年新代码存放区域/images/background.png")
# 绘制英雄图像
hero = pygame.image.load("/home/wengwenyu/vscodeProject/rg201python/2018年新代码存放区域/images/me1.png")
>>>>>>> 0d494bbb28d2c74140cefdcac7e5e26bfda9fe1d

# 绘制在屏幕上
screen.blit(bg,(0,0))
screen.blit(hero,(200,500))


pygame.display.update()

while True:
    pass