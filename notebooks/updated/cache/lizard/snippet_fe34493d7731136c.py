def parse(constraints):
    if not constraints:
        return None
    if type(constraints) is dict:
        return constraints
    constraints = {normalize_key(k): (normalize_list_value(v) if k in
        LIST_KEYS else normalize_value(v)) for k, v in [s.split('=') for s in
        constraints.split(' ')]}
    return constraints