import pygame

from settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(enemieses)
        self.image = ANIMATIONS['stay_l'][0]
        self.rect = pygame.Rect(x, y, 1, 1)
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x

    def update(self):
        pass

enemieseses = []

enemieses = pygame.sprite.Group()

enemieseses.append(Enemy(600, 369))
