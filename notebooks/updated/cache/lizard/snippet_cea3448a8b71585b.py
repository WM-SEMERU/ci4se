def dumps(data, ac_parser=None, **options):
    psr = find(None, forced_type=ac_parser)
    return psr.dumps(data, **options)