def split_escape(string, sep, maxsplit=None, escape_char='\\'):
    assert len(sep) == 1
    assert len(escape_char) == 1
    if isinstance(string, bytes):
        if isinstance(escape_char, text_type):
            escape_char = escape_char.encode('ascii')
        iter_ = iterbytes
    else:
        iter_ = iter
    if maxsplit is None:
        maxsplit = len(string)
    empty = string[:0]
    result = []
    current = empty
    escaped = False
    for char in iter_(string):
        if escaped:
            if char != escape_char and char != sep:
                current += escape_char
            current += char
            escaped = False
        elif char == escape_char:
            escaped = True
        elif char == sep and len(result) < maxsplit:
            result.append(current)
            current = empty
        else:
            current += char
    result.append(current)
    return result