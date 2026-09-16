def _destroy(self):
    self.unuse_region()
    if self._rlist is not None:
        try:
            if len(self._rlist) == 0:
                self._manager._fdict.pop(self._rlist.path_or_fd())
        except (TypeError, KeyError):
            pass