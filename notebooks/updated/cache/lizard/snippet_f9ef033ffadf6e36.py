def _make_entities_from_ids(entity_cls, entity_objs_and_ids, server_config):
    return [_make_entity_from_id(entity_cls, entity_or_id, server_config) for
        entity_or_id in entity_objs_and_ids]