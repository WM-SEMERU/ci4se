def box(self, x0, y0, width, height):
    assert width > 1
    assert height > 1
    width -= 1
    height -= 1
    for x in range(x0, x0 + width):
        self.point(x, y0, '-')
        self.point(x, y0 + height, '-')
    for y in range(y0, y0 + height):
        self.point(x0, y, '|')
        self.point(x0 + width, y, '|')
    self.point(x0, y0, '+')
    self.point(x0 + width, y0, '+')
    self.point(x0, y0 + height, '+')
    self.point(x0 + width, y0 + height, '+')