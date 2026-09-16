def get_unaligned_start_coord(self):
    sys.stderr.write('error unimplemented get_unaligned_start_coord\n')
    sys.exit()
    if len(self._unaligned) == 0:
        return None
    return [self._lines[self._unaligned[0] - 1]['filestart'], self._lines[
        self._unaligned[0] - 1]['innerstart']]