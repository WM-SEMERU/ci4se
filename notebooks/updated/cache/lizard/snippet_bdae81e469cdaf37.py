def get_sector_slice(self, start, end=None):
    pos, size = self.header.get_pos(start)
    if end is None:
        end = start
    while start < end:
        start += 1
        _, more = self.header.get_pos(start)
        size += more
    return slice(pos, pos + size)