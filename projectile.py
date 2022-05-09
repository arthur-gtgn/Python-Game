import pygame
import math


class Projectile:

    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, window):
        pygame.draw.circle(window, (0,0,0), (self.x, self.y), self.radius)
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius-1)

    @staticmethod
    def projectile_path(start_x, start_y, power, angle, time):
        vel_x = math.cos(angle) * power
        vel_y = math.sin(angle) * power

        dist_x = vel_x * time
        dist_y = (vel_y * time) + ((-4.9 * time**2)/2)

        new_x = round(dist_x + start_x)
        new_y = round(start_y - dist_y)

        return new_x, new_y

