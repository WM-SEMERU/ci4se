def get_description_lines(docstring):
    if prepare_docstring is None:
        raise ImportError('sphinx must be installed to use this function.')
    if not isinstance(docstring, str):
        return []
    lines = []
    for line in prepare_docstring(docstring):
        if DESCRIPTION_END_RE.match(line):
            break
        lines.append(line)
    if lines and lines[-1] != '':
        lines.append('')
    return lines