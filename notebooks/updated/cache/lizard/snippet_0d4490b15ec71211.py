def _get_config(self, i):
    variables = {}
    if not i.get_option('config'):
        raise Exception('The --config|-c option is missing.')
    with open(i.get_option('config')) as fh:
        exec(fh.read(), {}, variables)
    return variables['DATABASES']