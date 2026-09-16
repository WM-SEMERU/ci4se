def return_value(self, *args, **kwargs):
    self._called()
    return self._return_value(*args, **kwargs)