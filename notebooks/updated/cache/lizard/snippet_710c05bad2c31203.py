def _calculateBasalSegmentActivity(connections, activeInput,
    reducedBasalThresholdCells, connectedPermanence, activationThreshold,
    minThreshold, reducedBasalThreshold):
    overlaps = connections.computeActivity(activeInput, connectedPermanence)
    outrightActiveSegments = np.flatnonzero(overlaps >= activationThreshold)
    if reducedBasalThreshold != activationThreshold and len(
        reducedBasalThresholdCells) > 0:
        potentiallyActiveSegments = np.flatnonzero((overlaps <
            activationThreshold) & (overlaps >= reducedBasalThreshold))
        cellsOfCASegments = connections.mapSegmentsToCells(
            potentiallyActiveSegments)
        conditionallyActiveSegments = potentiallyActiveSegments[np.in1d(
            cellsOfCASegments, reducedBasalThresholdCells)]
        activeSegments = np.concatenate((outrightActiveSegments,
            conditionallyActiveSegments))
    else:
        activeSegments = outrightActiveSegments
    potentialOverlaps = connections.computeActivity(activeInput)
    matchingSegments = np.flatnonzero(potentialOverlaps >= minThreshold)
    return activeSegments, matchingSegments, potentialOverlaps