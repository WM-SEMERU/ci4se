def _float_or_str(value):
    value = QUOTE_REGEX.sub('', value)
    try:
        return float(value)
    except ValueError:
        return value