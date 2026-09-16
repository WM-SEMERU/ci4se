def indentation(logical_line, previous_logical, indent_char, indent_level,
    previous_indent_level):
    r
    c = 0 if logical_line else 3
    tmpl = 'E11%d %s' if logical_line else 'E11%d %s (comment)'
    if indent_level % 4:
        yield 0, tmpl % (1 + c, 'indentation is not a multiple of four')
    indent_expect = previous_logical.endswith(':')
    if indent_expect and indent_level <= previous_indent_level:
        yield 0, tmpl % (2 + c, 'expected an indented block')
    elif not indent_expect and indent_level > previous_indent_level:
        yield 0, tmpl % (3 + c, 'unexpected indentation')