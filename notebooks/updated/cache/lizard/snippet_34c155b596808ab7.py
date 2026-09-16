def _find_update_fields(cls, field, doc):

    def find_partial_matches():
        for key in doc:
            if len(key) > len(field):
                if key.startswith(field) and key[len(field)] == '.':
                    yield [key], doc[key]
            elif len(key) < len(field):
                if field.startswith(key) and field[len(key)] == '.':
                    matched = cls._find_field(field[len(key) + 1:], doc[key])
                    if matched:
                        match = matched[0]
                        match[0].insert(0, key)
                        yield match
                    return
    try:
        return [([field], doc[field])]
    except KeyError:
        return list(find_partial_matches())