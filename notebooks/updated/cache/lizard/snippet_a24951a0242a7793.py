def truncate_line(line, colno, max_before, max_after):
    line_len = len(line)
    new_colno = colno
    truncated_after = False
    truncated_before = False
    len_after = line_len - colno
    if len_after > max_after:
        truncated_after = True
        line = line[:colno + max_after]
    len_before = colno - 1
    if len_before > max_before:
        truncated_before = True
        line = line[len_before - max_before:]
        new_colno -= len_before - max_before
    line = _format('{0!A}', line)
    new_colno += 1
    if truncated_before:
        line = '...' + line
        new_colno += 3
    if truncated_after:
        line = line + '...'
    return line, new_colno