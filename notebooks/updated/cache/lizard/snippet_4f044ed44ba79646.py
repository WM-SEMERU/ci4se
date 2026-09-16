def split_levels(fields):
    first_level_fields = []
    next_level_fields = {}
    if not fields:
        return first_level_fields, next_level_fields
    if not isinstance(fields, list):
        fields = [a.strip() for a in fields.split(',') if a.strip()]
    for e in fields:
        if '.' in e:
            first_level, next_level = e.split('.', 1)
            first_level_fields.append(first_level)
            next_level_fields.setdefault(first_level, []).append(next_level)
        else:
            first_level_fields.append(e)
    first_level_fields = list(set(first_level_fields))
    return first_level_fields, next_level_fields