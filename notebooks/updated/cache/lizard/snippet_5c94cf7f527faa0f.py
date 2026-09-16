def _grouper(iterable, n_args, fillvalue=None):
    args = [iter(iterable)] * n_args
    return zip_longest(*args, fillvalue=fillvalue)