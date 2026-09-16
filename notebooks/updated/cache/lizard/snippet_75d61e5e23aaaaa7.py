def explore_package(module_name):
    packages = []
    loader = pkgutil.get_loader(module_name)
    for sub_module in pkgutil.walk_packages([os.path.dirname(loader.
        get_filename())], prefix=module_name + '.'):
        _, sub_module_name, _ = sub_module
        packages.append(sub_module_name)
    return packages