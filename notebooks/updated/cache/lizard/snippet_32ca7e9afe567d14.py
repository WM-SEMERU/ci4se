def parse_range_header(self, header, resource_size):
    if not header or '=' not in header:
        return None
    ranges = []
    units, range_ = header.split('=', 1)
    units = units.strip().lower()
    if units != 'bytes':
        return None
    for val in range_.split(','):
        val = val.strip()
        if '-' not in val:
            return None
        if val.startswith('-'):
            start = resource_size + int(val)
            if start < 0:
                start = 0
            stop = resource_size
        else:
            start, stop = val.split('-', 1)
            start = int(start)
            stop = int(stop) + 1 if stop else resource_size
            if start >= stop:
                return None
        ranges.append((start, stop))
    return ranges