"""
Camera class for scrolling view
"""

import pygame
from settings import *


class Camera:
    def __init__(self, width, height, level_width, level_height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.level_width = level_width
        self.level_height = level_height

    def apply(self, entity):
        """Apply camera offset to an entity"""
        if isinstance(entity, pygame.Rect):
            return entity.move(-self.camera.x, -self.camera.y)
        else:
            # For sprites
            return pygame.Rect(entity.rect.x - self.camera.x,
                               entity.rect.y - self.camera.y,
                               entity.rect.width, entity.rect.height)

    def update(self, target):
        """Update camera to follow target"""
        # Center camera on target
        x = target.rect.centerx - self.width // 2
        y = target.rect.centery - self.height // 2

        # Limit scrolling to level bounds
        x = max(0, min(x, self.level_width - self.width))
        y = max(0, min(y, self.level_height - self.height))

        self.camera = pygame.Rect(x, y, self.width, self.height)