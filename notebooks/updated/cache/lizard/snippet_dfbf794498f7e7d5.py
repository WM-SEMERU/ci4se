def _validate_params_types(self, method, params):
    if isinstance(params, list):
        if not isinstance(self.method_data[method]['types'], list):
            raise InvalidParamsError('expected keyword params, not positional')
        for param, type, posnum in zip(params, self.method_data[method][
            'types'], range(1, len(params) + 1)):
            if not (isinstance(param, type) or param is None):
                raise InvalidParamsError('positional arg #{} is the wrong type'
                    .format(posnum))
    elif isinstance(params, dict):
        if not isinstance(self.method_data[method]['types'], dict):
            raise InvalidParamsError('expected positional params, not keyword')
        if 'required' in self.method_data[method]:
            for key in self.method_data[method]['required']:
                if key not in params:
                    raise InvalidParamsError('missing key: %s' % key)
        for key in params.keys():
            if key not in self.method_data[method]['types'] or not (isinstance
                (params[key], self.method_data[method]['types'][key]) or 
                params[key] is None):
                raise InvalidParamsError('arg "{}" is the wrong type'.
                    format(key))