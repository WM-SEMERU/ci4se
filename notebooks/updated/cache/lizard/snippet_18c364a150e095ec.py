def _find_field(cls, field, doc):
    path = field.split('.')
    try:
        for key in path:
            doc = doc[key]
        return [(path, doc)]
    except (KeyError, TypeError):
        return []