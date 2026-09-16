def import_from_string(full_class_name):
    s = full_class_name.split('.')
    class_name = s[-1]
    module_name = full_class_name[:-len(class_name) - 1]
    module = importlib.import_module(module_name)
    klass = getattr(module, class_name)
    return klass