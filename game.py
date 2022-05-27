import pygame
from player import Player
from foe import Foe
from bonus_event import BonusEvent
pygame.init()


class Game:

    def __init__(self):
        self.is_playing = False

        self.bonus_event = BonusEvent(self)

        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        self.all_foes = pygame.sprite.Group()

        self.score = 0
        self.pressed = {}

    def add_score(self, amount):
        self.score += amount

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()

    def wasted(self):
        self.all_foes = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0

    def update(self, window, wscreen):

        font = pygame.font.SysFont("arial", 20)
        score_text = font.render(f"Score: {self.score}", 1, (255, 255, 255))
        window.blit(score_text, (20, 30))

        self.player.update_health_bar(window)

        self.bonus_event.update_bar(window)

        for foe in self.all_foes:
            foe.forward(window)
            foe.update_health_bar(window)

        for pack in self.bonus_event.all_packs:
            pack.fall()

        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < wscreen:
            self.player.move_right()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > 0:
            self.player.move_left()

        self.all_foes.draw(window)
        window.blit(self.player.image, self.player.rect)
        self.bonus_event.all_packs.draw(window)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        foe = Foe(self)
        self.all_foes.add(foe)
