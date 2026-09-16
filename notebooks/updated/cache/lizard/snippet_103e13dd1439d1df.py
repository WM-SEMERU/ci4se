def related_model(self):
    relationship_field = self.name
    if relationship_field not in get_relationships(self.schema):
        raise InvalidFilters('{} has no relationship attribute {}'.format(
            self.schema.__name__, relationship_field))
    return getattr(self.model, get_model_field(self.schema, relationship_field)
        ).property.mapper.class_