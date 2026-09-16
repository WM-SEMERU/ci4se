def just_in_time_method(func):
    if not inspect.ismethod:
        raise MetaError('oops')

    def wrapper(self, *args, **kwargs):
        if self.item is None:
            self.item = self.factory[self.key]
        return getattr(self.item, func.__name__)(*args, **kwargs)
    return wrapper