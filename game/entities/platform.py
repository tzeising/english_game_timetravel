"""
Platform class - various platform types
"""

import pygame
from settings import *


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Determine platform type based on position
        if y >= 500:  # Ground level - cobblestone
            self.draw_cobblestone()
        else:  # Floating platform - wood
            self.draw_wood()

    def draw_cobblestone(self):
        """Draw cobblestone texture"""
        # Base color
        self.image.fill((105, 105, 105))

        # Stone pattern
        stone_color = (84, 84, 84)
        for y in range(0, self.rect.height, 15):
            for x in range(0, self.rect.width, 20):
                offset = 10 if (y // 15) % 2 else 0
                pygame.draw.rect(self.image, stone_color,
                                 (x + offset, y, 18, 13), 1)

        # Worn spots
        for i in range(10):
            x = pygame.time.get_ticks() % self.rect.width
            y = (pygame.time.get_ticks() * i) % self.rect.height
            pygame.draw.circle(self.image, (60, 60, 60), (x, y), 3)

    def draw_wood(self):
        """Draw wooden platform"""
        # Wood gradient
        for i in range(self.rect.height):
            color_val = 139 + (i / self.rect.height) * 30
            color = (int(color_val * 0.8), int(color_val * 0.6), int(color_val * 0.4))
            pygame.draw.line(self.image, color, (0, i), (self.rect.width, i))

        # Wood grain
        grain_color = (90, 74, 58)
        for x in range(0, self.rect.width, 8):
            pygame.draw.line(self.image, grain_color,
                             (x, 0), (x + 3, self.rect.height), 1)

    def update(self, dt, platforms=None, time_holes=None):
        """Platforms don't move, but method required for sprite group"""
        pass