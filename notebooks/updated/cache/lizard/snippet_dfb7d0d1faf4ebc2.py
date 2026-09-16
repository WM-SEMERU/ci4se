def write_tex(matrix, version, out, scale=1, border=None, color='black',
    unit='pt', url=None):

    def point(x, y):
        return '\\pgfqpoint{{{0}{2}}}{{{1}{2}}}'.format(x, y, unit)
    check_valid_scale(scale)
    check_valid_border(border)
    border = get_border(version, border)
    with writable(out, 'wt') as f:
        write = f.write
        write('% Creator:  {0}\n'.format(CREATOR))
        write('% Date:     {0}\n'.format(time.strftime('%Y-%m-%dT%H:%M:%S')))
        if url:
            write('\\href{{{0}}}{{'.format(url))
        write('\\begin{pgfpicture}\n')
        write('  \\pgfsetlinewidth{{{0}{1}}}\n'.format(scale, unit))
        if color and color != 'black':
            write('  \\color{{{0}}}\n'.format(color))
        x, y = border, -border
        for (x1, y1), (x2, y2) in matrix_to_lines(matrix, x, y, incby=-1):
            write('  \\pgfpathmoveto{{{0}}}\n'.format(point(x1 * scale, y1 *
                scale)))
            write('  \\pgfpathlineto{{{0}}}\n'.format(point(x2 * scale, y2 *
                scale)))
        write('  \\pgfusepath{stroke}\n')
        write('\\end{{pgfpicture}}{0}\n'.format('' if not url else '}'))