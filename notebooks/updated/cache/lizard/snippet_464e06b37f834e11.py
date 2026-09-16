def get_line_segments(line):
    line = line.strip()
    tokens = tk.generate_tokens(io.StringIO(line).readline)
    equality_signs = [-1]
    comment_tuple = None, ''
    for i, t in enumerate(tokens):
        if t.type == tk.COMMENT:
            comment_tuple = t.start[1], t.string
        if t.type == tk.OP and t.string == '=':
            equality_signs.append(t.start[1])
    if len(equality_signs) > 1:
        lhs = line[equality_signs[-2] + 1:equality_signs[-1]].strip()
        equality_signs.pop(0)
    else:
        lhs = None
    rhs_start_idx = equality_signs[-1] + 1
    rhs = line[rhs_start_idx:comment_tuple[0]].strip()
    if rhs == '':
        rhs = None
    comment = comment_tuple[1].strip()
    return lhs, rhs, comment