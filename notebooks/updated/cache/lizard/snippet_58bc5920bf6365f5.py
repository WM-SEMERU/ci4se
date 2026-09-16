def add_indent_lines(prefix, s):
    if not s:
        return prefix
    prefix_len = str_visible_len(prefix)
    lines = s.splitlines(True)
    return ''.join([prefix + lines[0]] + [(' ' * prefix_len + l) for l in
        lines[1:]])