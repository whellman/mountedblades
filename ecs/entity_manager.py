# ecs/entity_manager.py


class EntityManager:
    def __init__(self):
        # Initialize the entity manager with an empty dictionary to hold entities and their components
        self.entities = {}
        self.next_entity_id = 0  # Used to assign unique IDs to new entities

    def create_entity(self):
        """
        Creates a new entity and returns its unique ID.
        """
        entity_id = self.next_entity_id
        self.entities[entity_id] = {}  # Initialize an empty dictionary for the entity's components
        self.next_entity_id += 1
        return entity_id

    def add_component(self, entity_id, component):
        """
        Adds or updates a component for the given entity.
        """
        if entity_id not in self.entities:
            raise ValueError(f"Entity {entity_id} does not exist.")
        self.entities[entity_id][component.name] = component

    def get_component(self, entity_id, component_name):
        """
        Retrieves a component by name from the specified entity.
        """
        return self.entities.get(entity_id, {}).get(component_name)

    def set_component(self, entity_id, component_name, **kwargs):
        """
        Updates specific attributes of an existing component.
        """
        component = self.get_component(entity_id, component_name)
        if component:
            for key, value in kwargs.items():
                setattr(component, key, value)
        else:
            raise ValueError(f"Component {component_name} not found for entity {entity_id}")

    def remove_component(self, entity_id, component_name):
        """
        Removes a component from the specified entity.
        """
        if entity_id in self.entities and component_name in self.entities[entity_id]:
            del self.entities[entity_id][component_name]

    def remove_entity(self, entity_id):
        """
        Removes an entity and all of its components.
        """
        if entity_id in self.entities:
            del self.entities[entity_id]
        else:
            raise ValueError(f"Entity {entity_id} does not exist.")
