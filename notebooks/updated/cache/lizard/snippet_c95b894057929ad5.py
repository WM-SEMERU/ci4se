def validate_read(self, kwargs):
    kwargs = copy.copy(kwargs)
    columns = kwargs.pop('columns', None)
    if columns is not None:
        raise TypeError(
            'cannot pass a column specification when reading a Fixed format store. this store must be selected in its entirety'
            )
    where = kwargs.pop('where', None)
    if where is not None:
        raise TypeError(
            'cannot pass a where specification when reading from a Fixed format store. this store must be selected in its entirety'
            )
    return kwargs