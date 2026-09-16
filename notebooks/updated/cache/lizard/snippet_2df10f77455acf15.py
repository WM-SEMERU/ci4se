def point(self, x, y, z=0, m=0):
    pointShape = _Shape(self.shapeType)
    pointShape.points.append([x, y, z, m])
    self._shapes.append(pointShape)