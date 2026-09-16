def outlineColor(self, value):
    if isinstance(value, Color) and not self._outline is None:
        self._outline['color'] = value