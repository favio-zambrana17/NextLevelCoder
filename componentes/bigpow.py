import pygame
import random
from os import path
from utils.constants import (SCREEN_WIDTH, WHITE, IMG_DIR)

allowed_speed = list(range(1, 3))


class Bigpow(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR, "ppp.png")).convert()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.speedy = random.choice(allowed_speed)
        self.size = size

    def update(self):
        self.rect.y = self.rect.y + self.speedy
