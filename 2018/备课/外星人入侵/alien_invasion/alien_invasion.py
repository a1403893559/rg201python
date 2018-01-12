# 系统模块
import sys
# 第三方模块
import pygame
# 导入自己写的模块里面的某个类
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf
from alien import Alien

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
    ship = Ship(screen,ai_settings)
    
    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()
    # 创建一个外星人
    #alien = Alien(ai_settings,screen)
    
    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
       # for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
        #        sys.exit()
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        
        ## 删除已消失的子弹
        #for bullet in bullets.copy():
        #    if bullet.rect.bottom <= 0:
        #        bullets.remove(bullet)
        #print(len(bullets))

        gf.update_bullets(bullets)
        #gf.update_screen(ai_settings,screen,ship,alien,bullets) 
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        ## 每次循环时都会重绘屏幕
        #screen.fill(ai_settings.bg_color)
        #ship.blitme()
        ## 让最近绘制的屏幕可见
        #pygame.display.flip()

run_game()

