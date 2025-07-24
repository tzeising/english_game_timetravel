"""
Player class - Lila Torres, the Time Guardian
"""

import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Position and movement
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0, 0)
        self.facing = 'right'
        self.on_ground = False

        # Create sprite (placeholder rectangle for now)
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Animation
        self.anim_frame = 0
        self.anim_timer = 0
        self.state = 'idle'  # idle, walking, jumping

        # Draw Lila sprite (simplified version)
        self.draw_lila()

    def draw_lila(self):
        """Draw Lila's sprite"""
        self.image.fill((0, 0, 0, 0))  # Clear

        # Hair (lilac)
        hair_color = LILAC
        pygame.draw.ellipse(self.image, hair_color, (8, 2, 16, 20))

        # Face (peach)
        face_color = (255, 218, 185)
        pygame.draw.ellipse(self.image, face_color, (10, 8, 12, 14))

        # Eyes
        pygame.draw.circle(self.image, WHITE, (13, 14), 2)
        pygame.draw.circle(self.image, WHITE, (19, 14), 2)
        pygame.draw.circle(self.image, BLUE, (13, 14), 1)
        pygame.draw.circle(self.image, BLUE, (19, 14), 1)

        # Shirt (pink)
        pygame.draw.rect(self.image, PINK, (8, 22, 16, 12))

        # Arms
        arm_color = face_color
        pygame.draw.rect(self.image, arm_color, (4, 24, 4, 8))
        pygame.draw.rect(self.image, arm_color, (24, 24, 4, 8))

        # Pants (dark blue)
        pants_color = (44, 62, 80)
        pygame.draw.rect(self.image, pants_color, (10, 34, 12, 10))

        # Shoes (black)
        pygame.draw.rect(self.image, BLACK, (10, 44, 5, 4))
        pygame.draw.rect(self.image, BLACK, (17, 44, 5, 4))

    def update(self, dt, platforms, time_holes=None):
        """Update player position and state"""
        # Handle input
        keys = pygame.key.get_pressed()

        # Horizontal movement
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel.x = -PLAYER_SPEED
            self.facing = 'left'
            if self.on_ground:
                self.state = 'walking'
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel.x = PLAYER_SPEED
            self.facing = 'right'
            if self.on_ground:
                self.state = 'walking'
        else:
            self.vel.x *= FRICTION
            if abs(self.vel.x) < 10 and self.on_ground:
                self.state = 'idle'

        # Jumping
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground:
            self.vel.y = PLAYER_JUMP_POWER
            self.on_ground = False
            self.state = 'jumping'

        # Apply gravity
        self.vel.y += GRAVITY * dt

        # Update position
        self.pos.x += self.vel.x * dt
        self.pos.y += self.vel.y * dt

        # Update rect
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

        # Platform collision
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                # Landing on top
                if self.vel.y > 0 and self.rect.bottom > platform.rect.top:
                    if self.rect.bottom - platform.rect.top < 20:  # Landing threshold
                        self.rect.bottom = platform.rect.top
                        self.pos.y = self.rect.y
                        self.vel.y = 0
                        self.on_ground = True
                # Hitting from below
                elif self.vel.y < 0 and self.rect.top < platform.rect.bottom:
                    if platform.rect.bottom - self.rect.top < 20:
                        self.rect.top = platform.rect.bottom
                        self.pos.y = self.rect.y
                        self.vel.y = 0
                # Side collisions
                elif self.vel.x > 0 and self.rect.right > platform.rect.left:
                    if self.rect.right - platform.rect.left < 20:
                        self.rect.right = platform.rect.left
                        self.pos.x = self.rect.x
                        self.vel.x = 0
                elif self.vel.x < 0 and self.rect.left < platform.rect.right:
                    if platform.rect.right - self.rect.left < 20:
                        self.rect.left = platform.rect.right
                        self.pos.x = self.rect.x
                        self.vel.x = 0

        # Time hole collision (fall through)
        if time_holes:
            for hole in time_holes:
                if self.rect.colliderect(hole):
                    self.vel.y += 200 * dt  # Extra falling force

        # Update animation
        self.anim_timer += dt
        if self.anim_timer > 0.1:
            self.anim_timer = 0
            self.anim_frame = (self.anim_frame + 1) % 4

        # Flip sprite if facing left
        if self.facing == 'left':
            self.image = pygame.transform.flip(self.image, True, False)

    def reset(self, x, y):
        """Reset player position"""
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0, 0)
        self.rect.x = x
        self.rect.y = y
        self.on_ground = False
        self.state = 'idle'