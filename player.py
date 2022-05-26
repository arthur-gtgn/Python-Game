import pygame.sprite
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()

        self.game = game

        self.health = 100

        self.max_health = 100
        self.attack = 100
        self.velocity = 5

        self.image = pygame.image.load("assets/monster.png")
        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 204

        self.projectile = Projectile(self.rect.x + 50, self.rect.y + 50, 5, self)

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_foes):
            self.rect.x += self.velocity
            self.projectile.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
        self.projectile.rect.x -= self.velocity
