"""
Resource manager for loading game assets
"""

import pygame
import os
from settings import *


class ResourceManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.fonts = {}

        # Try to load assets
        self.load_resources()

    def load_resources(self):
        """Load all game resources"""
        # Note: Since we're using placeholder graphics for now,
        # this will create colored rectangles as placeholders

        # Create placeholder images
        self.create_placeholder_graphics()

        # Load fonts (fallback to system font if custom font not found)
        try:
            font_path = os.path.join(FONTS_DIR, "PressStart2P.ttf")
            if os.path.exists(font_path):
                self.fonts['main'] = pygame.font.Font(font_path, 16)
                self.fonts['title'] = pygame.font.Font(font_path, 24)
            else:
                self.fonts['main'] = pygame.font.Font(None, 20)
                self.fonts['title'] = pygame.font.Font(None, 32)
        except:
            self.fonts['main'] = pygame.font.Font(None, 20)
            self.fonts['title'] = pygame.font.Font(None, 32)

    def create_placeholder_graphics(self):
        """Create placeholder graphics until real assets are available"""
        # Character placeholders
        self.images['lila_idle'] = self.create_colored_surface(32, 48, PINK)
        self.images['lila_walk'] = self.create_colored_surface(32, 48, PINK)
        self.images['lila_jump'] = self.create_colored_surface(32, 48, PINK)
        self.images['enemy_redcoat'] = self.create_colored_surface(32, 32, RED)

        # Object placeholders
        self.images['time_stone'] = self.create_colored_surface(32, 32, GOLD)
        self.images['portal_locked'] = self.create_colored_surface(60, 70, (50, 50, 50))
        self.images['portal_open'] = self.create_colored_surface(60, 70, PURPLE)

        # Platform placeholders
        self.images['platform_cobblestone'] = self.create_textured_surface(100, 20, (105, 105, 105))
        self.images['platform_wood'] = self.create_textured_surface(100, 20, BROWN)

        # Background placeholders
        self.images['colonial_building'] = self.create_colored_surface(80, 60, BROWN)
        self.images['liberty_bell'] = self.create_colored_surface(40, 50, GOLD)
        self.images['street_lamp'] = self.create_colored_surface(20, 60, (70, 70, 70))

        # UI placeholders
        self.images['heart_full'] = self.create_heart(20, 20, RED)
        self.images['heart_empty'] = self.create_heart(20, 20, (100, 0, 0))

    def create_colored_surface(self, width, height, color):
        """Create a colored rectangle as placeholder"""
        surf = pygame.Surface((width, height), pygame.SRCALPHA)
        surf.fill(color)
        return surf

    def create_textured_surface(self, width, height, color):
        """Create a textured surface"""
        surf = pygame.Surface((width, height))
        surf.fill(color)
        # Add simple texture
        darker = tuple(int(c * 0.8) for c in color)
        for y in range(0, height, 4):
            pygame.draw.line(surf, darker, (0, y), (width, y))
        return surf

    def create_heart(self, width, height, color):
        """Create a heart shape"""
        surf = pygame.Surface((width, height), pygame.SRCALPHA)
        # Draw heart using circles and polygon
        pygame.draw.circle(surf, color, (width // 4, height // 4), width // 4)
        pygame.draw.circle(surf, color, (3 * width // 4, height // 4), width // 4)
        points = [(0, height // 3), (width, height // 3), (width // 2, height)]
        pygame.draw.polygon(surf, color, points)
        return surf

    def get_image(self, name):
        """Get an image by name"""
        return self.images.get(name, self.create_colored_surface(32, 32, PURPLE))

    def get_sound(self, name):
        """Get a sound by name"""
        return self.sounds.get(name, None)

    def get_font(self, name='main'):
        """Get a font by name"""
        return self.fonts.get(name, pygame.font.Font(None, 20))