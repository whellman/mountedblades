# game/game_state.py
import tcod
from ecs.entity_manager import EntityManager
from ecs.components.position_component import PositionComponent
from ecs.components.human_component import HumanComponent
from utilities.config_loader import ConfigLoader

class GameState:
    def __init__(self):
        self.entity_manager = EntityManager()
        self.create_human_test_entities()
        self.levels = self.load_levels()
        self.current_level = self.levels[0]  # Start at the first level

    def create_human_test_entities(self):
        entity_id = self.entity_manager.create_entity()
        self.entity_manager.add_component(entity_id, PositionComponent(x=10, y=10))
        self.entity_manager.add_component(entity_id, HumanComponent(name="Human", color=tcod.white))
    def load_levels(self):
        return ConfigLoader.load_levels()  # Load level data from JSON files

    def is_game_over(self):
        # Implement logic to check if the game is over
        return False
