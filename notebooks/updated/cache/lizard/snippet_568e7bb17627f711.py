def _wrap(text, wrap_max=80, indent=4):
    indent = indent * ' '
    wrap_width = wrap_max - len(indent)
    if isinstance(text, Path):
        text = path2str(text)
    return textwrap.fill(text, width=wrap_width, initial_indent=indent,
        subsequent_indent=indent, break_long_words=False, break_on_hyphens=
        False)