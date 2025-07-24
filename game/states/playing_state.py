"""
Playing state - main gameplay
"""

import pygame
from game.entities.player import Player
from game.entities.enemy import Enemy
from game.entities.platform import Platform
from game.entities.time_stone import TimeStone
from game.entities.portal import Portal
from game.levels.level_manager import LevelManager
from game.ui.hud import HUD
from utils.camera import Camera
from settings import *


class PlayingState:
    def __init__(self, game):
        self.game = game
        self.level_manager = LevelManager()
        self.camera = Camera(WINDOW_WIDTH, WINDOW_HEIGHT, LEVEL_WIDTH, LEVEL_HEIGHT)
        self.hud = HUD()

        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.stones = pygame.sprite.Group()
        self.time_holes = []

        # Player
        self.player = Player(50, 450)
        self.all_sprites.add(self.player)

        # Portal
        self.portal = None

        # Background elements
        self.background_elements = []

    def enter(self):
        """Called when entering this state"""
        self.load_level(self.game.current_level)

    def exit(self):
        """Called when leaving this state"""
        pass

    def load_level(self, level_num):
        """Load a specific level"""
        # Clear existing sprites
        self.all_sprites.empty()
        self.platforms.empty()
        self.enemies.empty()
        self.stones.empty()
        self.time_holes = []
        self.background_elements = []

        # Get level data
        level_data = self.level_manager.get_level(level_num)

        # Add player back
        self.player.reset(50, 450)
        self.all_sprites.add(self.player)

        # Create platforms
        for plat_data in level_data['platforms']:
            platform = Platform(plat_data['x'], plat_data['y'],
                                plat_data['width'], plat_data['height'])
            self.platforms.add(platform)
            self.all_sprites.add(platform)

        # Create time holes
        if 'timeHoles' in level_data:
            for hole_data in level_data['timeHoles']:
                hole = pygame.Rect(hole_data['x'], hole_data['y'],
                                   hole_data['width'], hole_data['height'])
                self.time_holes.append(hole)

        # Create enemies
        for enemy_data in level_data['enemies']:
            enemy = Enemy(enemy_data['x'], enemy_data['y'],
                          enemy_data['vx'], enemy_data['range'])
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)

        # Create time stones
        for i, stone_data in enumerate(level_data['stones']):
            stone = TimeStone(stone_data['x'], stone_data['y'], i)
            self.stones.add(stone)
            self.all_sprites.add(stone)

        # Create portal
        portal_data = level_data['portal']
        self.portal = Portal(portal_data['x'], portal_data['y'])
        self.all_sprites.add(self.portal)

        # Store background elements
        self.background_elements = level_data.get('background', {})

        # Update game total stones
        self.game.total_stones = len(level_data['stones'])
        self.game.stones_collected = 0

    def handle_events(self, event):
        """Handle input events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.change_state('menu')

    def update(self, dt):
        """Update game logic"""
        # Update all sprites
        self.all_sprites.update(dt, self.platforms, self.time_holes)

        # Update camera to follow player
        self.camera.update(self.player)

        # Check collisions
        self.check_collisions()

        # Check if fallen off screen
        if self.player.rect.y > WINDOW_HEIGHT:
            self.player.reset(50, 450)
            if self.game.lose_life():
                return

        # Update portal state
        self.portal.set_unlocked(self.game.stones_collected >= self.game.total_stones)

    def check_collisions(self):
        """Check for collisions between entities"""
        # Player vs enemies
        enemy_hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
        if enemy_hits:
            self.player.reset(50, 450)
            if self.game.lose_life():
                return

        # Player vs stones
        stone_hits = pygame.sprite.spritecollide(self.player, self.stones, True)
        for stone in stone_hits:
            self.game.collect_stone()
            # Show exercise
            self.game.states['exercise'].set_stone(stone.stone_id)
            self.game.change_state('exercise')

        # Player vs portal
        if self.portal.unlocked and self.player.rect.colliderect(self.portal.rect):
            # Level complete!
            self.level_complete()

    def level_complete(self):
        """Called when level is completed"""
        # Could show level complete screen
        self.game.next_level()

    def draw(self, screen):
        """Draw everything"""
        # Draw sky gradient
        self.draw_sky(screen)

        # Apply camera offset
        camera_offset = self.camera.apply

        # Draw background elements
        self.draw_background_elements(screen, camera_offset)

        # Draw time holes
        for hole in self.time_holes:
            hole_rect = camera_offset(hole)
            pygame.draw.rect(screen, BLACK, hole_rect)
            # Glitch effect border
            pygame.draw.rect(screen, PURPLE, hole_rect, 3)

        # Draw all sprites with camera offset
        for sprite in self.all_sprites:
            screen.blit(sprite.image, camera_offset(sprite.rect))

        # Draw HUD (no camera offset)
        self.hud.draw(screen, self.game)

    def draw_sky(self, screen):
        """Draw sky gradient background"""
        if self.game.current_level == 1:
            # Colonial era sunset
            for y in range(0, WINDOW_HEIGHT, 5):
                color_r = int(135 + (y / WINDOW_HEIGHT) * 120)
                color_g = int(206 - (y / WINDOW_HEIGHT) * 100)
                color_b = int(235 - (y / WINDOW_HEIGHT) * 100)
                color = (min(255, color_r), min(255, color_g), min(255, color_b))
                pygame.draw.rect(screen, color, (0, y, WINDOW_WIDTH, 5))
        else:
            screen.fill(SKY_BLUE)

    def draw_background_elements(self, screen, camera_offset):
        """Draw background decorations"""
        # Simplified background drawing
        # In a full implementation, these would use actual sprites

        # Draw clouds
        for i in range(5):
            x = (i * 300 + pygame.time.get_ticks() // 50) % (LEVEL_WIDTH + 100) - 50
            y = 50 + i * 40
            cloud_rect = pygame.Rect(x, y, 80, 40)
            pygame.draw.ellipse(screen, WHITE, camera_offset(cloud_rect))

    def reset_level(self):
        """Reset the current level"""
        self.load_level(self.game.current_level)