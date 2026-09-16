def parse_docstring(thing):
    assert not isinstance(thing, bytes)
    doc = cleandoc(thing) if isinstance(thing, str) else getdoc(thing)
    doc = empty if doc is None else doc
    assert not isinstance(doc, bytes)
    parts = docstring_split(doc)
    if len(parts) == 2:
        title, body = parts[0], parts[1]
    else:
        title, body = parts[0], empty
    title = remove_line_breaks(title)
    body = body.replace('\r\n', newline).replace('\r', newline)
    return docstring(title, body)