def outlineWidth(self, value):
    if isinstance(value, (int, float, long)) and not self._outline is None:
        self._outline['width'] = value