def expand_dict_as_keys(d):
    to_product = []
    for key, values in sorted(d.items()):
        key_values = sorted([(key, v) for v in utils.ensure_listable(values
            ) if v is not None])
        if key_values:
            to_product.append(key_values)
    return list(itertools.product(*to_product))