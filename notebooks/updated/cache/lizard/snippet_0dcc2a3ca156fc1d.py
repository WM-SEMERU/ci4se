def plugin_class_validation(self, plugin_class):
    try:
        getattr(plugin_class, 'dependencies')
        getattr(plugin_class, 'execute')
    except AttributeError:
        return False
    return True