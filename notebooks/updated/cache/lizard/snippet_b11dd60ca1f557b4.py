def configure(self, *args, **kwargs):
    self.version = kwargs['schema_version']
    self.namespace = kwargs['namespace']
    self.backend = get(kwargs['type'])(*args, **kwargs)
    self.context = kwargs.pop('schema_context', {})