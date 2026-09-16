def asbool(value):
    is_string = isinstance(value, string_types)
    if is_string:
        value = value.strip().lower()
        if value in ('true', 'yes', 'on', 'y', 't', '1'):
            return True
        elif value in ('false', 'no', 'off', 'n', 'f', '0'):
            return False
        else:
            raise ValueError('String is not true/false: %r' % value)
    else:
        return bool(value)