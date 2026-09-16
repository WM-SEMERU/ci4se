def format_columns(lines, prefix=''):
    if len(lines) == 0:
        return ''
    ncols = 0
    for l in lines:
        ncols = max(ncols, len(l))
    if ncols == 0:
        return ''
    maxlen = [0] * (ncols - 1)
    for l in lines:
        for c in range(ncols - 1):
            maxlen[c] = max(maxlen[c], len(l[c]))
    fmtstr = prefix + '  '.join(['{{:{x}}}'.format(x=x) for x in maxlen])
    fmtstr += '  {}'
    return [fmtstr.format(*l) for l in lines]