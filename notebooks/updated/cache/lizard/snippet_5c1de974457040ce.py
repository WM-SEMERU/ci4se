def duration(self):
    if self._closed or not self._result or 'duration' not in self._result:
        return -1
    return self._result.get('duration', 0)