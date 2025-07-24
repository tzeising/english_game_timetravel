#!/usr/bin/env python3
"""
The Time Guardian: Lila's Quest
A time-traveling educational platformer game
"""

import pygame
import sys
from game.game import Game
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, TITLE, FPS


def main():
    """Main entry point for the game"""
    # Initialize Pygame
    pygame.init()
    pygame.mixer.init()

    # Create the game window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)

    # Create clock for controlling frame rate
    clock = pygame.time.Clock()

    # Create the game instance
    game = Game(screen)

    # Main game loop
    running = True
    while running:
        # Calculate delta time
        dt = clock.tick(FPS) / 1000.0

        # Handle events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            game.handle_events(event)

        # Update game state
        game.update(dt)

        # Draw everything
        game.draw()
        pygame.display.flip()

    # Quit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()