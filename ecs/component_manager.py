# ecs/component_manager.py

class ComponentManager:
    def __init__(self):
        self.components = {}

    def add_component(self, entity_id, component):
        self.components.setdefault(entity_id, []).append(component)

    def get_components(self, entity_id):
        return self.components.get(entity_id, [])
