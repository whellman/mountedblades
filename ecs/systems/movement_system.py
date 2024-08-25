# ecs/systems/movement_system.py

class MovementSystem:
    def update(game_state):
        for entity in game_state.entity_manager.entities:
            position = game_state.entity_manager.get_component(entity, "Position")
            velocity = game_state.entity_manager.get_component(entity, "Velocity")

            if position and velocity:
                newx = position.x + velocity.dx
                newy = position.y + velocity.dy
                # Add collision detection, boundaries, etc.
                
                # FIXME: hardcoding the world boundaries. Fix this by
                # passing the world size to the game state on creation
                # so that all relevant methods can see it.
                if newx > 80:
                    newx -= 80
                if newy > 50:
                    newy -= 50
                if newx < 0:
                    newx += 80
                if newy < 0:
                    newy += 50
                game_state.entity_manager.set_component(entity, "Position", x=newx, y=newy)
