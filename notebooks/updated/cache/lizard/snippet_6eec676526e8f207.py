def fmt_repertoire(r):
    if r is None:
        return ''
    r = r.squeeze()
    lines = []
    space = ' ' * 4
    head = '{S:^{s_width}}{space}Pr({S})'.format(S='S', s_width=r.ndim,
        space=space)
    lines.append(head)
    for state in utils.all_states(r.ndim):
        state_str = ''.join(str(i) for i in state)
        lines.append('{0}{1}{2}'.format(state_str, space, fmt_number(r[state]))
            )
    width = max(len(line) for line in lines)
    lines.insert(1, DOTTED_HEADER * (width + 1))
    return box('\n'.join(lines))