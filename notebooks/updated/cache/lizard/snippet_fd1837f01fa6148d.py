def update(self, content=None):
    if not content:
        return
    if content == 'summary' or 'extended' or 'powerflow':
        self._update_summary(self.system)
    if content == 'extended' or 'powerflow':
        self._update_extended(self.system)