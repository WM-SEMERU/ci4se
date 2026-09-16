def next(self):
    if self._fut is None:
        self._fut = self._iter.getq()
    try:
        try:
            (ent, self._cursor_before, self._cursor_after, self._more_results
                ) = self._fut.get_result()
            return ent
        except EOFError:
            self._exhausted = True
            raise StopIteration
    finally:
        self._fut = None