def prefer_type(self, prefer, over):
    self._write_lock.acquire()
    try:
        if self._preferred(preferred=over, over=prefer):
            raise ValueError('Type %r is already preferred over %r.' % (
                over, prefer))
        prefs = self._prefer_table.setdefault(prefer, set())
        prefs.add(over)
    finally:
        self._write_lock.release()