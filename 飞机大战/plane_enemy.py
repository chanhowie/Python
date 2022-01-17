import random
import pygame

# 屏幕大小
SCERRN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60
# 创建敌机时间
CREAT_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class Game_Sprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.yspeed=0
    
    def update(self):
        self.rect.y = self.rect.y + self.speed


class BackGround(Game_Sprite):
    def update(self):
        super().update()
        if self.rect.y > SCERRN_RECT.height:
            self.rect.y = -SCERRN_RECT.height
    
    def __init__(self, is_alt=False):
        # 调用父类方法实现精灵的创建
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = - self.rect.height


class Enemy(Game_Sprite):
    def __init__(self):
        super().__init__("./images/enemy1.png")
        # 指定速度
        self.speed = random.randint(1, 3)
        # 指定位置
        self.rect.y = -self.rect.height
        self.rect.x = random.randint(0, SCERRN_RECT.width - self.rect.width)
    
    def update(self):
        super().update()
        if self.rect.y > SCERRN_RECT.height:
            # kill 方法可以让对象被移除
            self.kill()
        # 是否飞出屏幕
    
    def __del__(self):
        pass  # print("挂了%s "%self.rect)


class Hero(Game_Sprite):
    def __init__(self):
        super().__init__("./images/me1.png", 0)
        self.rect.centerx = SCERRN_RECT.centerx
        self.rect.bottom = SCERRN_RECT.bottom - 20

        self.bullets = pygame.sprite.Group()
    
    def update(self):
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCERRN_RECT.right:
            self.rect.right = SCERRN_RECT.right
        else:
            self.rect.x = self.rect.x + self.speed
            self.rect.y = self.rect.y + self.yspeed
            
    
    def fire(self):
        for i in (0,1,2):
            bullet = Bullet()
            bullet.rect.bottom=self.rect.y-i*20
            bullet.rect.centerx=self.rect.centerx
            self.bullets.add(bullet)


class Bullet(Game_Sprite):
    def __init__(self):
        super().__init__("./images/bullet1.png",-2)
    
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
    
    def __del__(self):
        pass
