def current_iid(self):
    current = self.current
    if current is None or current not in self._canvas_markers:
        return None
    return self._canvas_markers[current]