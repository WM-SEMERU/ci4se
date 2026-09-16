def get_help_datapacks(module_name, server_prefix):
    _dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(
        __file__)))
    module_dir = '{}/../{}'.format(_dir, module_name, '_help.json')
    if os.path.isdir(module_dir):
        module_help_path = '{}/{}'.format(module_dir, '_help.json')
        if os.path.isfile(module_help_path):
            return helptools.get_help_datapacks(module_help_path, server_prefix
                )
        else:
            return [('Help', '{} does not have a help.json file'.format(
                module_name), False)]
    else:
        return [('Help', 'No module found called {}'.format(module_name),
            False)]