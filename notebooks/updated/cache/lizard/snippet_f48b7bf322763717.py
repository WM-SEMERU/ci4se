def get_restored(self):
    return (self._header.initial.restore_time > 0, self._header.initial.
        restore_time)