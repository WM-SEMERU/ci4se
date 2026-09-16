def convert_to_scl(spec, scl_options):
    scl_options['skip_functions'] = scl_options['skip_functions'].split(',')
    scl_options['meta_spec'] = None
    convertor = SclConvertor(options=scl_options)
    return str(convertor.convert(spec))