import pygame
from projectile import Projectile
from game import Game
import math

wScreen = 1200
hScreen = 500

win = pygame.display.set_mode((wScreen, hScreen))
background = pygame.image.load("assets/background.png")

x = 0
y = 0
time = 0
power = 0
angle = 0
shoot = False

game = Game()


def find_angle(pos):
    sX = game.player.projectile.rect.x
    sY = game.player.projectile.rect.y

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


def redraw_window(shooting):
    game.player.projectile.draw(win)
    if not shooting:
        pygame.draw.line(win, (255, 255, 255), line[0], line[1])
    pygame.display.update()


run = True
while run:
    win.blit(background, (0, 0))
    win.blit(game.player.image, game.player.rect)

    for foe in game.all_foes:
        foe.forward()

    game.all_foes.draw(win)
    pos = pygame.mouse.get_pos()
    line = [(game.player.projectile.rect.x, game.player.projectile.rect.y), pos]

    if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < wScreen:
        game.player.move_right()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()

    redraw_window(shoot)

    if shoot:

        if game.player.projectile.rect.y < 350 - game.player.projectile.radius \
                and game.player.projectile.rect.x < wScreen and \
                not game.check_collision(game.player.projectile, game.all_foes):

            time += 0.1
            po = Projectile.projectile_path(x, y, power, angle, time)
            game.player.projectile.rect.x = po[0]
            game.player.projectile.rect.y = po[1]

        else:
            shoot = False
            game.player.projectile.rect.y = game.player.rect.y + 50
            game.player.projectile.rect.x = game.player.rect.x + 50

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Hello World")
            if shoot is False:
                shoot = True
                x = game.player.projectile.rect.x
                y = game.player.projectile.rect.y
                time = 0
                power = (math.sqrt((line[1][1] - line[0][1]) ** 2 + (line[1][0] - line[0][0]) ** 2)) / 8
                angle = find_angle(pos)
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
