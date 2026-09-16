def verify_processing_options(opt, parser):
    scheme_types = scheme_prefix.values()
    if opt.processing_scheme.split(':')[0] not in scheme_types:
        parser.error('(%s) is not a valid scheme type.')