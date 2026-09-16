def pointz(self, x, y, z=0, m=None):
    shapeType = POINTZ
    pointShape = Shape(shapeType)
    pointShape.points.append([x, y, z, m])
    self.shape(pointShape)