# main.py

from __future__ import annotations

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

import random

from utilities.color_utils import ensure_contrast

#from game.game_loop import GameLoop
from game.game_state import GameState
from game.input_handler import InputHandler
from game.render_system import RenderSystem
from game.time_system import TimeSystem

def main():
    # Initialize game systems
    screen_width, screen_height = 80, 50

    tileset = tcod.tileset.load_tilesheet(
        "game/data/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
    )
    tcod.tileset.procedural_block_elements(tileset=tileset)

    root_console = tcod.console.Console(screen_width, screen_height)
    

    
    # Initialize the game state
    game_state = GameState()
    input_handler = InputHandler()
    render_system = RenderSystem(root_console)
    time_system = TimeSystem()


    # console.print(0, 0, "Mounted Blades")

    with tcod.context.new(console=root_console, tileset=tileset) as context:
        while not game_state.is_game_over():
            # 1 capture input
            commands = input_handler.handle_input()
            # 2 process player commands
            for command in commands:
                command.execute(game_state)
            # 3 update game state
            time_system.advance_time(game_state)
            # this hardcoded dumb thing is a standin for actual time. Its very philosophical like that.
            #for entity in game_state.entity_manager.entities:
            #    human = game_state.entity_manager.get_component(entity, "Human")
            #    position = game_state.entity_manager.get_component(entity, "Position")
            #    if human and position:
            #        newx = position.x + (random.randint(-1, 1))
            #        newy = position.y + (random.randint(-1, 1))
            #        if newx > screen_width: # 80
            #            newx = 0
            #        if newy > screen_height: # 50
            #            newy = 0
            #        if newx < 0:
            #            newx = screen_width
            #        if newy < 0:
            #            newy = screen_height
                    
            #        game_state.entity_manager.set_component(entity, "Position", x=newx, y=newy)
             #       print("eh")

            
            # 4 render the current state
            root_console.clear() # hm
            render_system.render(game_state)
            context.present(root_console)
            #tcod.console_flush() # hm
            


if __name__ == "__main__":
    main()
