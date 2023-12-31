# TODO: Authors: Put your names here (entire team)

import pygame
from Game import Game


class View:
    def __init__(self, screen: pygame.Surface, game: Game):
        self.screen = screen
        self.game = game
        self.background_color = pygame.Color("black")  # TODO: Choose own color

    def draw_everything(self):
        self.screen.fill(self.background_color)
        self.game.draw_game()
        pygame.display.update()
