# ecs/entity_manager.py

class EntityManager:
    def __init__(self):
        self.entities = {}

    def create_entity(self):
        entity_id = len(self.entities)
        self.entities.append({})
        return entity_id

    def add_component(self, entity_id, component):
        if entity_id not in self.entities:
            self.entities[entity_id] = {}
        self.entities[entity_id][component.name] = component

    def get_component(self, entity_id, component_name):
        return self.entities.get(entity_id, {}).get(component_name)

    def set_component(self, entity_id, component_name, **kwargs):
        component = self.get_component(entity_id, component_name)
        if component:
            for key, value in kwargs.items():
                setattr(component, key, value)
        else:
            raise ValueError(f"Component {component_name} not found for entity {entity_id}")
