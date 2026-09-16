def keyword_only(func):

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if len(args) > 0:
            raise TypeError('Method %s forces keyword arguments.' % func.
                __name__)
        self._input_kwargs = kwargs
        return func(self, **kwargs)
    return wrapper