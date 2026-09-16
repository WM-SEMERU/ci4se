def read(self, entity=None, attrs=None, ignore=None, params=None):
    if entity is None:
        entity = type(self)(self._server_config, product=self.product)
    if ignore is None:
        ignore = set()
    return super(RepositorySet, self).read(entity, attrs, ignore, params)