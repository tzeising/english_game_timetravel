"""
Main game class that manages game states and flow
"""

import pygame
from game.states.menu_state import MenuState
from game.states.playing_state import PlayingState
from game.states.cutscene_state import CutsceneState
from game.states.exercise_state import ExerciseState
from game.states.level_select_state import LevelSelectState
from utils.resources import ResourceManager
from settings import *


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True

        # Initialize resource manager
        self.resources = ResourceManager()

        # Game data
        self.score = 0
        self.lives = INITIAL_LIVES
        self.current_level = 1
        self.stones_collected = 0
        self.total_stones = 0
        self.cutscene_shown = False

        # Initialize states
        self.states = {
            'menu': MenuState(self),
            'playing': PlayingState(self),
            'cutscene': CutsceneState(self),
            'exercise': ExerciseState(self),
            'level_select': LevelSelectState(self)
        }

        # Set initial state
        self.current_state = self.states['menu']

    def change_state(self, state_name):
        """Change to a different game state"""
        if state_name in self.states:
            self.current_state.exit()
            self.current_state = self.states[state_name]
            self.current_state.enter()

    def handle_events(self, event):
        """Pass events to current state"""
        self.current_state.handle_events(event)

    def update(self, dt):
        """Update current state"""
        self.current_state.update(dt)

    def draw(self):
        """Draw current state"""
        self.current_state.draw(self.screen)

    def reset_level(self):
        """Reset current level"""
        self.lives = INITIAL_LIVES
        self.stones_collected = 0
        self.states['playing'].reset_level()

    def next_level(self):
        """Advance to next level"""
        if self.current_level < 3:
            self.current_level += 1
            self.reset_level()
            self.change_state('playing')
        else:
            # Game complete - return to menu
            self.change_state('menu')

    def game_over(self):
        """Handle game over"""
        # Could show game over screen
        self.change_state('menu')

    def collect_stone(self):
        """Called when player collects a time stone"""
        self.stones_collected += 1
        self.score += STONE_SCORE

    def complete_exercise(self):
        """Called when player completes an exercise"""
        self.score += EXERCISE_SCORE

    def lose_life(self):
        """Called when player loses a life"""
        self.lives -= 1
        if self.lives <= 0:
            self.game_over()
            return True
        return False