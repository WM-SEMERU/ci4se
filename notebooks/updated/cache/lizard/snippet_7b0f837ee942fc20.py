def _get_area(self):
    from fontTools.pens.areaPen import AreaPen
    pen = AreaPen(self.layer)
    self.draw(pen)
    return abs(pen.value)