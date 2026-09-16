def _mmComputeSequenceRepresentationData(self):
    if not self._sequenceRepresentationDataStale:
        return
    unionSDRTrace = self.mmGetTraceUnionSDR()
    sequenceLabelsTrace = self.mmGetTraceSequenceLabels()
    resetsTrace = self.mmGetTraceResets()
    n = len(unionSDRTrace.data)
    overlapMatrix = numpy.empty((n, n), dtype=uintType)
    stabilityConfusionUnionSDR = []
    distinctnessConfusionUnionSDR = []
    for i in xrange(n):
        for j in xrange(i + 1):
            overlapUnionSDR = len(unionSDRTrace.data[i] & unionSDRTrace.data[j]
                )
            overlapMatrix[i][j] = overlapUnionSDR
            overlapMatrix[j][i] = overlapUnionSDR
            if i != j and sequenceLabelsTrace.data[i
                ] is not None and not resetsTrace.data[i
                ] and sequenceLabelsTrace.data[j
                ] is not None and not resetsTrace.data[j]:
                if sequenceLabelsTrace.data[i] == sequenceLabelsTrace.data[j]:
                    stabilityConfusionUnionSDR.append(overlapUnionSDR)
                else:
                    distinctnessConfusionUnionSDR.append(overlapUnionSDR)
    self._mmData['overlap'] = overlapMatrix
    self._mmData['stabilityConfusion'] = stabilityConfusionUnionSDR
    self._mmData['distinctnessConfusion'] = distinctnessConfusionUnionSDR
    self._sequenceRepresentationDataStale = False