def parameters(names, **kwargs):
    sequence_fields = ['value', 'min', 'max', 'fixed']
    sequences = {}
    for attr in sequence_fields:
        try:
            iter(kwargs[attr])
        except (TypeError, KeyError):
            pass
        else:
            sequences[attr] = kwargs.pop(attr)
    if 'min' in sequences and 'max' in sequences:
        for min, max in zip(sequences['min'], sequences['max']):
            if min > max:
                raise ValueError(
                    'The value of `min` should be less than or equal to the value of `max`.'
                    )
    params = symbols(names, cls=Parameter, seq=True, **kwargs)
    for key, values in sequences.items():
        try:
            assert len(values) == len(params)
        except AssertionError:
            raise ValueError(
                '`len` of keyword-argument `{}` does not match the number of `Parameter`s created.'
                .format(attr))
        except TypeError:
            pass
        finally:
            for param, value in zip(params, values):
                setattr(param, key, value)
    return params