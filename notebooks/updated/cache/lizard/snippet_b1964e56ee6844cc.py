def _get_modules(self):
    not_import = set()
    not_import.add('base')
    modules = {}
    for path in self.config['global']['module_dir']:
        sys.path.insert(0, path)
        iter_modules = pkgutil.iter_modules([path])
        for module_info in iter_modules:
            module_name = module_info[1]
            if module_name in not_import:
                continue
            if helpers.helper_import(module_name, 'Validator'):
                module = helpers.helper_import(module_name)
                modules[module.__name__] = module
        sys.path.remove(path)
    return modules