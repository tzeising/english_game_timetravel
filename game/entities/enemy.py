"""
Enemy class - Red coat guards
"""

import pygame
from settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, patrol_range):
        super().__init__()

        # Position and movement
        self.start_x = x
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(vx * ENEMY_SPEED, 0)
        self.patrol_range = patrol_range

        # Create sprite
        self.image = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Draw enemy
        self.draw_enemy()

    def draw_enemy(self):
        """Draw red coat guard"""
        # Body (red coat)
        pygame.draw.rect(self.image, RED, (8, 12, 16, 20))

        # Head
        pygame.draw.circle(self.image, (255, 218, 185), (16, 8), 8)

        # Hat (tricorn)
        pygame.draw.rect(self.image, (139, 0, 0), (8, 0, 16, 6))
        pygame.draw.rect(self.image, (139, 0, 0), (6, 5, 20, 3))

        # Eyes
        pygame.draw.rect(self.image, WHITE, (11, 6, 3, 3))
        pygame.draw.rect(self.image, WHITE, (18, 6, 3, 3))
        pygame.draw.rect(self.image, BLACK, (12, 7, 1, 1))
        pygame.draw.rect(self.image, BLACK, (19, 7, 1, 1))

        # Arms
        pygame.draw.rect(self.image, RED, (4, 14, 4, 12))
        pygame.draw.rect(self.image, RED, (24, 14, 4, 12))

        # Musket
        pygame.draw.rect(self.image, BROWN, (26, 8, 2, 20))
        pygame.draw.rect(self.image, (192, 192, 192), (26, 8, 2, 5))

    def update(self, dt, platforms=None, time_holes=None):
        """Update enemy position"""
        # Move back and forth
        self.pos.x += self.vel.x * dt

        # Check patrol range
        if abs(self.pos.x - self.start_x) > self.patrol_range:
            self.vel.x *= -1

            # Flip sprite
            if self.vel.x > 0:
                self.image = pygame.transform.flip(self.image, False, False)
            else:
                self.image = pygame.transform.flip(self.image, True, False)

        # Update rect
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y