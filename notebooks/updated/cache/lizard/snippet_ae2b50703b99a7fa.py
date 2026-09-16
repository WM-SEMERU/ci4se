def parameter_type(self, parameter_type):
    allowed_values = ['SIMPLE', 'LIST', 'DYNAMIC']
    if parameter_type not in allowed_values:
        raise ValueError(
            'Invalid value for `parameter_type` ({0}), must be one of {1}'.
            format(parameter_type, allowed_values))
    self._parameter_type = parameter_type