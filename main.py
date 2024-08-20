# main.py

from __future__ import annotations

from game.game_loop import GameLoop
from game.game_state import GameState

def main():
    # Initialize the game state
    game_state = GameState()

    # Create and start the main game loop
    game_loop = GameLoop(game_state)
    game_loop.run()

if __name__ == "__main__":
    main()
