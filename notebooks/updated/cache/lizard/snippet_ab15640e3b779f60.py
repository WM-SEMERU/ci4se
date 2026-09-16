def append_csv_data(file_strings):
    out_lines = list()
    head_line = None
    for fstrings in file_strings:
        file_lines = fstrings.split('\n')
        head_line = file_lines.pop(0)
        out_lines.extend(file_lines)
    out_lines.sort()
    i = 0
    while len(out_lines[i]) == 0:
        out_lines.pop(i)
    out_lines.insert(0, head_line)
    out_lines.append('')
    out_string = '\n'.join(out_lines)
    return out_string