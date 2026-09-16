def metadata_to_rmd_options(language, metadata):
    options = (language or 'R').lower()
    if 'name' in metadata:
        options += ' ' + metadata['name'] + ','
        del metadata['name']
    for jupyter_option, rmd_option, rev in _BOOLEAN_OPTIONS_DICTIONARY:
        if jupyter_option in metadata:
            options += ' {}={},'.format(rmd_option, _r_logical_values(
                metadata[jupyter_option] != rev))
            del metadata[jupyter_option]
    for opt_name in metadata:
        opt_value = metadata[opt_name]
        opt_name = opt_name.strip()
        if opt_name == 'active':
            options += ' {}="{}",'.format(opt_name, str(opt_value))
        elif isinstance(opt_value, bool):
            options += ' {}={},'.format(opt_name, 'TRUE' if opt_value else
                'FALSE')
        elif isinstance(opt_value, list):
            options += ' {}={},'.format(opt_name, 'c({})'.format(', '.join(
                ['"{}"'.format(str(v)) for v in opt_value])))
        else:
            options += ' {}={},'.format(opt_name, str(opt_value))
    if not language:
        options = options[2:]
    return options.strip(',').strip()