def get_parent_queryset(self):
    if self.parent_queryset is not None:
        return self.parent_queryset._clone()
    if self.parent_model is not None:
        return self.parent_model._default_manager.all()
    raise ImproperlyConfigured(
        "'%s' must define 'parent_queryset' or 'parent_model'" % self.
        __class__.__name__)