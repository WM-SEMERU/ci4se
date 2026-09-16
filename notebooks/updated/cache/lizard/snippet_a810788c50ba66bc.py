def unregister(self, entity_class, entity):
    EntityState.release(entity, self)
    self.__entity_set_map[entity_class].remove(entity)