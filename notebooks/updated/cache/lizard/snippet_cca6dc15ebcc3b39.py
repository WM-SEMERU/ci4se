def import_submodules(package):
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for _, full_name, is_pkg in pkgutil.walk_packages(package.__path__, 
        package.__name__ + '.'):
        results[full_name] = importlib.import_module(full_name)
        if is_pkg:
            results.update(import_submodules(full_name))
    return results