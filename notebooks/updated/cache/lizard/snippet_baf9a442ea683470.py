def db_for_write(self, model, **hints):
    if model._meta.app_label in self._apps:
        return getattr(model, '_db_alias', model._meta.app_label)
    return None