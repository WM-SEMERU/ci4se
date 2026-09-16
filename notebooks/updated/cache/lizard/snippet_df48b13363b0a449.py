def _convertPointsToSegments(points, willBeReversed=False):
    previousOnCurve = None
    for point in reversed(points):
        if point.segmentType is not None:
            previousOnCurve = point.coordinates
            break
    assert previousOnCurve is not None
    offCurves = []
    segments = []
    for point in points:
        if point.segmentType is None:
            offCurves.append(point)
        else:
            segment = InputSegment(points=offCurves + [point],
                previousOnCurve=previousOnCurve, willBeReversed=willBeReversed)
            segments.append(segment)
            offCurves = []
            previousOnCurve = point.coordinates
    assert not offCurves
    return segments