"""
Level select state
"""

import pygame
from settings import *


class LevelSelectState:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 32)
        self.title_font = pygame.font.Font(None, 48)

        # Level buttons
        self.buttons = [
            {'level': 1, 'text': 'LEVEL 1: 1776', 'rect': pygame.Rect(0, 0, 400, 60)},
            {'level': 2, 'text': 'LEVEL 2: 1865', 'rect': pygame.Rect(0, 0, 400, 60)},
            {'level': 3, 'text': 'LEVEL 3: 1963', 'rect': pygame.Rect(0, 0, 400, 60)}
        ]

        # Position buttons
        start_y = 200
        for i, button in enumerate(self.buttons):
            button['rect'].center = (WINDOW_WIDTH // 2, start_y + i * 100)

        # Back button
        self.back_button = pygame.Rect(0, 0, 200, 50)
        self.back_button.center = (WINDOW_WIDTH // 2, 550)

        self.selected_button = None

    def enter(self):
        """Called when entering this state"""
        pass

    def exit(self):
        """Called when leaving this state"""
        pass

    def handle_events(self, event):
        """Handle input events"""
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            self.selected_button = None

            # Check level buttons
            for button in self.buttons:
                if button['rect'].collidepoint(mouse_pos):
                    self.selected_button = button
                    break

            # Check back button
            if self.back_button.collidepoint(mouse_pos):
                self.selected_button = 'back'

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.selected_button:
                if self.selected_button == 'back':
                    self.game.change_state('menu')
                else:
                    # Start selected level
                    self.game.current_level = self.selected_button['level']
                    self.game.reset_level()
                    self.game.change_state('playing')

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.change_state('menu')
            elif event.key >= pygame.K_1 and event.key <= pygame.K_3:
                level = event.key - pygame.K_0
                self.game.current_level = level
                self.game.reset_level()
                self.game.change_state('playing')

    def update(self, dt):
        """Update level select"""
        pass

    def draw(self, screen):
        """Draw level select screen"""
        screen.fill(SKY_BLUE)

        # Title
        title = self.title_font.render("SELECT LEVEL", True, GOLD)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 80))
        screen.blit(title, title_rect)

        # Level buttons
        for button in self.buttons:
            # Determine button color
            if self.selected_button == button:
                color = GOLD
                border_color = WHITE
            else:
                color = BROWN
                border_color = GOLD

            # Draw button
            pygame.draw.rect(screen, color, button['rect'])
            pygame.draw.rect(screen, border_color, button['rect'], 3)

            # Button text
            text = self.font.render(button['text'], True, WHITE)
            text_rect = text.get_rect(center=button['rect'].center)
            screen.blit(text, text_rect)

            # Level description
            desc = ""
            if button['level'] == 1:
                desc = "Philadelphia - First Conditional"
            elif button['level'] == 2:
                desc = "Civil War - Second Conditional"
            elif button['level'] == 3:
                desc = "Civil Rights - Mixed Conditionals"

            desc_font = pygame.font.Font(None, 20)
            desc_text = desc_font.render(desc, True, WHITE)
            desc_rect = desc_text.get_rect(center=(button['rect'].centerx, button['rect'].bottom + 20))
            screen.blit(desc_text, desc_rect)

        # Back button
        back_color = GOLD if self.selected_button == 'back' else BROWN
        back_border = WHITE if self.selected_button == 'back' else GOLD

        pygame.draw.rect(screen, back_color, self.back_button)
        pygame.draw.rect(screen, back_border, self.back_button, 3)

        back_text = self.font.render("BACK", True, WHITE)
        back_rect = back_text.get_rect(center=self.back_button.center)
        screen.blit(back_text, back_rect)