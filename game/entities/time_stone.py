"""
Time Stone class - collectible items
"""

import pygame
import math
from settings import *


class TimeStone(pygame.sprite.Sprite):
    def __init__(self, x, y, stone_id):
        super().__init__()

        self.stone_id = stone_id
        self.pos = pygame.math.Vector2(x, y)
        self.rotation = 0
        self.pulse = 0

        # Create sprite
        self.original_image = pygame.Surface((STONE_SIZE * 2, STONE_SIZE * 2), pygame.SRCALPHA)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))

        # Draw stone
        self.draw_stone()

    def draw_stone(self):
        """Draw the time stone"""
        center = STONE_SIZE

        # Outer glow
        for i in range(10, 0, -1):
            alpha = int(255 * (1 - i / 10) * 0.3)
            color = (*GOLD, alpha)
            pygame.draw.circle(self.original_image, color, (center, center), STONE_SIZE + i)

        # Main stone (diamond shape)
        points = [
            (center, center - STONE_SIZE),  # Top
            (center + STONE_SIZE, center),  # Right
            (center, center + STONE_SIZE),  # Bottom
            (center - STONE_SIZE, center)  # Left
        ]

        # Stone gradient effect
        pygame.draw.polygon(self.original_image, GOLD, points)

        # Inner light
        inner_points = [
            (center, center - STONE_SIZE // 2),
            (center + STONE_SIZE // 2, center),
            (center, center + STONE_SIZE // 2),
            (center - STONE_SIZE // 2, center)
        ]
        pygame.draw.polygon(self.original_image, (255, 255, 200), inner_points)

    def update(self, dt, platforms=None, time_holes=None):
        """Update stone animation"""
        # Rotation
        self.rotation += dt * 100

        # Pulsing effect
        self.pulse = (math.sin(pygame.time.get_ticks() / 300) + 1) / 2

        # Rotate image
        self.image = pygame.transform.rotate(self.original_image, self.rotation)
        self.rect = self.image.get_rect(center=(self.pos.x, self.pos.y))

        # Scale with pulse
        scale = 1 + self.pulse * 0.2
        new_size = (int(self.rect.width * scale), int(self.rect.height * scale))
        self.image = pygame.transform.scale(self.image, new_size)
        self.rect = self.image.get_rect(center=(self.pos.x, self.pos.y))