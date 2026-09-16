def has_module_perms(self, user_obj, app_label):
    cache_name = '_%s_cache' % app_label
    if hasattr(self, cache_name):
        handlers = getattr(self, cache_name)
    else:
        handlers = [h for h in registry.get_handlers() if app_label in h.
            get_supported_app_labels()]
        setattr(self, cache_name, handlers)
    for handler in handlers:
        if handler.has_module_perms(user_obj, app_label):
            return True
    return False