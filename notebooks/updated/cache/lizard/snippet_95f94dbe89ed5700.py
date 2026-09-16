def initialize(self):
    if self._tm is None:
        params = {'columnCount': self.columnCount, 'basalInputSize': self.
            basalInputWidth, 'apicalInputSize': self.apicalInputWidth,
            'cellsPerColumn': self.cellsPerColumn, 'activationThreshold':
            self.activationThreshold, 'initialPermanence': self.
            initialPermanence, 'connectedPermanence': self.
            connectedPermanence, 'minThreshold': self.minThreshold,
            'sampleSize': self.sampleSize, 'permanenceIncrement': self.
            permanenceIncrement, 'permanenceDecrement': self.
            permanenceDecrement, 'basalPredictedSegmentDecrement': self.
            basalPredictedSegmentDecrement,
            'apicalPredictedSegmentDecrement': self.
            apicalPredictedSegmentDecrement, 'maxSynapsesPerSegment': self.
            maxSynapsesPerSegment, 'seed': self.seed}
        if self.implementation == 'ApicalTiebreakCPP':
            params['learnOnOneCell'] = self.learnOnOneCell
            params['maxSegmentsPerCell'] = self.maxSegmentsPerCell
            import htmresearch_core.experimental
            cls = htmresearch_core.experimental.ApicalTiebreakPairMemory
        elif self.implementation == 'ApicalTiebreak':
            params['reducedBasalThreshold'] = self.reducedBasalThreshold
            import htmresearch.algorithms.apical_tiebreak_temporal_memory
            cls = (htmresearch.algorithms.apical_tiebreak_temporal_memory.
                ApicalTiebreakPairMemory)
        elif self.implementation == 'ApicalDependent':
            params['reducedBasalThreshold'] = self.reducedBasalThreshold
            import htmresearch.algorithms.apical_dependent_temporal_memory
            cls = (htmresearch.algorithms.apical_dependent_temporal_memory.
                TripleMemory)
        else:
            raise ValueError('Unrecognized implementation %s' % self.
                implementation)
        self._tm = cls(**params)