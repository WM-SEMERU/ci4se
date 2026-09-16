def normalize_options(options):
    normalized_options = []

    def _add(option, arg=None):
        normalized_options.append(option)
        arg and normalized_options.append(arg)
    for option, arg in options.viewitems():
        prefixed_option = Build.prefix_option(option)
        if isinstance(arg, list) and arg:
            for a in arg:
                _add(prefixed_option, a)
        else:
            _add(prefixed_option, arg)
    return normalized_options