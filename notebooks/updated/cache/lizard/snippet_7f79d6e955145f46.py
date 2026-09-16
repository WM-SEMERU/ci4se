def _removeBPoint(self, index, **kwargs):
    bPoint = self.bPoints[index]
    nextSegment = bPoint._nextSegment
    offCurves = nextSegment.offCurve
    if offCurves:
        offCurve = offCurves[0]
        self.removePoint(offCurve)
    segment = bPoint._segment
    offCurves = segment.offCurve
    if offCurves:
        offCurve = offCurves[-1]
        self.removePoint(offCurve)
    self.removePoint(bPoint._point)