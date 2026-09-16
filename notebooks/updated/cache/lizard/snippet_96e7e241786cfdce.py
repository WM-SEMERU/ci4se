def combine_lists(d, keys=None, deepcopy=True):
    if isinstance(d, list):
        init_list = True
        d = {'dummy_key843': d}
    else:
        init_list = False
    flattened = flatten(d, list_of_dicts=None)
    for key, value in list(flattened.items()):
        if keys is not None:
            try:
                if not key[-1] in keys:
                    continue
            except Exception:
                continue
        if not isinstance(value, list):
            continue
        if not all([is_dict_like(d) for d in value]):
            continue
        newd = {}
        for subdic in value:
            for subk, subv in subdic.items():
                if subk not in newd:
                    newd[subk] = []
                newd[subk].append(subv)
        flattened[key] = newd
    final = unflatten(flattened, list_of_dicts=None, deepcopy=deepcopy)
    if init_list:
        return list(final.values())[0]
    else:
        return final