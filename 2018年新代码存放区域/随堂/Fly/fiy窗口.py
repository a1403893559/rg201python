import pygame
# 开始
pygame.init()
# display (窗口) 类游戏代码
# set_mode() 方法 初始化我们的显示窗口
# update() 方法 刷新我们的屏幕
screen = pygame.display.set_mode((480,700))
# image.load
# 步骤1 加载图片数据
bg = pygame.image.load('/home/wengwenyu/vscodeProject/rg201python/2018年新代码存放区域/images/background.png')
# 步骤2 绘制图片数据
screen.blit(bg,(0,0))
# 步骤3 更新显示
pygame.display.update()

# 步骤1 加载图片数据
hero_fly = pygame.image.load('/home/wengwenyu/vscodeProject/rg201python/2018年新代码存放区域/images/me1.png') 
# 步骤2 绘制到屏幕上
screen.blit(hero_fly, (100,500))
# 步骤3 更新屏幕显示
pygame.display.update()


while True:
    pass
# 结束
pygame.quit()