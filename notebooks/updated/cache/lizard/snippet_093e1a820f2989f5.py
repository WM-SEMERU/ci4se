def import_plugin(package_name, include_available=False):
    available_plugins_dir = MICRODROP_CONDA_SHARE.joinpath('plugins',
        'available')
    enabled_plugins_dir = MICRODROP_CONDA_ETC.joinpath('plugins', 'enabled')
    search_paths = [enabled_plugins_dir]
    if include_available:
        search_paths += [available_plugins_dir]
    for dir_i in search_paths:
        if dir_i not in sys.path:
            sys.path.insert(0, dir_i)
    module_name = package_name.split('.')[-1].replace('-', '_')
    return importlib.import_module(module_name)