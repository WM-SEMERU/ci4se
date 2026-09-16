def _is_pair(item):
    return isinstance(item, (list, tuple, set)) and len(item
        ) == 2 and not isinstance(item[0], (list, tuple, set)
        ) and not isinstance(item[1], (list, tuple, set))