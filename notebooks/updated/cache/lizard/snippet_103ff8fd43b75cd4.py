def _get_bcpOut(self):
    nextSegment = self._nextSegment
    offCurves = nextSegment.offCurve
    if offCurves:
        bcp = offCurves[0]
        x, y = relativeBCPOut(self.anchor, (bcp.x, bcp.y))
    else:
        x = y = 0
    return x, y