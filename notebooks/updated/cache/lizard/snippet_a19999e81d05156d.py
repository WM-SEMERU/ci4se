def minutes_played(self):
    if self._minutes_played[self._index]:
        minutes, seconds = self._minutes_played[self._index].split(':')
        minutes = float(minutes) + float(seconds) / 60
        return float(minutes)
    return None