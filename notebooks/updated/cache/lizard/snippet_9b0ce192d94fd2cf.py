def pow(self, *args, **kwargs):
    return self._apply(operator.pow, *args, **kwargs)