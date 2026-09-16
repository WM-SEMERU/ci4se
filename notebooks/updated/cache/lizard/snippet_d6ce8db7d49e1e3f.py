def get_model_params(self, deep=True):
    r
    out = dict()
    for key in self._get_model_param_names():
        from pyemma.util.exceptions import PyEMMA_DeprecationWarning
        warnings.simplefilter('always', DeprecationWarning)
        warnings.simplefilter('always', PyEMMA_DeprecationWarning)
        try:
            with warnings.catch_warnings(record=True) as w:
                value = getattr(self, key, None)
            if len(w) and w[0].category in (DeprecationWarning,
                PyEMMA_DeprecationWarning):
                continue
        finally:
            warnings.filters.pop(0)
            warnings.filters.pop(0)
        if deep and hasattr(value, 'get_params'):
            deep_items = list(value.get_params().items())
            out.update((key + '__' + k, val) for k, val in deep_items)
        out[key] = value
    return out