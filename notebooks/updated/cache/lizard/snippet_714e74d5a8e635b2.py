def get_class(self, module, class_name):
    class_object = getattr(module, class_name, None)
    if not class_object or not issubclass(class_object, Controller):
        class_object = None
    return class_object