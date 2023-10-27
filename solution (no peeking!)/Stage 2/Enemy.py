# Author: Pippin.

import pygame
from Missile import Missile


class Enemy:
    def __init__(self, screen: pygame.Surface,
                 x=100, y=50, h_speed=5, v_speed=10):
        self.screen = screen
        self.image = pygame.image.load("../assets/badguy.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y
        self.h_speed = h_speed  # Increase speeds to make the game harder.
        self.v_speed = v_speed
        self.direction = 1
        self.original_x = x
        self.is_off_the_screen = False
        self.has_exploded = False
        self.explosion_sound = pygame.mixer.Sound("../assets/explosion.wav")

        print("Constructed an Enemy.")  # Temporary

    def draw(self):
        """ Draw (blit) the image of this Fighter. """

    def move(self):
        """
        Move this Enemy left/right (per its direction) and down as needed.
        """

    def is_hit_by(self, missile: Missile):
        """ True if this Enemy and the given Missile overlap. """

    def explode(self):
        """ This Enemy explodes: Play a sound and set has_exploded to True. """

