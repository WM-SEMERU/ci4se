def normalize_parameters(params):
    key_values = [(utils.escape(k), utils.escape(v)) for k, v in params]
    key_values.sort()
    parameter_parts = ['{0}={1}'.format(k, v) for k, v in key_values]
    return '&'.join(parameter_parts)