# game/game_state.py

from ecs.entity_manager import EntityManager
from utilities.config_loader import ConfigLoader

class GameState:
    def __init__(self):
        self.entity_manager = EntityManager()
        self.levels = self.load_levels()
        self.current_level = self.levels[0]  # Start at the first level

    def load_levels(self):
        return ConfigLoader.load_levels()  # Load level data from JSON files

    def is_game_over(self):
        # Implement logic to check if the game is over
        return False
