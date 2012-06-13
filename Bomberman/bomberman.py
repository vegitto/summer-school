import pygame
import random

from pygame.locals import *

class GameException(Exception):
    pass

class Settings(object):
    def __init__(self):
            self.resolution = (950, 950)
            self.background = (48,121,4)
            self.title = "BOMBERMAN"

class Game(object):
    def __init__(self,settings = Settings()):
            pygame.init()
            self.init_from_settings(settings)
            self.clock = pygame.time.Clock()
            self.table = [ [random.randint(0, 1) for i in range(

    def init_from_settings(self,settings):
            self.screen = pygame.display.set_mode(settings.resolution)
            pygame.display.set_caption(settings.title)
            background = pygame.Surface(self.screen.get_size())
            self.background = background.convert()
            self.background.fill(settings.background)

    def run(self):
        while True:
                try:
                        self.game_tick()
                except GameException:
                        return

    def game_tick(self):
        self.clock.tick(60)
        for event in pygame.event.get():
                if event.type == QUIT:
                       raise GameException
        for i in range(2, 18, 2):
            for j in range(2, 18, 2):
                x1 = i * 50
                y1 = j * 50
                x2 = 50
                y2 = 50
                pygame.draw.rect(self.background,
                pygame.color.Color("grey"), (x1, y1, x2, y2), 0)
                pygame.draw.rect(self.background,
                pygame.color.Color("black"),(x1, y1, x2, y2), 2)

        for i in range(21):
            x = i * 50
            y = (i + 1) * 50
            pygame.draw.rect(self.background, pygame.color.Color("grey"),
                        (0, x, 50, y), 0)
            pygame.draw.rect(self.background, pygame.color.Color("black"),
                        (0, x, 50, y), 3)
            pygame.draw.rect(self.background, pygame.color.Color("grey"),
                        (x, 0, y, 50), 0)
            pygame.draw.rect(self.background, pygame.color.Color("black"),
                        (x, 0, y, 50), 3)
            pygame.draw.rect(self.background, pygame.color.Color("grey"),
                        (900, x, 950, y), 0)
            pygame.draw.rect(self.background, pygame.color.Color("black"),
                        (900, x, 950, y), 3)
            pygame.draw.rect(self.background, pygame.color.Color("grey"),
                        (x, 900, y, 950), 0)
            pygame.draw.rect(self.background, pygame.color.Color("black"),
                        (x, 900, y, 950), 3)
        self.screen.blit(self.background, (0,0))
     #  self.allsprites.draw(self.screen)
        pygame.display.flip()

