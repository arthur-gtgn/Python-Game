import pygame
from projectile import Projectile
import math

wScreen = 1200
hScreen = 500

win = pygame.display.set_mode((wScreen, hScreen))

x = 0
y = 0
time = 0
power = 0
angle = 0
shoot = False

bullet = Projectile(300, 300, 5, (255, 255, 255))


def find_angle(pos):
    sX = bullet.x
    sY = bullet.y

    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle = math.pi / 2

    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle

    return angle


def redraw_window():
    win.fill((64, 64, 64))
    bullet.draw(win)
    pygame.draw.line(win, (255, 255, 255), line[0], line[1])
    pygame.display.update()


run = True

while run:
    pos = pygame.mouse.get_pos()
    line = [(bullet.x, bullet.y), pos]
    redraw_window()

    if shoot:
        if bullet.y < 500 - bullet.radius:
            time += 0.05
            po = Projectile.projectile_path(x, y, power, angle, time)
            bullet.x = po[0]
            bullet.y = po[1]
        else:
            shoot = False
            bullet.y = 494

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Hello World")
            if shoot is False:
                shoot = True
                x = bullet.x
                y = bullet.y
                time = 0
                power = (math.sqrt((line[1][1] - line[0][1]) ** 2 + (line[1][0] - line[0][0]) ** 2)) / 8
                angle = find_angle(pos)
