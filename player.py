import pygame.sprite
from projectile import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()

        self.game = game

        self.health = 100

        self.max_health = 100
        self.attack = 50
        self.velocity = 5

        self.image = pygame.image.load("assets/monster.png")
        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 204

        self.projectile = Projectile(self.rect.x + 50, self.rect.y + 50, 5, self)

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount

    def update_health_bar(self, surf):
        pygame.draw.rect(surf, (255, 0, 0), [self.rect.x - 26, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surf, (0, 255, 0), [self.rect.x - 26, self.rect.y - 20, self.health, 5])

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_foes):
            self.rect.x += self.velocity
            self.projectile.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
        self.projectile.rect.x -= self.velocity
