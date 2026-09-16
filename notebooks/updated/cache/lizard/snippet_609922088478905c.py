def draw(self, milliseconds, surface):
    if self.is_visible:
        global collidable_objects
        for obj in collidable_objects:
            if obj.is_visible:
                obj.draw(milliseconds, surface)
        super(CollisionManager, self).draw(milliseconds, surface)