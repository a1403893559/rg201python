import pygame
# 游戏的开始（加载资源，所有的模块加载进来
pygame.init()

hero_rect = pygame.Rect(10,10,50,50)

print('英雄的原点 %d %d'%(hero_rect.x,hero_rect.y))
print('英雄的大小 %d %d'%(hero_rect.width,hero_rect.height))
print('英雄的大小 %d %d'%hero_rect.size)

# 游戏结束 （卸载资源）
pygame.quit()