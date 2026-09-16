def summarize(self):
    if not self._achievements_summarized:
        for _ in self.operations():
            pass
    self._summarize()
    return self._summary