def validate_read(self, kwargs):
    kwargs = super().validate_read(kwargs)
    if 'start' in kwargs or 'stop' in kwargs:
        raise NotImplementedError(
            'start and/or stop are not supported in fixed Sparse reading')
    return kwargs