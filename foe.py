import pygame
import random


class Foe(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()

        self.game = game

        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.velocity = 1 + random.randint(0, 2)

        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()

        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 320

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.rect.x = 1225 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = 1 + random.randint(0, 2)
            self.game.add_score(50)

    def update_health_bar(self, surf):
        pygame.draw.rect(surf, (255, 0, 0), [self.rect.x - 26, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surf, (0, 255, 0), [self.rect.x - 26, self.rect.y - 20, self.health, 5])

    def forward(self, window):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        elif self.game.check_collision(self, self.game.all_players):
            self.game.player.damage(self.attack, window)
