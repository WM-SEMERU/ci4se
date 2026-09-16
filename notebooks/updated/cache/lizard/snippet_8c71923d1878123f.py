def shift_right(self, times=1):
    try:
        return Location(self._rank, self._file + times)
    except IndexError as e:
        raise IndexError(e)