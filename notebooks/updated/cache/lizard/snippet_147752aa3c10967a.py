def discover(package, cls_match_func):
    matched_classes = set()
    for _, module_name, _ in pkgutil.walk_packages(package.__path__, prefix
        =package.__name__ + '.'):
        module = __import__(module_name, fromlist=[str('__trash')], level=0)
        for _, imported_class in inspect.getmembers(module, inspect.isclass):
            if imported_class.__module__ != module.__name__:
                continue
            if cls_match_func(imported_class):
                matched_classes.add(imported_class)
    return matched_classes