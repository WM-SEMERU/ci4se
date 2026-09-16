def copy_params(get_or_post_params, ignore=None):
    if ignore is None:
        ignore = set()
    params = {}
    for key in get_or_post_params:
        if key not in ignore and get_or_post_params[key]:
            params[key] = get_or_post_params[key]
    return params