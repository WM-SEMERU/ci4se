def str(self, threshold=0.1):
    if not self._times:
        return ''
    total = sum(s.sum for k, s in six.iteritems(self._times) if '.' not in k)
    table = [['', '% total', 'sum', 'avg', 'dev', 'min', 'max', 'num']]
    for k, v in sorted(self._times.items()):
        percent = 100 * v.sum / (total or 1)
        if percent > threshold:
            table.append([k, '%.2f%%' % percent, '%.4f' % v.sum, '%.4f' % v
                .avg, '%.4f' % v.dev, '%.4f' % v.min, '%.4f' % v.max, '%d' %
                v.num])
    col_widths = [max(len(row[i]) for row in table) for i in range(len(
        table[0]))]
    out = ''
    for row in table:
        out += '  ' + row[0].ljust(col_widths[0]) + '  '
        out += '  '.join(val.rjust(width) for val, width in zip(row[1:],
            col_widths[1:]))
        out += '\n'
    return out