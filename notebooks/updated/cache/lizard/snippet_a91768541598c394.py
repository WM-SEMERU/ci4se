def pexpireat(self, key, timestamp):
    if not isinstance(timestamp, int):
        raise TypeError('timestamp argument must be int, not {!r}'.format(
            timestamp))
    fut = self.execute(b'PEXPIREAT', key, timestamp)
    return wait_convert(fut, bool)