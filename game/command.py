class Command:
    def execute(self, game_state):
        raise NotImplementedError

class MoveUpCommand(Command):
    def execute(self, game_state):
        player = game_state.player
        game_state.entity_manager.set_component(player, "Velocity", dx=0, dy=-1)

class MoveDownCommand(Command):
    def execute(self, game_state):
        player = game_state.player
        game_state.entity_manager.set_component(player, "Velocity", dx=0, dy=1)
class MoveLeftCommand(Command):
    def execute(self, game_state):
        player = game_state.player
        game_state.entity_manager.set_component(player, "Velocity", dx=-1, dy=0)

class MoveRightCommand(Command):
    def execute(self, game_state):
        player = game_state.player
        game_state.entity_manager.set_component(player, "Velocity", dx=1, dy=0)
 

class QuitCommand(Command):
    def execute(self, game_state):
        raise SystemExit
        #game_state.quit()

COMMAND_REGISTRY = {
    "move_up": MoveUpCommand,
    "move_down": MoveDownCommand,
    "move_left": MoveLeftCommand,
    "move_right": MoveRightCommand,
    "quit": QuitCommand,
    # Map other actions to command classes...
}

def create_command(action_name):
    command_class = COMMAND_REGISTRY.get(action_name)
    if command_class:
        return command_class()
    else:
        raise ValueError(f"No command found for action: {action_name}")
