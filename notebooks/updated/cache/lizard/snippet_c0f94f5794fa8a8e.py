def assumption_list_string(assumptions, assumption_dict):
    if isinstance(assumptions, six.string_types):
        raise TypeError(
            'assumptions must be an iterable of strings, not a string itself')
    for a in assumptions:
        if a not in assumption_dict.keys():
            raise ValueError('{} not present in assumption_dict'.format(a))
    assumption_strings = [assumption_dict[a] for a in assumptions]
    return strings_to_list_string(assumption_strings)