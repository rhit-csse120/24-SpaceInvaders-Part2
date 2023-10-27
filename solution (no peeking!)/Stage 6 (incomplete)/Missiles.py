# Author: Sam.

import pygame
from Missile import Missile
from Enemies import Enemies


class Missiles:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.list_of_missiles: list[Missile] = []

    def add_missile(self, missile: Missile):
        self.list_of_missiles.append(missile)

    def draw(self):
        for missile in self.list_of_missiles:
            missile.draw()

    def move(self):
        for missile in self.list_of_missiles:
            missile.move()

    def remove_dead_missiles(self):
        pass

    def handle_explosions(self, enemies: Enemies):
        for missile in self.list_of_missiles:
            for enemy in enemies.list_of_enemies:
                if enemy.is_hit_by(missile):
                    missile.explode()
                    if not enemy.has_exploded:
                        enemy.explode()
                    break  # Assumes Missile cannot explode more than one Enemy.



