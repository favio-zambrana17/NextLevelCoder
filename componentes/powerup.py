import pygame
import random
from os import path
from utils.constants import (SCREEN_WIDTH, IMG_DIR, WHITE)

allowed_speed = list(range(3,5))


class Powerup(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR, "cc.png")).convert()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.speedy = random.choice(allowed_speed)
        self.size = size

    def update(self):
        self.rect.y = self.rect.y + self.speedy

