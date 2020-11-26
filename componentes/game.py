import pygame
from utils.constants import (SCREEN_HEIGHT, SCREEN_WIDTH, TITLE)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        #un ejemplo
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    def run(self):
        self.create_components()
        #gameloop:
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()  #metodo para terminar el juego - metodo

    def create_components(self):
        pass

    def update(self):
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #QUIT - constante
                self.playing = False
    def draw(self):
        pass

