def get_component(self, entity, component_type, missing=MISSING):
    relation = self._get_relation(component_type)
    if entity not in relation:
        if missing is MISSING:
            raise NoSuchComponentError()
        else:
            return missing
    return relation[entity]