def ensure_unique(qs, field_name, value, exclude_id=None):
    orig = value
    if not value:
        value = 'None'
    for x in itertools.count(1):
        if not qs.exclude(id=exclude_id).filter(**{field_name: value}).exists(
            ):
            break
        if orig:
            value = '%s-%d' % (orig, x)
        else:
            value = '%d' % x
    return value