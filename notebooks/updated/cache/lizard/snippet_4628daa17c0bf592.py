def background(self):
    if self._color or not self.editor:
        return self._color
    else:
        return drift_color(self.editor.background, 110)