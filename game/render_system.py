# game/render_system.py

import tcod

class RenderSystem:
    def __init__(self, console):
        self.console = console

    def render(self, game_state):
        for entity in game_state.entity_manager.entities:
            human = game_state.entity_manager.get_component(entity, "Human")
            position = game_state.entity_manager.get_component(entity, "Position")
            if human and position:
                self.draw_entity(position, human)
            if entity == game_state.player:
                self.draw_entity(position, game_state.entity_manager.get_component(entity, "Player"))
                

    def draw_entity(self, position, human):
        # Example: Draw a simple character or rectangle
        self.console.print(x=position.x, y=position.y, string='@', fg=human.color)
        # Alternatively, use tcod functions to draw shapes or images
