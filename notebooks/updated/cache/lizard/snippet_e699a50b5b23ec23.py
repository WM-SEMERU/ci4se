def auto_invalidate(self):
    current = datetime.now()
    if current > self._invalidated + timedelta(seconds=self._timetolive):
        self.invalidate()