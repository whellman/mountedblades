# game/time_system.py

# time system needs to handle any time effects.
# damage over time bleeding, poision maybe, etc.

# but for now, just the movement function that
# transforms velocity into position
import random

from ecs.systems.movement_system import MovementSystem

class TimeSystem:
#    def __init__(self):
#        movement_system = MovementSystem()

    def advance_time(self, game_state):
        # for now, we simply apply the velocity to the position
        # in order to account for the movement of entities
        for entity in game_state.entity_manager.entities:
            human = game_state.entity_manager.get_component(entity, "Human")
            position = game_state.entity_manager.get_component(entity, "Position")
            if human and position:
                game_state.entity_manager.set_component(entity, "Velocity", dx=random.randint(-1, 1), dy=random.randint(-1, 1))
        MovementSystem.update(game_state)
        
