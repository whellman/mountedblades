# main.py

from __future__ import annotations

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset


from game.game_loop import GameLoop
from game.game_state import GameState

def main():
    # Initialize the game state
    game_state = GameState()

    #Load a tileset and open a window using it, this window will immediately close.
    tileset = tcod.tileset.load_tilesheet(
        "game/data/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
    )

    tcod.tileset.procedural_block_elements(tileset=tileset)
    console = tcod.console.Console(80, 50)
    console.print(0, 0, "Mounted Blades")
    console.print(1, 2, "a Game of Lance and Horse")
    console.print(2, 4, "@ -----> l l l l")
    with tcod.context.new(console=console, tileset=tileset) as context:
        while True:
            context.present(console) # render the console to the window and show it (presenting it to the player, that is to say)
            for event in tcod.event.wait(): #event loop, blocks until pending events EXIST
                print(event)
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit
        #game_loop = GameLoop(game_state)
        #game_loop.run()

    # Create and start the main game loop

if __name__ == "__main__":
    main()
