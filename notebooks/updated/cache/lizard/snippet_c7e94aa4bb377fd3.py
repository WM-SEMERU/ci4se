def dumps_list(l, *, escape=True, token='%\n', mapper=None, as_content=True):
    r
    strings = (_latex_item_to_string(i, escape=escape, as_content=
        as_content) for i in l)
    if mapper is not None:
        if not isinstance(mapper, list):
            mapper = [mapper]
        for m in mapper:
            strings = [m(s) for s in strings]
        strings = [_latex_item_to_string(s) for s in strings]
    return NoEscape(token.join(strings))