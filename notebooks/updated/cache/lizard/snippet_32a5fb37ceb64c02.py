def _format_param_val(self, param_val):
    if isinstance(param_val, list):
        return ' '.join(str(x) for x in param_val)
    else:
        return str(param_val)