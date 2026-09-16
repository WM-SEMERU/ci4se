def filter(self, **kwargs):
    f_field = kwargs.keys()[0]
    f_value = kwargs[f_field]
    _newset = []
    for m in self._dataset:
        if hasattr(m, f_field):
            if getattr(m, f_field) == f_value:
                _newset.append(m)
    self._dataset = _newset
    return self