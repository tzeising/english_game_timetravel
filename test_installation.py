#!/usr/bin/env python3
"""
Test installation - verify all dependencies are installed correctly
"""

import sys


def test_imports():
    """Test if all required modules can be imported"""
    print("Testing Python version...")
    print(f"Python {sys.version}")

    if sys.version_info < (3, 8):
        print("ERROR: Python 3.8+ required!")
        return False

    print("\nTesting imports...")

    try:
        import pygame
        print(f"✓ Pygame {pygame.version.ver} installed")
    except ImportError:
        print("✗ Pygame not installed - run: pip install pygame")
        return False

    try:
        import pygame_menu
        print("✓ Pygame-menu installed")
    except ImportError:
        print("✗ Pygame-menu not installed - run: pip install pygame-menu")
        return False

    try:
        from PIL import Image
        print("✓ Pillow installed")
    except ImportError:
        print("✗ Pillow not installed - run: pip install pillow")
        return False

    return True


def test_pygame():
    """Test basic Pygame functionality"""
    print("\nTesting Pygame initialization...")
    try:
        import pygame
        pygame.init()

        # Test display
        test_surface = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Installation Test")

        # Test font
        font = pygame.font.Font(None, 24)

        # Test clock
        clock = pygame.time.Clock()

        # Run for a brief moment
        for i in range(30):
            test_surface.fill((135, 206, 235))  # Sky blue

            text = font.render("Installation Successful!", True, (255, 255, 255))
            text_rect = text.get_rect(center=(320, 240))
            test_surface.blit(text, text_rect)

            pygame.display.flip()
            clock.tick(30)

        pygame.quit()
        print("✓ Pygame working correctly")
        return True

    except Exception as e:
        print(f"✗ Pygame error: {e}")
        return False


def test_game_structure():
    """Test if game files are in place"""
    print("\nTesting game structure...")

    required_files = [
        'main.py',
        'settings.py',
        'requirements.txt',
        'game/game.py',
        'game/entities/player.py',
        'game/states/menu_state.py',
        'game/levels/level1.py'
    ]

    import os
    all_present = True

    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ {file} missing!")
            all_present = False

    return all_present


def main():
    """Run all tests"""
    print("=== The Time Guardian Installation Test ===\n")

    tests_passed = True

    if not test_imports():
        tests_passed = False

    if not test_pygame():
        tests_passed = False

    if not test_game_structure():
        tests_passed = False

    print("\n" + "=" * 40)
    if tests_passed:
        print("✓ All tests passed! You can run the game with: python main.py")
    else:
        print("✗ Some tests failed. Please install missing dependencies.")
        print("Run: pip install -r requirements.txt")

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()