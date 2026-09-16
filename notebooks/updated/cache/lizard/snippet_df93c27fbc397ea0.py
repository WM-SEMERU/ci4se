def _getgroup(string, depth):
    out, comma = [], False
    while string:
        items, string = _getitem(string, depth)
        if not string:
            break
        out += items
        if string[0] == '}':
            if comma:
                return out, string[1:]
            return [('{' + a + '}') for a in out], string[1:]
        if string[0] == ',':
            comma, string = True, string[1:]
    return None