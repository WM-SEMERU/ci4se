def _get_col_items(mapping):
    from .variable import IndexVariable
    col_items = []
    for k, v in mapping.items():
        col_items.append(k)
        var = getattr(v, 'variable', v)
        if isinstance(var, IndexVariable):
            level_names = var.to_index_variable().level_names
            if level_names is not None:
                col_items += list(level_names)
    return col_items