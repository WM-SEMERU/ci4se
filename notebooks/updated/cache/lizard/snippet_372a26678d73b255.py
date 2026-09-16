def set_fraction(self, value):
    if value < 0:
        value *= -1
    value = min(value, 1)
    if self.horizontal:
        width = int(self.width * value)
        height = self.height
    else:
        width = self.width
        height = int(self.height * value)
    self.canvas.coords(self.meter, self.xpos, self.ypos, self.xpos + width,
        self.ypos + height)