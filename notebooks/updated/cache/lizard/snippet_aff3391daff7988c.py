def check_oneof(**kwargs):
    if not kwargs:
        return None
    not_nones = [val for val in kwargs.values() if val is not None]
    if len(not_nones) > 1:
        raise ValueError('Only one of {fields} should be set.'.format(
            fields=', '.join(sorted(kwargs.keys()))))