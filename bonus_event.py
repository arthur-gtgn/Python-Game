import pygame
from health_pack import HealthPack


class BonusEvent:

    def __init__(self, game):
        self.game = game

        self.percent = 0
        self.percent_speed = 2
        self.all_packs = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def ready(self):
        return self.percent >= 100

    def pack_fall(self):
        self.all_packs.add(HealthPack(self))

    def start(self):
        if self.ready():
            print("Bonus")
            self.pack_fall()
            self.percent = 0

    def update_bar(self, surf):

        self.add_percent()

        self.start()

        pygame.draw.rect(surf, (128, 128, 128), [
            10,
            10,
            1175,
            10
        ])

        pygame.draw.rect(surf, (0, 0, 255), [
            10,
            10,
            (1175 / 100) * self.percent,
            10
        ])