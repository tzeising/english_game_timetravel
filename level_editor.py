#!/usr/bin/env python3
"""
Simple Level Editor for The Time Guardian
"""

import pygame
import json
import tkinter as tk
from tkinter import filedialog, messagebox
from settings import *


class LevelEditor:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Time Guardian - Level Editor")
        self.clock = pygame.time.Clock()

        # Editor state
        self.running = True
        self.mode = 'platform'  # platform, stone, enemy, portal, timehole
        self.grid_size = 20
        self.show_grid = True
        self.camera_x = 0

        # Level data
        self.platforms = []
        self.stones = []
        self.enemies = []
        self.time_holes = []
        self.portal = None

        # Current selection
        self.selecting = False
        self.select_start = None
        self.current_platform = None

        # UI
        self.font = pygame.font.Font(None, 24)
        self.create_ui()

    def create_ui(self):
        """Create UI elements"""
        self.mode_buttons = [
            {'mode': 'platform', 'text': '[1] Platform', 'key': pygame.K_1, 'color': BROWN},
            {'mode': 'stone', 'text': '[2] Stone', 'key': pygame.K_2, 'color': GOLD},
            {'mode': 'enemy', 'text': '[3] Enemy', 'key': pygame.K_3, 'color': RED},
            {'mode': 'portal', 'text': '[4] Portal', 'key': pygame.K_4, 'color': PURPLE},
            {'mode': 'timehole', 'text': '[5] Time Hole', 'key': pygame.K_5, 'color': BLACK}
        ]

    def snap_to_grid(self, pos):
        """Snap position to grid"""
        x = round(pos[0] / self.grid_size) * self.grid_size
        y = round(pos[1] / self.grid_size) * self.grid_size
        return (x, y)

    def handle_events(self):
        """Handle input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                # Mode selection
                for button in self.mode_buttons:
                    if event.key == button['key']:
                        self.mode = button['mode']

                # Other controls
                if event.key == pygame.K_g:
                    self.show_grid = not self.show_grid
                elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.save_level()
                elif event.key == pygame.K_o and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.load_level()
                elif event.key == pygame.K_DELETE:
                    self.delete_at_mouse()
                elif event.key == pygame.K_LEFT:
                    self.camera_x = max(0, self.camera_x - 100)
                elif event.key == pygame.K_RIGHT:
                    self.camera_x = min(LEVEL_WIDTH - WINDOW_WIDTH, self.camera_x + 100)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self.handle_click(event.pos)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and self.selecting:
                    self.finish_selection(event.pos)

            elif event.type == pygame.MOUSEMOTION:
                if self.selecting:
                    self.update_selection(event.pos)

    def handle_click(self, pos):
        """Handle mouse click"""
        world_pos = (pos[0] + self.camera_x, pos[1])
        snapped = self.snap_to_grid(world_pos)

        if self.mode == 'platform' or self.mode == 'timehole':
            self.selecting = True
            self.select_start = snapped
            self.current_platform = {
                'x': snapped[0],
                'y': snapped[1],
                'width': self.grid_size,
                'height': self.grid_size
            }

        elif self.mode == 'stone':
            self.stones.append({'x': snapped[0], 'y': snapped[1]})

        elif self.mode == 'enemy':
            # Create enemy with default values
            self.enemies.append({
                'x': snapped[0],
                'y': snapped[1],
                'vx': 1,
                'range': 100
            })

        elif self.mode == 'portal':
            self.portal = {'x': snapped[0], 'y': snapped[1]}

    def update_selection(self, pos):
        """Update platform selection"""
        if self.current_platform and self.select_start:
            world_pos = (pos[0] + self.camera_x, pos[1])
            snapped = self.snap_to_grid(world_pos)

            self.current_platform['width'] = abs(snapped[0] - self.select_start[0])
            self.current_platform['height'] = abs(snapped[1] - self.select_start[1])
            self.current_platform['x'] = min(snapped[0], self.select_start[0])
            self.current_platform['y'] = min(snapped[1], self.select_start[1])

    def finish_selection(self, pos):
        """Finish platform selection"""
        if self.current_platform:
            if self.current_platform['width'] > 0 and self.current_platform['height'] > 0:
                if self.mode == 'platform':
                    self.platforms.append(self.current_platform.copy())
                elif self.mode == 'timehole':
                    self.time_holes.append(self.current_platform.copy())

        self.selecting = False
        self.select_start = None
        self.current_platform = None

    def delete_at_mouse(self):
        """Delete object at mouse position"""
        mouse_pos = pygame.mouse.get_pos()
        world_pos = (mouse_pos[0] + self.camera_x, mouse_pos[1])

        # Check platforms
        self.platforms = [p for p in self.platforms
                          if not (p['x'] <= world_pos[0] <= p['x'] + p['width'] and
                                  p['y'] <= world_pos[1] <= p['y'] + p['height'])]

        # Check stones
        self.stones = [s for s in self.stones
                       if not (abs(s['x'] - world_pos[0]) < 20 and
                               abs(s['y'] - world_pos[1]) < 20)]

        # Check enemies
        self.enemies = [e for e in self.enemies
                        if not (abs(e['x'] - world_pos[0]) < 20 and
                                abs(e['y'] - world_pos[1]) < 20)]

        # Check time holes
        self.time_holes = [h for h in self.time_holes
                           if not (h['x'] <= world_pos[0] <= h['x'] + h['width'] and
                                   h['y'] <= world_pos[1] <= h['y'] + h['height'])]

    def draw(self):
        """Draw everything"""
        self.screen.fill(SKY_BLUE)

        # Draw grid
        if self.show_grid:
            for x in range(0, LEVEL_WIDTH, self.grid_size):
                pygame.draw.line(self.screen, (200, 200, 200),
                                 (x - self.camera_x, 0), (x - self.camera_x, WINDOW_HEIGHT))
            for y in range(0, WINDOW_HEIGHT, self.grid_size):
                pygame.draw.line(self.screen, (200, 200, 200),
                                 (0, y), (WINDOW_WIDTH, y))

        # Draw platforms
        for platform in self.platforms:
            rect = pygame.Rect(platform['x'] - self.camera_x, platform['y'],
                               platform['width'], platform['height'])
            pygame.draw.rect(self.screen, BROWN, rect)
            pygame.draw.rect(self.screen, BLACK, rect, 2)

        # Draw time holes
        for hole in self.time_holes:
            rect = pygame.Rect(hole['x'] - self.camera_x, hole['y'],
                               hole['width'], hole['height'])
            pygame.draw.rect(self.screen, BLACK, rect)
            pygame.draw.rect(self.screen, PURPLE, rect, 3)

        # Draw stones
        for stone in self.stones:
            pos = (stone['x'] - self.camera_x, stone['y'])
            pygame.draw.circle(self.screen, GOLD, pos, 15)
            pygame.draw.circle(self.screen, (255, 255, 200), pos, 8)

        # Draw enemies
        for enemy in self.enemies:
            rect = pygame.Rect(enemy['x'] - self.camera_x - 16, enemy['y'] - 16, 32, 32)
            pygame.draw.rect(self.screen, RED, rect)
            pygame.draw.rect(self.screen, (139, 0, 0), rect, 2)

            # Draw patrol range
            pygame.draw.line(self.screen, (255, 100, 100),
                             (enemy['x'] - enemy['range'] - self.camera_x, enemy['y']),
                             (enemy['x'] + enemy['range'] - self.camera_x, enemy['y']), 2)

        # Draw portal
        if self.portal:
            rect = pygame.Rect(self.portal['x'] - self.camera_x, self.portal['y'], 60, 70)
            pygame.draw.rect(self.screen, PURPLE, rect)
            pygame.draw.rect(self.screen, WHITE, rect, 3)

        # Draw current selection
        if self.selecting and self.current_platform:
            rect = pygame.Rect(self.current_platform['x'] - self.camera_x,
                               self.current_platform['y'],
                               self.current_platform['width'],
                               self.current_platform['height'])
            color = BROWN if self.mode == 'platform' else BLACK
            pygame.draw.rect(self.screen, (*color, 128), rect)
            pygame.draw.rect(self.screen, WHITE, rect, 2)

        # Draw UI
        self.draw_ui()

    def draw_ui(self):
        """Draw UI elements"""
        # Mode buttons
        y = 10
        for button in self.mode_buttons:
            color = WHITE if self.mode == button['mode'] else (200, 200, 200)
            text = self.font.render(button['text'], True, color)
            self.screen.blit(text, (10, y))
            y += 30

        # Instructions
        instructions = [
            "G - Toggle Grid",
            "Ctrl+S - Save Level",
            "Ctrl+O - Load Level",
            "Delete - Delete Object",
            "← → - Move Camera",
            f"Camera: {self.camera_x}"
        ]

        y = WINDOW_HEIGHT - len(instructions) * 25 - 10
        for inst in instructions:
            text = self.font.render(inst, True, WHITE)
            self.screen.blit(text, (10, y))
            y += 25

        # Object counts
        counts = [
            f"Platforms: {len(self.platforms)}",
            f"Stones: {len(self.stones)}",
            f"Enemies: {len(self.enemies)}",
            f"Time Holes: {len(self.time_holes)}"
        ]

        x = WINDOW_WIDTH - 200
        y = 10
        for count in counts:
            text = self.font.render(count, True, WHITE)
            self.screen.blit(text, (x, y))
            y += 25

    def save_level(self):
        """Save level to file"""
        # Create Tk root window
        root = tk.Tk()
        root.withdraw()

        # Ask for filename
        filename = filedialog.asksaveasfilename(
            defaultextension=".py",
            filetypes=[("Python files", "*.py"), ("All files", "*.*")],
            initialfile="level_new.py"
        )

        if filename:
            level_data = {
                'title': 'NEW LEVEL',
                'platforms': self.platforms,
                'timeHoles': self.time_holes,
                'stones': self.stones,
                'enemies': self.enemies,
                'portal': self.portal,
                'exercises': [
                                 {
                                     'question': 'If you _____ (play), you will learn.',
                                     'answer': 'play',
                                     'hint': 'First conditional'
                                 }
                             ] * len(self.stones)  # One exercise per stone
            }

            # Write Python file
            with open(filename, 'w') as f:
                f.write('"""\nCustom Level\n"""\n\n')
                f.write('LEVEL_CUSTOM = ')
                f.write(json.dumps(level_data, indent=4))
                f.write('\n')

            messagebox.showinfo("Success", f"Level saved to {filename}")

        root.destroy()

    def load_level(self):
        """Load level from file"""
        # This is a simplified loader - in practice, you'd parse the Python file
        messagebox.showinfo("Info", "Load feature not implemented.\nEdit level files directly.")

    def run(self):
        """Run the editor"""
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


def main():
    """Run the level editor"""
    print("=== Time Guardian Level Editor ===")
    print("\nControls:")
    print("1-5 - Select object type")
    print("Click and drag - Create platforms")
    print("Click - Place stones/enemies/portal")
    print("G - Toggle grid")
    print("Delete - Remove object under mouse")
    print("← → - Move camera")
    print("Ctrl+S - Save level")
    print("\nStarting editor...")

    editor = LevelEditor()
    editor.run()


if __name__ == "__main__":
    main()