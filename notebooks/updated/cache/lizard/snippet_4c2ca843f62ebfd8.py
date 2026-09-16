def ParseNumericOption(self, options, name, base=10, default_value=None):
    numeric_value = getattr(options, name, None)
    if not numeric_value:
        return default_value
    try:
        return int(numeric_value, base)
    except (TypeError, ValueError):
        name = name.replace('_', ' ')
        raise errors.BadConfigOption('Unsupported numeric value {0:s}: {1!s}.'
            .format(name, numeric_value))