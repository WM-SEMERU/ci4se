def get_modules():
    modules = []
    module_list = exec_action('modules', 'list', action_parameter=
        '--only-names')
    if not module_list:
        return None
    for module in module_list:
        if module not in ['help', 'usage', 'version']:
            modules.append(module)
    return modules