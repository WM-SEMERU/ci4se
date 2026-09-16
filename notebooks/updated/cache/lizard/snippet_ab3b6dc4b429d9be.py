def color(self, color):
    if saturation_of_color(color) == 0:
        self.white()
        return
    self._color = color
    self.hue = hue_of_color(color)