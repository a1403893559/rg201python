import pygame
pygame.init()
'''游戏代码'''
hero_rect = pygame.Rect(100,500,120,126)

print('坐标原点 %d %d'%(hero_rect.x,hero_rect.y))
print('英雄大小 %d %d'%(hero_rect.width,hero_rect.height))
# size属性会返回矩形区域的（宽 高） 元祖
print('英雄大小 %d %d',hero_rect.size)
pygame.quit()