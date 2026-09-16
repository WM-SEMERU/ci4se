def string_sanitize(string, tab_width=8):
    r
    string = string.replace('\r', '')
    lines = list()
    for line in string.split('\n'):
        tab_count = line.count('\t')
        if tab_count > 0:
            line_length = 0
            new_line = list()
            for i, chunk in enumerate(line.split('\t')):
                line_length += len(chunk)
                new_line.append(chunk)
                if i < tab_count:
                    next_tab_stop_in = tab_width - line_length % tab_width
                    new_line.append(' ' * next_tab_stop_in)
                    line_length += next_tab_stop_in
            lines.append(''.join(new_line))
        else:
            lines.append(line)
    return '\n'.join(lines)