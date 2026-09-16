def get_app_submodules(module_name):
    for name, module in get_app_modules():
        if module_has_submodule(module, module_name):
            yield name, import_module('{0}.{1}'.format(name, module_name))