#import pygame
#pygame.init()
#pygame.quit()
#from pygame import *
#init()
#quit()
# 1、导入pygame的所有模块
# 2、开始初始化模块
# 3、结束模块
# 4、初始化一个游戏窗口
# 5、添加一个游戏循环
# 6、添加游戏背景
# 7、添加图片的三个步骤  步骤1 load加载 步骤2 把绘制绘制窗口上 步骤3 更新窗口
# 8、添加飞机 三个步骤
# 1
import pygame
from plane import *
# 2
pygame.init()
# 4 display 是屏幕   set_mod 设置大小
screen = pygame.display.set_mode((480,700))
# 6 image模块    load方法
bg = pygame.image.load('/home/wengwenyu/vscodeProject/rg201python/2018年新代码存放区域/images/background.png')
# 7 绘制
screen.blit(bg,(0,0))
# 7 更新
# 8
hero_me = pygame.image.load('/home/wengwenyu/vscodeProject/rg201python/2018年新代码存放区域/images/me1.png')
# 设置英雄的初始位置
hero_rect = pygame.Rect(200,600,102,126)
screen.blit(hero_me,hero_rect)

# 新的代码  创建敌方飞机
enemy1 = GameSprite('/home/wengwenyu/vscodeProject/rg201python/2018年新代码存放区域/images/enemy1.png')

# 设置敌机的为止
enemy1.rect.x = 50
enemy1.rect.y = 50

# 把敌机添加到精灵组
enemy_Group = pygame.sprite.Group(enemy1)
# update 和 draw方法
enemy_Group.update()
enemy_Group.draw(screen)
pygame.display.update()
# 游戏时钟
clock = pygame.time.Clock()



# 5
while True:
    # 设置帧率
    clock.tick(60)


    # 捕获事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('退出游戏')
            pygame.quit()
            exit()
    if hero_rect.y == 0:
        hero_rect.y = 600
    else:
        # 设置y轴的值
        hero_rect.y = hero_rect.y - 1
        

    # 重新设置一下背景
    screen.blit(bg,(0,0))
    # 绘制英雄的坐标
    screen.blit(hero_me,hero_rect)
    # update 和 draw方法
    enemy_Group.update()
    enemy_Group.draw(screen)
    # 更新屏幕
    pygame.display.update()
    #print(hero_rect.x,hero_rect.y)
    # pass
# 3
pygame.quit()