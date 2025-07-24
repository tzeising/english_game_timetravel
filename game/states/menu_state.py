"""
Menu state - main menu
"""

import pygame
import pygame_menu
from settings import *


class MenuState:
    def __init__(self, game):
        self.game = game
        self.menu = None
        self.create_menu()

    def create_menu(self):
        """Create the main menu"""
        # Custom theme
        custom_theme = pygame_menu.themes.THEME_BLUE.copy()
        custom_theme.title_background_color = (139, 69, 19)
        custom_theme.widget_font = pygame_menu.font.FONT_8BIT
        custom_theme.widget_font_size = 20
        custom_theme.title_font_size = 30

        self.menu = pygame_menu.Menu(
            'The Time Guardian',
            WINDOW_WIDTH,
            WINDOW_HEIGHT,
            theme=custom_theme
        )

        # Add menu items
        self.menu.add.label('LILA\'S QUEST', font_size=25)
        self.menu.add.vertical_margin(30)
        self.menu.add.button('BEGIN MISSION', self.start_game)
        self.menu.add.button('LEVEL SELECT', self.level_select)
        self.menu.add.button('HOW TO PLAY', self.show_instructions)
        self.menu.add.button('QUIT', pygame_menu.events.EXIT)

        # Mission briefing text
        self.mission_text = [
            "Professor Quinn:",
            "",
            "The Watch chose you, Lila.",
            "Collect the Time Stones",
            "and stop Dr. Chronos!",
            "",
            "Save time itself from",
            "being unraveled..."
        ]
        self.show_mission = False

    def enter(self):
        """Called when entering this state"""
        self.show_mission = False
        # Reset game data when returning to menu
        self.game.score = 0
        self.game.lives = INITIAL_LIVES
        self.game.current_level = 1
        self.game.stones_collected = 0

    def exit(self):
        """Called when leaving this state"""
        pass

    def start_game(self):
        """Start the game"""
        self.show_mission = True

    def level_select(self):
        """Go to level select"""
        self.game.change_state('level_select')

    def show_instructions(self):
        """Show how to play"""
        instructions = [
            "HOW TO PLAY:",
            "",
            "Arrow Keys / A,D - Move",
            "Space / Up - Jump",
            "Collect Time Stones",
            "Answer grammar questions",
            "Reach the portal!",
            "",
            "Press ESC to continue"
        ]
        self.show_popup(instructions)

    def show_popup(self, text_lines):
        """Show a popup message"""
        # This would show a popup in the actual implementation
        pass

    def handle_events(self, event):
        """Handle input events"""
        if self.show_mission:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    # Start with cutscene
                    self.game.cutscene_shown = False
                    self.game.change_state('cutscene')
                elif event.key == pygame.K_ESCAPE:
                    self.show_mission = False
        else:
            self.menu.update([event])

    def update(self, dt):
        """Update menu"""
        pass

    def draw(self, screen):
        """Draw the menu"""
        if self.show_mission:
            # Draw mission briefing
            screen.fill(BLACK)

            # Draw briefing box
            box_width = 600
            box_height = 400
            box_x = (WINDOW_WIDTH - box_width) // 2
            box_y = (WINDOW_HEIGHT - box_height) // 2

            # Box background
            pygame.draw.rect(screen, BROWN, (box_x, box_y, box_width, box_height))
            pygame.draw.rect(screen, GOLD, (box_x, box_y, box_width, box_height), 5)

            # Draw text
            font = pygame.font.Font(None, 24)
            y_offset = box_y + 50
            for line in self.mission_text:
                if line == "Professor Quinn:":
                    text = font.render(line, True, GOLD)
                else:
                    text = font.render(line, True, WHITE)
                text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, y_offset))
                screen.blit(text, text_rect)
                y_offset += 35

            # Start button prompt
            prompt = font.render("Press ENTER to start", True, GREEN)
            prompt_rect = prompt.get_rect(center=(WINDOW_WIDTH // 2, box_y + box_height - 50))
            screen.blit(prompt, prompt_rect)
        else:
            # Draw main menu
            screen.fill(SKY_BLUE)
            self.menu.draw(screen)