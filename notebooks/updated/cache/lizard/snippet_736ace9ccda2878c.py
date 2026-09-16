def _set_params_callback(self, **params):
    if 'callbacks' in params:
        setattr(self, 'callbacks', params.pop('callbacks'))
    names, _ = zip(*getattr(self, 'callbacks_'))
    for key in params.copy():
        name = key[11:]
        if '__' not in name and name in names:
            self._replace_callback(name, params.pop(key))
    for key in params.copy():
        name = key[11:]
        part0, part1 = name.split('__')
        kwarg = {part1: params.pop(key)}
        callback = dict(self.callbacks_).get(part0)
        if callback is not None:
            callback.set_params(**kwarg)
        else:
            raise ValueError(
                'Trying to set a parameter for callback {} which does not exist.'
                .format(part0))
    return self