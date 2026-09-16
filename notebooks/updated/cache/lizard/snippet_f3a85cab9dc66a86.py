def read_short(self, base, offset=0):
    fmt = b'<H' if self._byte_order is LITTLE_ENDIAN else b'>H'
    return self._read_int(fmt, base, offset)