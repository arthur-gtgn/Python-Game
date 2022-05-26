import pygame


class Foe(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()

        self.game = game

        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 1

        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()

        self.rect.x = 1000
        self.rect.y = 204

    def update_health_bar(self):
        return

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
