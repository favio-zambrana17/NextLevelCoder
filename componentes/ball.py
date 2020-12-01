import pygame
import random

from utils.constants import (BLUE, SCREEN_HEIGHT, SCREEN_WIDTH)

allowed_speed = list(range(3,7))

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.choice(allowed_speed)
        self.speedx = random.choice(allowed_speed)

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



