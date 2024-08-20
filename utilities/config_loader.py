# utilities/config_loader.py

import json

class ConfigLoader:
    @staticmethod
    def load_levels():
        # Load level data from JSON files
        with open('game/data/levels/level1.json', 'r') as file:
            level_data = json.load(file)
        return [level_data]  # Return a list of level data
