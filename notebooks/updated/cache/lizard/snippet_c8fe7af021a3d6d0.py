def convert_to_float_list(value):
    if isinstance(value, list) or value is None:
        return value
    else:
        s = re.findall('([-+]?\\d*\\.\\d+|\\d+|[-+]?\\d+)', value)
        for k, v in enumerate(s):
            try:
                s[k] = float(v)
            except ValueError:
                pass
        return s