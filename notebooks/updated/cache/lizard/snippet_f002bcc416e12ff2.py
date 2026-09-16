def upload_entities_tsv(namespace, workspace, entities_tsv):
    if isinstance(entities_tsv, string_types):
        with open(entities_tsv, 'r') as tsv:
            entity_data = tsv.read()
    elif isinstance(entities_tsv, io.StringIO):
        entity_data = entities_tsv.getvalue()
    else:
        raise ValueError('Unsupported input type.')
    return upload_entities(namespace, workspace, entity_data)