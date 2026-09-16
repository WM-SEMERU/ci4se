def split_leading_indent(line, max_indents=None):
    indent = ''
    while (max_indents is None or max_indents > 0) and line.startswith((
        openindent, closeindent)) or line.lstrip() != line:
        if max_indents is not None and line.startswith((openindent,
            closeindent)):
            max_indents -= 1
        indent += line[0]
        line = line[1:]
    return indent, line