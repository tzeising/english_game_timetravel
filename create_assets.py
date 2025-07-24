#!/usr/bin/env python3
"""
Create better placeholder assets for the game
"""

import os
import math

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Pillow is required to create assets.")
    print("Install with: pip install pillow")
    exit(1)


def create_lila_sprite():
    """Create a better Lila sprite with lilac hair and pink shirt"""
    img = Image.new('RGBA', (32, 48), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Hair (lilac) - rounded shape
    draw.ellipse([8, 2, 24, 22], fill=(221, 160, 221))

    # Hair strands
    draw.line([(10, 5), (8, 15)], fill=(200, 140, 200), width=1)
    draw.line([(22, 5), (24, 15)], fill=(200, 140, 200), width=1)

    # Face (peach)
    draw.ellipse([10, 8, 22, 22], fill=(255, 218, 185))

    # Eyes (white with blue iris)
    draw.ellipse([11, 13, 15, 17], fill=(255, 255, 255))
    draw.ellipse([17, 13, 21, 17], fill=(255, 255, 255))
    draw.ellipse([12, 14, 14, 16], fill=(74, 144, 226))
    draw.ellipse([18, 14, 20, 16], fill=(74, 144, 226))

    # Mouth
    draw.arc([13, 17, 19, 21], 0, 180, fill=(214, 139, 139), width=1)

    # Shirt (pink)
    draw.rectangle([8, 22, 24, 34], fill=(255, 105, 180))
    draw.rectangle([4, 24, 28, 32], fill=(255, 105, 180))

    # Arms
    draw.rectangle([2, 24, 6, 34], fill=(255, 218, 185))
    draw.rectangle([26, 24, 30, 34], fill=(255, 218, 185))

    # Pants (dark blue)
    draw.rectangle([10, 34, 22, 44], fill=(44, 62, 80))

    # Shoes (black)
    draw.rectangle([10, 44, 15, 48], fill=(0, 0, 0))
    draw.rectangle([17, 44, 22, 48], fill=(0, 0, 0))

    img.save('assets/graphics/characters/lila_idle.png')
    print("✓ Created Lila sprite")


def create_enemy_sprite():
    """Create red coat enemy sprite"""
    img = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Hat (tricorn)
    draw.polygon([(8, 0), (24, 0), (26, 6), (6, 6)], fill=(139, 0, 0))
    draw.rectangle([6, 5, 26, 8], fill=(139, 0, 0))

    # Head
    draw.ellipse([10, 4, 22, 16], fill=(255, 218, 185))

    # Eyes
    draw.rectangle([11, 8, 14, 11], fill=(255, 255, 255))
    draw.rectangle([18, 8, 21, 11], fill=(255, 255, 255))
    draw.rectangle([12, 9, 13, 10], fill=(0, 0, 0))
    draw.rectangle([19, 9, 20, 10], fill=(0, 0, 0))

    # Body (red coat)
    draw.rectangle([8, 16, 24, 28], fill=(220, 20, 60))

    # Arms
    draw.rectangle([4, 18, 8, 28], fill=(220, 20, 60))
    draw.rectangle([24, 18, 28, 28], fill=(220, 20, 60))

    # Musket
    draw.rectangle([26, 10, 28, 26], fill=(101, 67, 33))
    draw.rectangle([26, 10, 28, 14], fill=(192, 192, 192))

    img.save('assets/graphics/characters/enemy_redcoat.png')
    print("✓ Created enemy sprite")


def create_time_stone():
    """Create animated time stone"""
    img = Image.new('RGBA', (40, 40), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Outer glow
    for i in range(8, 0, -1):
        alpha = int(255 * (1 - i / 8) * 0.3)
        color = (255, 215, 0, alpha)
        draw.ellipse([20 - i * 2, 20 - i * 2, 20 + i * 2, 20 + i * 2], fill=color)

    # Main diamond
    draw.polygon([(20, 8), (32, 20), (20, 32), (8, 20)], fill=(255, 215, 0))

    # Inner light
    draw.polygon([(20, 14), (26, 20), (20, 26), (14, 20)], fill=(255, 255, 200))

    img.save('assets/graphics/objects/time_stone.png')
    print("✓ Created time stone")


def create_platforms():
    """Create platform textures"""
    # Cobblestone
    img = Image.new('RGBA', (128, 32), (105, 105, 105))
    draw = ImageDraw.Draw(img)

    # Draw stone pattern
    for y in range(0, 32, 8):
        for x in range(0, 128, 16):
            offset = 8 if (y // 8) % 2 else 0
            draw.rectangle([x + offset, y, x + offset + 15, y + 7],
                           outline=(84, 84, 84), width=1)

    img.save('assets/graphics/objects/platform_cobblestone.png')
    print("✓ Created cobblestone platform")

    # Wood platform
    img = Image.new('RGBA', (128, 20), (139, 69, 19))
    draw = ImageDraw.Draw(img)

    # Wood grain
    for x in range(0, 128, 8):
        color = (101, 67, 33) if x % 16 == 0 else (120, 60, 20)
        draw.line([(x, 0), (x + 3, 20)], fill=color, width=1)

    img.save('assets/graphics/objects/platform_wood.png')
    print("✓ Created wood platform")


def create_portal():
    """Create portal sprites"""
    # Locked portal
    img = Image.new('RGBA', (60, 70), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Frame
    draw.rectangle([0, 0, 60, 70], fill=(51, 51, 51))
    draw.rectangle([5, 5, 55, 65], fill=(102, 102, 102))
    draw.rectangle([10, 10, 50, 60], fill=(0, 0, 0))

    # Lock
    draw.ellipse([25, 25, 35, 35], fill=(255, 215, 0))
    draw.arc([22, 18, 38, 34], 0, 180, fill=(255, 215, 0), width=3)

    img.save('assets/graphics/objects/portal_locked.png')
    print("✓ Created locked portal")

    # Open portal
    img = Image.new('RGBA', (60, 70), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Swirling effect
    for i in range(5):
        alpha = 255 - i * 40
        color = (147, 112, 219, alpha)
        draw.ellipse([i * 3, i * 4, 60 - i * 3, 70 - i * 4], fill=color)

    # Center bright spot
    draw.ellipse([20, 25, 40, 45], fill=(255, 255, 255, 200))

    img.save('assets/graphics/objects/portal_open.png')
    print("✓ Created open portal")


def create_ui_elements():
    """Create UI elements"""
    # Button normal
    img = Image.new('RGBA', (200, 50), (139, 69, 19))
    draw = ImageDraw.Draw(img)
    draw.rectangle([2, 2, 198, 48], fill=(160, 82, 45))
    draw.rectangle([4, 4, 196, 46], fill=(139, 69, 19))
    img.save('assets/graphics/ui/button_normal.png')

    # Button hover
    img = Image.new('RGBA', (200, 50), (255, 215, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle([2, 2, 198, 48], fill=(255, 235, 100))
    draw.rectangle([4, 4, 196, 46], fill=(255, 215, 0))
    img.save('assets/graphics/ui/button_hover.png')

    print("✓ Created UI buttons")


def create_background_objects():
    """Create background decoration objects"""
    # Colonial building
    img = Image.new('RGBA', (80, 60), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Building
    draw.rectangle([0, 20, 80, 60], fill=(139, 69, 19))

    # Roof
    draw.polygon([(0, 20), (40, 0), (80, 20)], fill=(101, 67, 33))

    # Windows
    for x in [15, 45]:
        draw.rectangle([x, 30, x + 15, 45], fill=(70, 130, 180))
        draw.line([(x + 7, 30), (x + 7, 45)], fill=(255, 255, 255), width=1)
        draw.line([(x, 37), (x + 15, 37)], fill=(255, 255, 255), width=1)

    # Door
    draw.rectangle([32, 40, 48, 60], fill=(101, 67, 33))

    img.save('assets/graphics/objects/colonial_building.png')
    print("✓ Created colonial building")

    # Liberty Bell
    img = Image.new('RGBA', (40, 50), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Support
    draw.rectangle([5, 0, 35, 10], fill=(101, 67, 33))

    # Bell
    draw.ellipse([5, 5, 35, 40], fill=(255, 215, 0))
    draw.rectangle([5, 35, 35, 45], fill=(255, 215, 0))

    # Crack
    draw.line([(20, 10), (22, 25), (18, 40)], fill=(0, 0, 0), width=2)

    img.save('assets/graphics/objects/liberty_bell.png')
    print("✓ Created Liberty Bell")


def create_menu_background():
    """Create menu background"""
    img = Image.new('RGBA', (1280, 720), (135, 206, 235))
    draw = ImageDraw.Draw(img)

    # Gradient sky
    for y in range(720):
        color_r = int(135 + (y / 720) * 60)
        color_g = int(206 - (y / 720) * 50)
        color_b = int(235 - (y / 720) * 50)
        draw.line([(0, y), (1280, y)], fill=(color_r, color_g, color_b))

    # Clouds
    for i in range(8):
        x = 100 + i * 150
        y = 50 + (i % 3) * 100
        draw.ellipse([x - 40, y - 20, x + 40, y + 20], fill=(255, 255, 255, 180))
        draw.ellipse([x - 60, y - 15, x - 20, y + 15], fill=(255, 255, 255, 150))
        draw.ellipse([x + 20, y - 15, x + 60, y + 15], fill=(255, 255, 255, 150))

    img.save('assets/graphics/ui/menu_background.png')
    print("✓ Created menu background")


def main():
    """Create all assets"""
    print("=== Creating Game Assets ===\n")

    # Check directories exist
    if not os.path.exists('assets/graphics/characters'):
        print("ERROR: Run setup_project.py first!")
        return

    print("Creating character sprites...")
    create_lila_sprite()
    create_enemy_sprite()

    print("\nCreating objects...")
    create_time_stone()
    create_platforms()
    create_portal()

    print("\nCreating UI elements...")
    create_ui_elements()

    print("\nCreating background objects...")
    create_background_objects()
    create_menu_background()

    print("\n✓ All placeholder assets created!")
    print("You can now replace these with your own artwork.")


if __name__ == "__main__":
    main()