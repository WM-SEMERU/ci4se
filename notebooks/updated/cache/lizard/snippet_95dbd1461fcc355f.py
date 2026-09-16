def _map_relation(c, language='any'):
    label = c.label(language)
    return {'id': c.id, 'type': c.type, 'uri': c.uri, 'label': label.label if
        label else None}