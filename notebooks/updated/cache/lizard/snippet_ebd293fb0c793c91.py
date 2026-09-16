def validateRegexStr(value, blank=False, strip=None, allowlistRegexes=None,
    blocklistRegexes=None, excMsg=None):
    _validateGenericParameters(blank=blank, strip=strip, allowlistRegexes=
        allowlistRegexes, blocklistRegexes=blocklistRegexes)
    returnNow, value = _prevalidationCheck(value, blank, strip,
        allowlistRegexes, blocklistRegexes, excMsg)
    if returnNow:
        return value
    try:
        return re.compile(value)
    except Exception as ex:
        _raiseValidationException(_(
            '%r is not a valid regular expression: %s') % (_errstr(value),
            ex), excMsg)