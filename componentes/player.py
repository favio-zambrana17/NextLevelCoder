import pygame

from componentes.bullet import Bullet
from componentes.bigbullet import Big_Bullet
from os import path
from utils.constants import (SCREEN_HEIGHT, SCREEN_WIDTH, IMG_DIR, WHITE)


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.time = 0
        self.time1 = 0
        self.game = game
        self.image = pygame.image.load(path.join(IMG_DIR, "ddd.png")).convert()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.bullets = pygame.sprite.Group()
        self.flag = False
        self.ammo = False

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            self.rect.centerx += 5

        if key[pygame.K_LEFT]:
            self.rect.centerx -= 5

        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.left <= 0:
            self.rect.left = 0

    def shoot(self):
        sound_rifle = pygame.mixer.Sound(path.join(IMG_DIR, "rifle.ogg"))
        pygame.mixer.Sound.play(sound_rifle)
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.game.all_sprites.add(bullet)
        self.bullets.add(bullet)
        self.time += 1
        if self.time == 6:
            self.flag = False
        if self.flag:
            bullet1 = Bullet(self.rect.centerx + 10, self.rect.top)
            self.game.all_sprites.add(bullet1)
            self.bullets.add(bullet1)
            bullet2 = Bullet(self.rect.centerx + -10, self.rect.top)
            self.game.all_sprites.add(bullet2)
            self.bullets.add(bullet2)
            bullet3 = Bullet(self.rect.centerx + 20, self.rect.top)
            self.game.all_sprites.add(bullet3)
            self.bullets.add(bullet3)
            bullet4 = Bullet(self.rect.centerx + -20, self.rect.top)
            self.game.all_sprites.add(bullet4)
            self.bullets.add(bullet4)
        self.time1 += 1
        if self.time1 == 10:
            self.ammo = False
        if self.ammo:
            big_bullet = Big_Bullet(self.rect.centerx, self.rect.top)
            self.game.all_sprites.add(big_bullet)
            self.bullets.add(big_bullet)


