def marker(self, lat, long, text, color=None, icon=None):
    try:
        self.dsmap = self._marker(lat, long, text, self.dsmap, color, icon)
        return self.dsmap
    except Exception as e:
        self.err(e, self.marker, 'Can not get marker')