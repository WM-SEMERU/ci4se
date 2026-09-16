def create_was_derived_from_relation(self, used_entity_id, used_entity_kind,
    generated_entity_id, generated_entity_kind):
    data = {'used_entity': {'id': used_entity_id, 'kind': used_entity_kind},
        'generated_entity': {'id': generated_entity_id, 'kind':
        generated_entity_kind}}
    return self._post('/relations/was_derived_from', data)