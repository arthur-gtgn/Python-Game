import pygame
import random


class HealthPack(pygame.sprite.Sprite):

    def __init__(self, bonus_event):
        super().__init__()

        self.bonus_event = bonus_event

        self.image = pygame.image.load("assets/bonus.png")

        self.rect = self.image.get_rect()

        self.gpe = random.randint(1, 3)
        self.rect.x = random.randint(20, 1180)

        self.last = pygame.time.get_ticks()
        self.cooldown = 5000

    def fall(self):
        if self.rect.y <= 350:
            self.rect.y += self.gpe
        else:
            self.bonus_event.all_packs.remove(self)

        if self.bonus_event.game.check_collision(self, self.bonus_event.game.all_players):
            self.remove()
            self.bonus_event.game.player.add_hp(10)
