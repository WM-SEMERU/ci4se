def update(self, arg, allow_overwrite=False):
    if inspect.isclass(arg) and issubclass(arg, ICatalog) or isinstance(arg,
        ICatalog):
        arg = arg._providers
    if not allow_overwrite:
        for key in arg:
            if key in self._providers:
                raise KeyError('Key %s already exists' % key)
    super(ProviderMapping, self).update(arg)