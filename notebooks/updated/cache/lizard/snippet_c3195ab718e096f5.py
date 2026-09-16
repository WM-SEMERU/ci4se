def index(self, item):
    item = self._cast(item)
    offset = item - self.startIp
    if offset >= 0 and offset < self._len:
        return offset
    raise ValueError('%s is not in range' % self._ipver.long2ip(item))