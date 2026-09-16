def unquote(cls, string):
    if len(string) == 0:
        return ''
    if string[0] == '"':
        if len(string) == 1 or string[-1] != '"':
            raise SyntaxError('Poorly formed string literal: ' + string)
        string = string[1:-1]
    if len(string) == 0:
        return ''

    def replace(match):
        value = match.group(0)
        if value == '""':
            return '"'
        if len(value) < 2:
            raise SyntaxError('Poorly formed string literal: ' + string)
        return value[1]
    result = re.sub(cls._escaped_character_re, replace, string)
    return result