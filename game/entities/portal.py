"""
Portal class - level exit
"""

import pygame
import math
from settings import *


class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)
        self.unlocked = False
        self.swirl_angle = 0

        # Create sprite
        self.image = pygame.Surface((PORTAL_WIDTH, PORTAL_HEIGHT), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))

    def set_unlocked(self, unlocked):
        """Set portal state"""
        self.unlocked = unlocked

    def update(self, dt, platforms=None, time_holes=None):
        """Update portal animation"""
        self.swirl_angle += dt * 100
        self.draw_portal()

    def draw_portal(self):
        """Draw the portal"""
        self.image.fill((0, 0, 0, 0))  # Clear

        if self.unlocked:
            # Active portal - swirling effect
            center_x = PORTAL_WIDTH // 2
            center_y = PORTAL_HEIGHT // 2

            # Multiple swirl layers
            for i in range(5):
                angle = self.swirl_angle + i * 30
                scale = 1 + i * 0.3
                alpha = 255 - i * 40

                # Draw ellipse
                width = int(PORTAL_WIDTH * 0.8 * scale)
                height = int(PORTAL_HEIGHT * 0.8 * scale)

                # Create a temporary surface for rotation
                temp_surf = pygame.Surface((width, height), pygame.SRCALPHA)
                color = (*PURPLE, alpha)
                pygame.draw.ellipse(temp_surf, color, (0, 0, width, height))

                # Rotate and blit
                rotated = pygame.transform.rotate(temp_surf, angle)
                rot_rect = rotated.get_rect(center=(center_x, center_y))
                self.image.blit(rotated, rot_rect)

            # Central bright spot
            pygame.draw.ellipse(self.image, (255, 255, 255, 200),
                                (center_x - 10, center_y - 15, 20, 30))
        else:
            # Locked portal
            # Frame
            pygame.draw.rect(self.image, (51, 51, 51), (0, 0, PORTAL_WIDTH, PORTAL_HEIGHT))
            pygame.draw.rect(self.image, (102, 102, 102), (5, 5, PORTAL_WIDTH - 10, PORTAL_HEIGHT - 10))
            pygame.draw.rect(self.image, BLACK, (10, 10, PORTAL_WIDTH - 20, PORTAL_HEIGHT - 20))

            # Lock symbol
            lock_x = PORTAL_WIDTH // 2
            lock_y = PORTAL_HEIGHT // 2

            # Lock body
            pygame.draw.rect(self.image, GOLD, (lock_x - 10, lock_y - 5, 20, 15))

            # Lock shackle
            pygame.draw.arc(self.image, GOLD, (lock_x - 8, lock_y - 15, 16, 20),
                            0, math.pi, 3)