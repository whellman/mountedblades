# ecs/entity_manager.py

class EntityManager:
    def __init__(self):
        self.entities = []

    def create_entity(self):
        entity_id = len(self.entities)
        self.entities.append({})
        return entity_id

    def add_component(self, entity_id, component):
        self.entities[entity_id][component.name] = component

    def get_component(self, entity_id, component_name):
        return self.entities[entity_id].get(component_name)
