def remove_entities(status, entitylist):
    try:
        entities = status.entities
        text = status.text
    except AttributeError:
        entities = status.get('entities', dict())
        text = status['text']
    indices = [ent['indices'] for etype, entval in list(entities.items()) for
        ent in entval if etype in entitylist]
    indices.sort(key=lambda x: x[0], reverse=True)
    for start, end in indices:
        text = text[:start] + text[end:]
    return text