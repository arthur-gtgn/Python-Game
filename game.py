import pygame
from player import Player
from foe import Foe


class Game:

    def __init__(self):
        self.is_playing = False

        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        self.all_foes = pygame.sprite.Group()
        self.pressed = {}

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

    def update(self, window, wscreen):
        self.player.update_health_bar(window)

        for foe in self.all_foes:
            foe.forward()
            foe.update_health_bar(window)

        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < wscreen:
            self.player.move_right()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > 0:
            self.player.move_left()

        self.all_foes.draw(window)
        window.blit(self.player.image, self.player.rect)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        foe = Foe(self)
        self.all_foes.add(foe)
