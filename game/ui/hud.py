"""
HUD - Heads-up display
"""

import pygame
from settings import *


class HUD:
    def __init__(self):
        self.font = pygame.font.Font(None, FONT_SIZE * 2)
        self.small_font = pygame.font.Font(None, FONT_SIZE)

    def draw(self, screen, game):
        """Draw HUD elements"""
        # Left panel - Score and stones
        self.draw_panel(screen, HUD_PADDING, HUD_PADDING, 200, 80)

        # Score
        score_text = self.font.render(f"SCORE: {game.score}", True, GOLD)
        screen.blit(score_text, (HUD_PADDING + 10, HUD_PADDING + 10))

        # Time stones
        stones_text = self.font.render(f"STONES: {game.stones_collected}/{game.total_stones}", True, GOLD)
        screen.blit(stones_text, (HUD_PADDING + 10, HUD_PADDING + 35))

        # Right panel - Lives
        lives_x = WINDOW_WIDTH - HUD_PADDING - 150
        self.draw_panel(screen, lives_x, HUD_PADDING, 150, 60)

        # Draw hearts
        heart_x = lives_x + 10
        heart_y = HUD_PADDING + 20
        for i in range(3):
            if i < game.lives:
                self.draw_heart(screen, heart_x + i * 40, heart_y, True)
            else:
                self.draw_heart(screen, heart_x + i * 40, heart_y, False)

        # Level title
        if hasattr(game, 'current_level'):
            level_text = f"LEVEL {game.current_level}"
            if game.current_level == 1:
                level_text += " - PHILADELPHIA 1776"
            elif game.current_level == 2:
                level_text += " - CIVIL WAR 1865"
            elif game.current_level == 3:
                level_text += " - CIVIL RIGHTS 1963"

            title = self.font.render(level_text, True, GOLD)
            title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 40))

            # Title background
            bg_rect = title_rect.inflate(40, 20)
            pygame.draw.rect(screen, (0, 0, 0, 180), bg_rect)
            pygame.draw.rect(screen, GOLD, bg_rect, 3)

            screen.blit(title, title_rect)

    def draw_panel(self, screen, x, y, width, height):
        """Draw a UI panel"""
        # Background
        panel_surf = pygame.Surface((width, height))
        panel_surf.set_alpha(200)
        panel_surf.fill(BLACK)
        screen.blit(panel_surf, (x, y))

        # Border
        pygame.draw.rect(screen, GOLD, (x, y, width, height), 3)

    def draw_heart(self, screen, x, y, full):
        """Draw a heart (life indicator)"""
        if full:
            color = (255, 0, 102)
        else:
            color = (100, 0, 51)

        # Heart shape using circles and polygon
        # Left bump
        pygame.draw.circle(screen, color, (x + 5, y + 5), 5)
        # Right bump
        pygame.draw.circle(screen, color, (x + 15, y + 5), 5)
        # Bottom triangle
        points = [
            (x, y + 5),
            (x + 20, y + 5),
            (x + 10, y + 18)
        ]
        pygame.draw.polygon(screen, color, points)