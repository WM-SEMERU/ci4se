def ruler_line(self, widths, linetype='-'):
    cells = []
    for w in widths:
        cells.append(linetype * (w + 2))
    return '+' + '+'.join(cells) + '+'