# game/game_state.py
import tcod
from ecs.entity_manager import EntityManager
from ecs.components.position_component import PositionComponent
from ecs.components.human_component import HumanComponent
from ecs.components.health_component import HealthComponent
from ecs.components.velocity_component import VelocityComponent
from utilities.config_loader import ConfigLoader

#gamestate.player is a player with player.move

class GameState:
    def __init__(self):
        self.entity_manager = EntityManager()

        self.player = self.entity_manager.create_entity()
        self.entity_manager.add_component(self.player, PositionComponent(x= 30, y= 10))
        self.entity_manager.add_component(self.player, HumanComponent(name="Player", color=tcod.red))
        self.entity_manager.add_component(self.player, HealthComponent(hp= 100))
        self.entity_manager.add_component(self.player, VelocityComponent(dx= 0, dy= 0))
        
        self.create_human_test_entities()
        self.levels = self.load_levels()
        self.current_level = self.levels[0]  # Start at the first level

    def create_human_test_entities(self):
        entity_id = self.entity_manager.create_entity()
        self.entity_manager.add_component(entity_id, PositionComponent(x=10, y=10))
        self.entity_manager.add_component(entity_id, HumanComponent(name="Human", color=tcod.white))
        self.entity_manager.add_component(entity_id, VelocityComponent(dx= 0, dy= 0))
                                          
        ent2 = self.entity_manager.create_entity()
        self.entity_manager.add_component(ent2, PositionComponent(x=20, y=20))
        self.entity_manager.add_component(ent2, HumanComponent(name="Human", color=tcod.cyan))
        self.entity_manager.add_component(ent2, VelocityComponent(dx= 0, dy= 0))                                  
    def load_levels(self):
        return ConfigLoader.load_levels()  # Load level data from JSON files

    def is_game_over(self):
        # Implement logic to check if the game is over
        return False
