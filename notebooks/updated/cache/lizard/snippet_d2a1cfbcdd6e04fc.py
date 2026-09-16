def get_queryset(self):
    if self.queryset is not None:
        queryset = self.queryset
        if hasattr(queryset, '_clone'):
            queryset = queryset._clone()
    elif self.model is not None:
        queryset = self.model._default_manager.all()
    else:
        msg = '{0} must define ``queryset`` or ``model``'
        raise ImproperlyConfigured(msg.format(self.__class__.__name__))
    return queryset