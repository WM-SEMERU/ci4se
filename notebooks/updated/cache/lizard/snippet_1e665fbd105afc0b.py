def format_sequence(seq, start=None, end=None, group_size=3):
    width = 100
    loc_width = 9
    sep = ' '
    body_sep = ' : '
    start = start or 0
    end = end or len(seq)
    bw = width - loc_width - len(body_sep)
    assert group_size <= bw, 'group size must be less than available line width'
    gpl = int((bw + len(sep)) / (group_size + len(sep)))
    gpl = int(gpl / 5) * 5 if gpl > 20 else gpl
    rpl = group_size * gpl
    line_fmt = '{{l:>{lw}s}}{body_sep}{{body}}'.format(lw=loc_width,
        body_sep=body_sep)
    ge_fmt = '{{ge:>{gs}}}'.format(gs=group_size)
    blocks = []
    for ls in range(start, end, rpl):
        le = ls + rpl
        groups = [ge_fmt.format(ge=str(gs + group_size)[-group_size + 1:]) for
            gs in range(ls, le, group_size)]
        blocks += [line_fmt.format(l='', body=sep.join(groups)) + '\n']
        groups = [seq[gs:min(gs + group_size, end)] for gs in range(ls, le,
            group_size)]
        blocks += [line_fmt.format(l=str(ls + 1), body=sep.join(groups)) + '\n'
            ]
        blocks += ['\n']
    return blocks