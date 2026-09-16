def get_item(self, **kwargs):
    if six.callable(self.context):
        self.reload_context(es_based=False, **kwargs)
    objects = self._parent_queryset()
    if objects is not None and self.context not in objects:
        raise JHTTPNotFound('{}({}) not found'.format(self.Model.__name__,
            self._get_context_key(**kwargs)))
    return self.context