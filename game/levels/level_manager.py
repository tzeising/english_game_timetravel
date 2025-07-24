"""
Level Manager - handles loading and managing level data
"""

from .level1 import LEVEL_1
from .level2 import LEVEL_2
from .level3 import LEVEL_3


class LevelManager:
    def __init__(self):
        self.levels = {
            1: LEVEL_1,
            2: LEVEL_2,
            3: LEVEL_3
        }

    def get_level(self, level_num):
        """Get level data by number"""
        return self.levels.get(level_num, LEVEL_1)

    def get_level_count(self):
        """Get total number of levels"""
        return len(self.levels)