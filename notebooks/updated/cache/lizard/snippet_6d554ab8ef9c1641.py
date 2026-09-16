def query_all_collisions(collision_object):
    global collidable_objects
    colliding = []
    for obj in collidable_objects:
        if obj is not collision_object:
            if collision_object.is_colliding(obj):
                colliding.append(obj)
    return colliding