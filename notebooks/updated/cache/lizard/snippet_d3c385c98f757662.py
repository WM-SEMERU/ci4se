def _validate_iso8601_string(self, value):
    ISO8601_REGEX = (
        '(\\d{4})-(\\d{2})-(\\d{2})T(\\d{2})\\:(\\d{2})\\:(\\d{2})([+-](\\d{2})\\:(\\d{2})|Z)'
        )
    if re.match(ISO8601_REGEX, value):
        return value
    else:
        raise ValueError('{} must be in ISO8601 format.'.format(value))