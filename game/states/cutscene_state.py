"""
Cutscene state - story sequences
"""

import pygame
from settings import *


class CutsceneState:
    def __init__(self, game):
        self.game = game
        self.current_panel = 0
        self.panels = []
        self.font = pygame.font.Font(None, 20)
        self.name_font = pygame.font.Font(None, 24)

        # Define cutscene panels
        self.create_panels()

    def create_panels(self):
        """Create cutscene panels"""
        self.panels = [
            {
                'background': 'observatory',
                'speaker': 'Professor Quinn',
                'text': 'So... the Watch chose you. I didn\'t expect someone so young... but time rarely does what we expect.'
            },
            {
                'background': 'watch',
                'speaker': 'Professor Quinn',
                'text': 'Time is breaking. My old friend Elias Morgenstern... he\'s become Chronos. Grief twisted him. He\'s begun to erase history, thread by thread.'
            },
            {
                'background': 'bookstore',
                'speaker': 'Narrator',
                'text': 'Lila Torres never thought she was special. But the moment she touched the watch, the world... shifted.'
            },
            {
                'background': 'glitch',
                'speaker': 'Professor Quinn',
                'text': 'If we don\'t act now, time itself will unravel. That\'s why you must go back to where Elias first lost hope...'
            },
            {
                'background': 'philadelphia',
                'speaker': 'Professor Quinn',
                'text': 'Philadelphia, 1776. This was when Elias still believed in change. Help him remember... If they unite, they will gain their freedom.'
            }
        ]

    def enter(self):
        """Called when entering this state"""
        self.current_panel = 0

    def exit(self):
        """Called when leaving this state"""
        self.game.cutscene_shown = True

    def handle_events(self, event):
        """Handle input events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                self.next_panel()
            elif event.key == pygame.K_ESCAPE:
                self.skip_cutscene()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.next_panel()

    def next_panel(self):
        """Go to next panel"""
        self.current_panel += 1
        if self.current_panel >= len(self.panels):
            self.end_cutscene()

    def skip_cutscene(self):
        """Skip the cutscene"""
        self.end_cutscene()

    def end_cutscene(self):
        """End cutscene and start game"""
        self.game.change_state('playing')

    def update(self, dt):
        """Update cutscene"""
        pass

    def draw(self, screen):
        """Draw current panel"""
        screen.fill(BLACK)

        panel = self.panels[self.current_panel]

        # Draw background based on type
        self.draw_background(screen, panel['background'])

        # Draw text box
        self.draw_textbox(screen, panel['speaker'], panel['text'])

        # Draw skip button
        skip_text = self.font.render("Press ESC to skip", True, WHITE)
        screen.blit(skip_text, (WINDOW_WIDTH - 150, 20))

    def draw_background(self, screen, bg_type):
        """Draw panel background"""
        if bg_type == 'observatory':
            # Stars
            for i in range(100):
                x = (i * 137) % WINDOW_WIDTH
                y = (i * 241) % WINDOW_HEIGHT
                pygame.draw.circle(screen, WHITE, (x, y), 1)

            # Quinn silhouette
            pygame.draw.rect(screen, BLACK, (200, 400, 80, 120))

            # Time map (glowing)
            pygame.draw.circle(screen, GREEN, (500, 450), 50)
            pygame.draw.circle(screen, (0, 255, 0, 128), (500, 450), 60, 3)

        elif bg_type == 'watch':
            # Watch
            pygame.draw.circle(screen, GOLD, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 60)
            pygame.draw.circle(screen, BROWN, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 60, 5)
            pygame.draw.circle(screen, WHITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 40)

            # Fracture lines
            for i in range(4):
                x = WINDOW_WIDTH // 4 + i * 150
                pygame.draw.line(screen, RED, (x, 100), (x, WINDOW_HEIGHT - 100), 2)

        elif bg_type == 'bookstore':
            # Bookshelf
            pygame.draw.rect(screen, BROWN, (0, WINDOW_HEIGHT - 200, WINDOW_WIDTH, 200))

            # Lila
            pygame.draw.rect(screen, BLUE, (300, 400, 40, 60))

            # Glowing box
            pygame.draw.rect(screen, GOLD, (400, 420, 60, 40))

        elif bg_type == 'glitch':
            # Photos disappearing
            for i in range(3):
                alpha = 255 - i * 85
                surf = pygame.Surface((100, 120))
                surf.set_alpha(alpha)
                surf.fill(BROWN)
                screen.blit(surf, (200 + i * 200, 200))

        elif bg_type == 'philadelphia':
            # Buildings
            for i in range(4):
                x = 100 + i * 200
                pygame.draw.rect(screen, BROWN, (x, 300, 120, 180))

            # Cobblestone
            pygame.draw.rect(screen, (105, 105, 105), (0, 480, WINDOW_WIDTH, 120))

            # Lila
            pygame.draw.rect(screen, BLUE, (100, 420, 40, 60))

            # Time stone
            pygame.draw.circle(screen, RED, (600, 450), 15)

    def draw_textbox(self, screen, speaker, text):
        """Draw dialogue textbox"""
        # Box
        box_height = 120
        box_y = WINDOW_HEIGHT - box_height - 20

        pygame.draw.rect(screen, (26, 26, 26), (20, box_y, WINDOW_WIDTH - 40, box_height))
        pygame.draw.rect(screen, WHITE, (20, box_y, WINDOW_WIDTH - 40, box_height), 3)

        # Speaker name
        name_color = BLUE if speaker == 'Narrator' else GOLD
        name_text = self.name_font.render(speaker + ":", True, name_color)
        screen.blit(name_text, (40, box_y + 10))

        # Text (word wrap)
        words = text.split(' ')
        lines = []
        current_line = []

        for word in words:
            test_line = ' '.join(current_line + [word])
            if self.font.size(test_line)[0] < WINDOW_WIDTH - 100:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]

        if current_line:
            lines.append(' '.join(current_line))

        # Draw lines
        y = box_y + 40
        for line in lines:
            text_surf = self.font.render(line, True, WHITE)
            screen.blit(text_surf, (40, y))
            y += 25

        # Continue indicator
        if pygame.time.get_ticks() % 1000 < 500:
            points = [(WINDOW_WIDTH - 50, box_y + 90),
                      (WINDOW_WIDTH - 40, box_y + 90),
                      (WINDOW_WIDTH - 45, box_y + 100)]
            pygame.draw.polygon(screen, WHITE, points)