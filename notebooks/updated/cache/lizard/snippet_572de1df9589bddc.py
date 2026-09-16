def validateInt(value, blank=False, strip=None, allowlistRegexes=None,
    blocklistRegexes=None, min=None, max=None, lessThan=None, greaterThan=
    None, excMsg=None):
    return validateNum(value=value, blank=blank, strip=strip,
        allowlistRegexes=None, blocklistRegexes=blocklistRegexes, _numType=
        'int', min=min, max=max, lessThan=lessThan, greaterThan=greaterThan)