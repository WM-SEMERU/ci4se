def _insertBPoint(self, index, type, anchor, bcpIn, bcpOut, **kwargs):
    self._insertSegment(index=index, type='line', points=[anchor], smooth=False
        )
    bPoints = self.bPoints
    index += 1
    if index >= len(bPoints):
        index = -1
    bPoint = bPoints[index]
    bPoint.bcpIn = bcpIn
    bPoint.bcpOut = bcpOut
    bPoint.type = type