def ensure_one_opt(opt, parser, opt_list):
    the_one = None
    for name in opt_list:
        attr = name[2:].replace('-', '_')
        if hasattr(opt, attr) and getattr(opt, attr) is not None:
            if the_one is None:
                the_one = name
            else:
                parser.error('%s and %s are mutually exculsive' % (the_one,
                    name))
    if the_one is None:
        parser.error('you must supply one of the following %s' % ', '.join(
            opt_list))