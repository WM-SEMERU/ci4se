def replace(self, scaling_group, name, cooldown, min_entities, max_entities,
    metadata=None):
    return self._manager.replace(scaling_group, name, cooldown,
        min_entities, max_entities, metadata=metadata)