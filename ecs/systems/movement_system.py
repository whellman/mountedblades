# ecs/systems/movement_system.py

class MovementSystem:
    def update(self, game_state):
        for entity in game_state.entity_manager.entities:
            position = entity.get("Position")
            velocity = entity.get("Velocity")

            if position and velocity:
                position.x += velocity.dx
                position.y += velocity.dy
                # Add collision detection, boundaries, etc.
