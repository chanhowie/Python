import pygame.time

from plane_enemy import *


class PlaneGame(object):
    def __init__(self):
        print("初始化")
        # 创建窗口
        self.screem = pygame.display.set_mode(SCERRN_RECT.size)
        # 创建时钟
        self.clock = pygame.time.Clock()
        # 创建私有方法
        self.__creat_sprite()
        # 设置定时器事件
        pygame.time.set_timer(CREAT_ENEMY_EVENT, 100)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
    
    def stargame(self):
        # 1设置刷新率
        self.clock.tick(FRAME_PER_SEC)
        # 2事件监听
        self.__event_handler()
        # 3碰撞监听
        self.__check_collide()
        # 4更新绘制组
        self.__update_sprites()
        # 5更新显示
        pygame.display.update()
    
    def __event_handler(self):
        for event in pygame.event.get():
            # print(event)
            # 判断是否退出
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREAT_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            
            if event.type == HERO_FIRE_EVENT:
                self.hero.fire()


            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed = 7
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -7
            elif keys_pressed[pygame.K_UP]:
                self.hero.yspeed = -5
            elif keys_pressed[pygame.K_DOWN]:
                self.hero.yspeed = 5
            
            else:
                self.hero.speed = 0
                self.hero.yspeed = 0
    
    def __check_collide(self):
        # 子弹与敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 触碰敌机
        # pygame.sprite.groupcollide(self.hero_group, self.enemy_group, True, True)
        died=pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if not len(died)==0:
            #游戏失败
            #结束游戏
            self.__game_over()

    def __creat_sprite(self):
        # 创建背景精灵和精灵组
        bg1 = BackGround()
        bg2 = BackGround(True)
        
        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        #
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
    
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screem)
        self.enemy_group.update()
        self.enemy_group.draw(self.screem)
        self.hero_group.update()
        self.hero_group.draw(self.screem)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screem)
    
    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象  启动游戏
    game = PlaneGame()
    while True:
        game.stargame()
