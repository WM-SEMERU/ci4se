def find_resource_class(resource_path):
    class_path = ResourceTypes[resource_path]
    full_path = '.'.join([__name__, class_path])
    class_data = full_path.split('.')
    module_path = '.'.join(class_data[:-1])
    class_str = class_data[-1]
    module = importlib.import_module(module_path)
    return getattr(module, class_str)