import pygame
import math


class Projectile(pygame.sprite.Sprite):

    def __init__(self, x, y, radius, player):
        super().__init__()

        self.player = player
        self.image = pygame.image.load("assets/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.radius = radius

    def draw(self, window):
        window.blit(self.image, self.rect)

    @staticmethod
    def projectile_path(start_x, start_y, power, angle, time):
        vel_x = math.cos(angle) * power
        vel_y = math.sin(angle) * power

        dist_x = vel_x * time
        dist_y = (vel_y * time) + ((-4.9 * time**2)/2)

        new_x = round(dist_x + start_x)
        new_y = round(start_y - dist_y)

        return new_x, new_y

    def collision(self):
        if self.player.game.check_collision(self, self.player.game.all_foes):
            return True

