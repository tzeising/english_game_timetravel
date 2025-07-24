"""
Exercise state - grammar exercises when collecting stones
"""

import pygame
from settings import *
from game.levels.level_manager import LevelManager


class ExerciseState:
    def __init__(self, game):
        self.game = game
        self.level_manager = LevelManager()
        self.current_stone_id = 0
        self.current_exercise = None
        self.input_text = ""
        self.feedback = ""
        self.feedback_color = WHITE
        self.font = pygame.font.Font(None, 24)
        self.title_font = pygame.font.Font(None, 32)

    def set_stone(self, stone_id):
        """Set which stone's exercise to show"""
        self.current_stone_id = stone_id
        level_data = self.level_manager.get_level(self.game.current_level)
        self.current_exercise = level_data['exercises'][stone_id]
        self.input_text = ""
        self.feedback = ""

    def enter(self):
        """Called when entering this state"""
        pass

    def exit(self):
        """Called when leaving this state"""
        pass

    def handle_events(self, event):
        """Handle input events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.check_answer()
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            elif event.key == pygame.K_ESCAPE:
                # Skip exercise (lose points)
                self.game.change_state('playing')
            else:
                # Add character to input
                if event.unicode and len(self.input_text) < 20:
                    self.input_text += event.unicode

    def check_answer(self):
        """Check if the answer is correct"""
        if self.input_text.strip().lower() == self.current_exercise['answer'].lower():
            self.feedback = "CORRECT! Well done!"
            self.feedback_color = GREEN
            self.game.complete_exercise()

            # Return to game after delay
            pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
        else:
            self.feedback = "Try again! Check your answer."
            self.feedback_color = RED

    def update(self, dt):
        """Update exercise state"""
        # Check for return to game event
        for event in pygame.event.get([pygame.USEREVENT + 1]):
            if event.type == pygame.USEREVENT + 1:
                pygame.time.set_timer(pygame.USEREVENT + 1, 0)  # Cancel timer
                self.game.change_state('playing')

    def draw(self, screen):
        """Draw the exercise screen"""
        # Dark overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        # Exercise box
        box_width = 600
        box_height = 400
        box_x = (WINDOW_WIDTH - box_width) // 2
        box_y = (WINDOW_HEIGHT - box_height) // 2

        # Box background
        pygame.draw.rect(screen, WHITE, (box_x, box_y, box_width, box_height))
        pygame.draw.rect(screen, GOLD, (box_x, box_y, box_width, box_height), 5)

        # Title
        title = self.title_font.render("TIME STONE CHALLENGE", True, RED)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, box_y + 40))
        screen.blit(title, title_rect)

        # Question
        question = self.current_exercise['question']
        # Split at the blank
        parts = question.split('_____')

        y_pos = box_y + 120
        if len(parts) == 2:
            # Draw first part
            text1 = self.font.render(parts[0], True, BLACK)
            screen.blit(text1, (box_x + 50, y_pos))

            # Draw input box
            input_x = box_x + 50 + text1.get_width() + 10
            input_width = 150
            pygame.draw.rect(screen, (240, 240, 240), (input_x, y_pos - 5, input_width, 30))
            pygame.draw.rect(screen, BLACK, (input_x, y_pos - 5, input_width, 30), 2)

            # Draw input text
            input_surface = self.font.render(self.input_text, True, BLACK)
            screen.blit(input_surface, (input_x + 5, y_pos))

            # Draw cursor
            cursor_x = input_x + 5 + input_surface.get_width()
            if pygame.time.get_ticks() % 1000 < 500:  # Blinking cursor
                pygame.draw.line(screen, BLACK, (cursor_x, y_pos), (cursor_x, y_pos + 20), 2)

            # Draw second part
            text2 = self.font.render(parts[1], True, BLACK)
            screen.blit(text2, (input_x + input_width + 10, y_pos))

        # Hint
        hint_text = f"Hint: {self.current_exercise['hint']}"
        hint_surface = self.font.render(hint_text, True, (100, 100, 100))
        screen.blit(hint_surface, (box_x + 50, y_pos + 60))

        # Feedback
        if self.feedback:
            feedback_surface = self.font.render(self.feedback, True, self.feedback_color)
            feedback_rect = feedback_surface.get_rect(center=(WINDOW_WIDTH // 2, y_pos + 120))
            screen.blit(feedback_surface, feedback_rect)

        # Instructions
        inst1 = self.font.render("Press ENTER to submit", True, GREEN)
        inst2 = self.font.render("Press ESC to skip (lose points)", True, RED)
        screen.blit(inst1, (box_x + 50, box_y + box_height - 80))
        screen.blit(inst2, (box_x + 50, box_y + box_height - 50))