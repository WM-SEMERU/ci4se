def duration(self):
    if self._duration:
        return self._duration
    elif self.end:
        return self.end - self.begin
    else:
        return None