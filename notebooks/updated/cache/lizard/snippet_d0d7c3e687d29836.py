def read(self, num_bytes, debug_info=None):
    if self.debug:
        if not debug_info:
            debug_info = str(num_bytes)
        sys.stderr.write('%s: READING %s\n' % (self.__class__.__name__,
            debug_info))
    res = self.ser.read(num_bytes)
    if self.debug:
        sys.stderr.write('%s: READ %i:\n%s\n' % (self.__class__.__name__,
            len(res), pyhsm.util.hexdump(res)))
    self.num_read_bytes += len(res)
    return res