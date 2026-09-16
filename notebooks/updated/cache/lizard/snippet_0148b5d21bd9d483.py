def check_views(view_set, max_views=3):
    if not isinstance(view_set, Iterable):
        view_set = tuple([view_set])
    if len(view_set) > max_views:
        raise ValueError('Can only have {} views'.format(max_views))
    return [check_int(view, 'view', min_value=0, max_value=max_views - 1) for
        view in view_set]