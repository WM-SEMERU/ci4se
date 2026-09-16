def unquote(cls, string):
    if len(string) == 0:
        return ''
    if string[0] != '"':
        return string
    if len(string) == 1:
        return string
    if string[-1] != '"':
        raise ValueError('Poorly formed string literal: %s' % string)

    def replace(match):
        value = match.group(0)
        if value == '\\\\':
            return '\\'
        if value == '\\"':
            return '"'
        if value == '""':
            return '"'
        if len(value) != 2:
            raise ValueError('Poorly formed string literal: %s' % string)
        return value
    result = re.sub(cls._escaped_quote_re, replace, string[1:-1])
    return result