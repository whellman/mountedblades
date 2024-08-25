# game/input_handler.py

import tcod
from game.command import create_command

class InputHandler:
    def handle_input(self):
        # List of commands to return
        commands = []

        # Poll for an event from the API
        for event in tcod.event.wait(): #changed get to wait
            if event.type == "KEYDOWN":
                if event.sym == tcod.event.K_UP:
                    commands.append(create_command("move_up"))
                elif event.sym == tcod.event.K_DOWN:
                    commands.append(create_command("move_down"))
                elif event.sym == tcod.event.K_LEFT:
                    commands.append(create_command("move_left"))
                elif event.sym == tcod.event.K_RIGHT:
                    commands.append(create_command("move_right"))
                elif event.sym == tcod.event.K_ESCAPE:
                    commands.append(create_command("quit"))
                # Handle other keys...

            elif isinstance(event, tcod.event.Quit): #event.type == "QUIT":
                commands.append(create_command("quit"))
                #raise SystemExit

        return commands
#
#            for event in tcod.event.wait(): #event loop, blocks until pending events EXIST
#                print(event)
#                if isinstance(event, tcod.event.Quit):
#                    raise SystemExit
