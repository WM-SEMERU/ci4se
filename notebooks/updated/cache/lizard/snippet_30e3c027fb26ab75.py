def sort(x, axis=-1, reverse=False, with_index=False, only_index=False):
    from .function_bases import sort as sort_base
    n_outputs = 2 if with_index and not only_index else 1
    return sort_base(x, axis, reverse, with_index, only_index, n_outputs)