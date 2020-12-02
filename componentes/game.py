import pygame

from componentes.ball import Ball
from componentes.player import Player
from utils.constants import (SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, BLACK)



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        #un ejemplo
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        self.create_components()
        #gameloop:
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()
        pygame.quit()  #metodo para terminar el juego - metodo

    def create_components(self):
        self.all_sprites = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        ball = Ball(1)
        self.all_sprites.add(ball)
        self.balls.add(ball)

    def update(self):
        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(self.player, self.balls, False)
        if hits:
            self.playing = False

        hits = pygame.sprite.groupcollide(self.balls, self.player.bullets, True, True)
        for hit in hits:
            if hit.size < 4:
                for i in range (0, 2):
                    ball = Ball(hit.size + 1)
                    self.all_sprites.add(ball)
                    self.balls.add(ball)


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #QUIT - constante
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                 self.player.shoot()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()


