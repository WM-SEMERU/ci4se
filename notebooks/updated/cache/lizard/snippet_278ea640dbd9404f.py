def _nest_vars_in_rec(var_items, rec_items, input_order, items_by_key, parallel
    ):
    num_items = var_items
    var_items = list(var_items)[0]
    if rec_items:
        rec_items = list(rec_items)[0]
        if rec_items == 1 and var_items > 1 or parallel.startswith('batch'):
            num_items = set([rec_items])
            for var_key in (k for k, t in input_order.items() if t != 'record'
                ):
                var_key = tuple(var_key.split('__'))
                items_by_key[var_key] = [items_by_key[var_key]] * rec_items
        else:
            assert var_items == rec_items, (var_items, rec_items)
    return items_by_key, num_items