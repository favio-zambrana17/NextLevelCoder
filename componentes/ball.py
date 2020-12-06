import pygame
import random

from os import path

from utils.constants import (BLACK, SCREEN_HEIGHT, SCREEN_WIDTH, IMG_DIR)
allowed_speed = list(range(1, 3))


class Ball(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR, "blue.png")).convert()
        self.image = pygame.transform.scale(self.image, (100 // size, 100 // size))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.choice(allowed_speed)
        self.speedx = random.choice(allowed_speed)
        self.size = size

    def update(self):
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.speedx = random.choice(allowed_speed) * - 1
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = random.choice(allowed_speed)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.speedy = random.choice(allowed_speed) * - 1
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedy = random.choice(allowed_speed)
