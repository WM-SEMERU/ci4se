def _convert(self, val):
    if isinstance(val, dict) and not isinstance(val, DotDict):
        return DotDict(val), True
    elif isinstance(val, list) and not isinstance(val, DotList):
        return DotList(val), True
    return val, False