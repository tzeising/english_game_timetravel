"""
Game settings and configuration
"""

# Window settings
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
TITLE = "The Time Guardian: Lila's Quest"
FPS = 60

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)
GOLD = (255, 215, 0)
RED = (220, 20, 60)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (147, 112, 219)
PINK = (255, 105, 180)
LILAC = (221, 160, 221)
BROWN = (139, 69, 19)

# Player settings
PLAYER_SPEED = 300  # pixels per second
# Jump power tuned so player can reach mid-level platforms
PLAYER_JUMP_POWER = -650
PLAYER_WIDTH = 32
PLAYER_HEIGHT = 48

# Physics
GRAVITY = 1500  # pixels per second squared
FRICTION = 0.85

# Enemy settings
ENEMY_SPEED = 100
ENEMY_WIDTH = 32
ENEMY_HEIGHT = 32

# Collectibles
STONE_SIZE = 16
PORTAL_WIDTH = 60
PORTAL_HEIGHT = 70

# UI settings
HUD_PADDING = 20
HEART_SIZE = 20
FONT_SIZE = 16
MENU_FONT_SIZE = 24

# Level settings
TILE_SIZE = 32
LEVEL_WIDTH = 2400
LEVEL_HEIGHT = 720

# Game mechanics
INITIAL_LIVES = 3
STONE_SCORE = 100
EXERCISE_SCORE = 100

# Asset paths
ASSETS_DIR = "assets"
GRAPHICS_DIR = f"{ASSETS_DIR}/graphics"
SOUNDS_DIR = f"{ASSETS_DIR}/sounds"
FONTS_DIR = f"{ASSETS_DIR}/fonts"
