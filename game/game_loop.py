# game/game_loop.py

from game.input_handler import InputHandler
from game.render_system import RenderSystem
from ecs.systems.movement_system import MovementSystem
from ecs.systems.combat_system import CombatSystem

class GameLoop:
    def __init__(self, game_state):
        self.game_state = game_state
        self.input_handler = InputHandler()
        self.render_system = RenderSystem()

        # Initialize systems
        self.systems = [
            MovementSystem(),
            CombatSystem(),
            # Add more systems as needed
        ]

    def run(self):
        while not self.game_state.is_game_over():
            # Process input
            commands = self.input_handler.handle_input()
            for command in commands:
                command.execute(self.game_state)

            # Update game state
            for system in self.systems:
                system.update(self.game_state)

            # Render the game state
            self.render_system.render(self.game_state)
