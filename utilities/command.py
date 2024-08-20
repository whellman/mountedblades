# utilities/command.py

class Command:
    def __init__(self, raw_command):
        self.raw_command = raw_command

    def execute(self, game_state):
        # Implement command execution logic
        print(f"Executing command: {self.raw_command}")
