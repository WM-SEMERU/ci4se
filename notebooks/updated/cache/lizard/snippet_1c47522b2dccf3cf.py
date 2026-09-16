def _pop_params(cls, kwargs):
    params = cls.params
    if not isinstance(params, Mapping):
        params = {k: NotSpecified for k in params}
    param_values = []
    for key, default_value in params.items():
        try:
            value = kwargs.pop(key, default_value)
            if value is NotSpecified:
                raise KeyError(key)
            hash(value)
        except KeyError:
            raise TypeError('{typename} expected a keyword parameter {name!r}.'
                .format(typename=cls.__name__, name=key))
        except TypeError:
            raise TypeError(
                '{typename} expected a hashable value for parameter {name!r}, but got {value!r} instead.'
                .format(typename=cls.__name__, name=key, value=value))
        param_values.append((key, value))
    return tuple(param_values)