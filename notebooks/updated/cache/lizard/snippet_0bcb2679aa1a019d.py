def _inside_regions(self, address):
    try:
        start_addr = next(self._regions.irange(maximum=address, reverse=True))
    except StopIteration:
        return False
    else:
        return address < self._regions[start_addr]