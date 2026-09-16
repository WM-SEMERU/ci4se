def register_frame(self, frame):
    self._frame = frame
    for column in self._columns:
        for widget in column:
            widget.register_frame(self._frame)