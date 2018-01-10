# 系统模块
import sys
# 第三方模块
import pygame
# 导入自己写的模块里面的某个类
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏并且创建一个屏幕对象
    pygame.init()
    #screen = pygame.display.set_mode((1200,800))
    #pygame.display.set_caption('外星人入侵')
    # 设置背景色
    #bg_color = (230,230,230)
    # 实例化一个设置类的对象
    ai_settings = Settings()
    # 初始化一个屏幕对象
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('外星人入侵')
    
    # 创建一膄飞船
    ship = Ship(screen)
    

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        #for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
        #        sys.exit()
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship) 
        ## 每次循环时都会重绘屏幕
        #screen.fill(ai_settings.bg_color)
        #ship.blitme()
        ## 让最近绘制的屏幕可见
        #pygame.display.flip()

run_game()

