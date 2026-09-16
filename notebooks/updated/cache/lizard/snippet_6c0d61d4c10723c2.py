def get_config_file_paths(env, args):
    flag = '--pants-config-files='
    evars = ['PANTS_GLOBAL_PANTS_CONFIG_FILES', 'PANTS_PANTS_CONFIG_FILES',
        'PANTS_CONFIG_FILES']
    path_list_values = []
    if os.path.isfile(get_default_pants_config_file()):
        path_list_values.append(ListValueComponent.create(
            get_default_pants_config_file()))
    for var in evars:
        if var in env:
            path_list_values.append(ListValueComponent.create(env[var]))
            break
    for arg in args:
        if arg.startswith(flag):
            path_list_values.append(ListValueComponent.create(arg[len(flag):]))
    return ListValueComponent.merge(path_list_values).val