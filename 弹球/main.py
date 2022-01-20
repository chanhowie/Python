import pygame
import random

pygame.init()
pygame.display.set_caption("ri")
screen = pygame.display.set_mode((600, 500))

screen_file_x = 0
screen_file_y = 255
screen_file_z = 0

position_x = random.randint(0, 600)
position_y = random.randint(0, 500)

radius = random.randint(10, 30)
radius_goal = 0

speed = 4
clock = pygame.time.Clock()
i = speed
j = speed
k = 0

def change1():
    global screen_file_x
    screen_file_x = random.randint(0, 255)
    global screen_file_y
    screen_file_y = random.randint(0, 255)
    global screen_file_z
    screen_file_z = random.randint(0, 255)
    global radius_goal
    radius_goal = random.randint(10, 40)


while True:
    clock.tick(60)
    if position_x < 0:
        i = speed
        change1()
    elif position_x > 600:
        i = -speed
        change1()
    if position_y > 500:
        j = speed
        change1()
    elif position_y < 0:
        j = -speed
        change1()
    if radius < radius_goal and k > 10:
        radius += 1
        k = 0
    elif radius > radius_goal and k > 10:
        k = 0
        radius -= 1
    k += 1
    print(k)
    position_x += i
    position_y -= j
    screen.fill((0, 0, 0))
    circle = pygame.draw.circle(screen,
                                (screen_file_x, screen_file_y, screen_file_z),
                                (position_x, position_y), radius,
                                0)
    print("当前大小%d 目标大小%d "%(radius,radius_goal))
    pygame.display.update()
