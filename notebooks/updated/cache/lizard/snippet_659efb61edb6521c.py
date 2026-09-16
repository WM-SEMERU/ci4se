def validateURL(value, blank=False, strip=None, allowlistRegexes=None,
    blocklistRegexes=None, excMsg=None):
    try:
        result = validateRegex(value=value, regex=URL_REGEX, blank=blank,
            strip=strip, allowlistRegexes=allowlistRegexes,
            blocklistRegexes=blocklistRegexes)
        if result is not None:
            return result
    except ValidationException:
        if value == 'localhost':
            return value
        _raiseValidationException(_('%r is not a valid URL.') % value, excMsg)