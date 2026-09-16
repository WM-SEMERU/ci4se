def _get_history_next(self):
    if self._has_history:
        ret = self._input_history.return_history(1)
        self.string = ret
        self._curs_pos = len(ret)