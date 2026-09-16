def point(self, x, y, color=None):
    if x < 0 or y < 0 or x > self.width - 1 or y > self.height - 1:
        return
    if color is None:
        color = self.color
    o = self._offset(x, y)
    self.canvas[o:o + 3] = blend(self.canvas[o:o + 3], bytearray(color))