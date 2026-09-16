def create_point(self, xcen, ycen, size=10, color='red', fill=None):
    if fill is None:
        fill = color
    x, y = self.p2c((xcen, ycen))
    x1 = x - size
    x2 = x + size
    y1 = y - size
    y2 = y + size
    self.create_rectangle(x1, y1, x2, y2, fill=fill, outline=color)