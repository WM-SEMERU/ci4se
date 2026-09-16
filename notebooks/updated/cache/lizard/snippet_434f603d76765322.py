def validate_args(**args):
    if not args['query']:
        print('\nMissing required query argument.')
        sys.exit()
    for key in DEFAULTS:
        if key not in args:
            args[key] = DEFAULTS[key]
    return args