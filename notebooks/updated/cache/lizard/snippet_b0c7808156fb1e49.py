def to_csv(self, sep=',', path=None):
    data = []
    first_row = ['Stat']
    first_row.extend(self._names)
    data.append(sep.join(first_row))
    stats = self._stats()
    for stat in stats:
        k, n, f = stat
        if k is None:
            row = [''] * len(data[0])
            data.append(sep.join(row))
            continue
        row = [n]
        for key in self._names:
            raw = getattr(self[key], k)
            if f is None:
                row.append(raw)
            elif f == 'p':
                row.append(fmtp(raw))
            elif f == 'n':
                row.append(fmtn(raw))
            elif f == 'dt':
                row.append(raw.strftime('%Y-%m-%d'))
            else:
                raise NotImplementedError('unsupported format %s' % f)
        data.append(sep.join(row))
    res = '\n'.join(data)
    if path is not None:
        with open(path, 'w') as fl:
            fl.write(res)
    else:
        return res