def filter_from_options(key, options):
    return anyconfig.utils.filter_options([k for k in options.keys() if k !=
        key], options)