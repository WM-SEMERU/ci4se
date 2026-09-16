def sync(self, max_bytes):
    max_bytes = max(max_bytes, 2)
    r = self._r
    r.align()
    while max_bytes > 0:
        try:
            b = r.bytes(1)
            if b == b'\xff':
                if r.bits(4) == 15:
                    return True
                r.align()
                max_bytes -= 2
            else:
                max_bytes -= 1
        except BitReaderError:
            return False
    return False