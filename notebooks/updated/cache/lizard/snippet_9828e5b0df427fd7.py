def create_entity(self, entity_type, term_ids, id=None):
    new_entity = Centity(type=self.type)
    if id is None:
        n = 1 if self.entity_layer is None else len(self.entity_layer.
            map_entity_id_to_node) + 1
        id = 'e{n}'.format(**locals())
    new_entity.set_id(id)
    new_entity.set_type(entity_type)
    references = Creferences()
    references.add_span(term_ids)
    new_entity.add_reference(references)
    self.add_entity(new_entity)
    return new_entity