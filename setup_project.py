import os

# Define folder structure
structure = [
    "game/states",
    "game/entities",
    "game/levels",
    "game/ui",
    "assets/graphics/characters",
    "assets/graphics/backgrounds",
    "assets/graphics/objects",
    "assets/graphics/ui",
    "assets/sounds",
    "assets/fonts",
    "utils"
]

# Define placeholder files
files = {
    "main.py": """import pygame\n\nif __name__ == '__main__':\n    pygame.init()\n    screen = pygame.display.set_mode((800, 600))\n    pygame.display.set_caption('English Game - Time Travel')\n    running = True\n    while running:\n        for event in pygame.event.get():\n            if event.type == pygame.QUIT:\n                running = False\n    pygame.quit()""",
    "requirements.txt": "pygame>=2.0.0",
    "README.md": "# English Game: Time Travel\n\nA time-travel grammar platformer featuring Lila.",
    "settings.py": "# Game configuration variables\nSCREEN_WIDTH = 800\nSCREEN_HEIGHT = 600",
    "utils/__init__.py": "",
    "utils/constants.py": "# Define global constants here",
    "utils/resources.py": "# Asset loading utilities",
    "utils/camera.py": "# Camera logic for scrolling levels",
    "game/__init__.py": "",
    "game/game.py": "# Main game class placeholder",
    "game/states/__init__.py": "",
    "game/states/menu_state.py": "# Menu state logic",
    "game/states/playing_state.py": "# Playing state logic",
    "game/states/cutscene_state.py": "# Cutscene logic",
    "game/states/exercise_state.py": "# Grammar exercise logic",
    "game/states/level_select_state.py": "# Level selection logic",
    "game/entities/__init__.py": "",
    "game/entities/player.py": "# Lila player class",
    "game/entities/enemy.py": "# Enemy logic",
    "game/entities/platform.py": "# Platform logic",
    "game/entities/time_stone.py": "# Collectible item logic",
    "game/entities/portal.py": "# Portal logic",
    "game/levels/__init__.py": "",
    "game/levels/level_manager.py": "# Level management logic",
    "game/levels/level1.py": "# Philadelphia 1776 level",
    "game/levels/level2.py": "# Civil War 1865 level",
    "game/levels/level3.py": "# Civil Rights 1963 level",
    "game/ui/__init__.py": "",
    "game/ui/hud.py": "# Heads-up display logic",
    "game/ui/menu.py": "# Menu components",
}

# Create folders
for folder in structure:
    os.makedirs(folder, exist_ok=True)

# Create files
for filepath, content in files.items():
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Project setup complete.")
