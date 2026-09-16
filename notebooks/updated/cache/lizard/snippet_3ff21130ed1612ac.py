def _afterpoint(string):
    if _isnumber(string):
        if _isint(string):
            return -1
        else:
            pos = string.rfind('.')
            pos = string.lower().rfind('e') if pos < 0 else pos
            if pos >= 0:
                return len(string) - pos - 1
            else:
                return -1
    else:
        return -1