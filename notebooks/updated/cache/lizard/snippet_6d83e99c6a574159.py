def _expand_rec_to_vars(var_items, rec_items, input_order, items_by_key,
    parallel):
    num_items = var_items
    var_items = list(var_items)[0]
    if rec_items:
        for rec_key in (k for k, t in input_order.items() if t == 'record'):
            rec_vals = items_by_key[rec_key]
            if len(rec_vals) == 1 and var_items > 1:
                items_by_key[rec_key] = rec_vals * var_items
            else:
                assert var_items == len(rec_vals), (var_items, rec_vals)
    return items_by_key, num_items