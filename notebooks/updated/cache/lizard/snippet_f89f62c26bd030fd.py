def getDefaultTMParams(self, inputSize, numInputBits):
    sampleSize = int(1.5 * numInputBits)
    if numInputBits == 20:
        activationThreshold = 18
        minThreshold = 18
    elif numInputBits == 10:
        activationThreshold = 8
        minThreshold = 8
    else:
        activationThreshold = int(numInputBits * 0.6)
        minThreshold = activationThreshold
    return {'columnCount': inputSize, 'cellsPerColumn': 16, 'learn': True,
        'learnOnOneCell': False, 'initialPermanence': 0.41,
        'connectedPermanence': 0.6, 'permanenceIncrement': 0.1,
        'permanenceDecrement': 0.03, 'minThreshold': minThreshold,
        'basalPredictedSegmentDecrement': 0.003,
        'apicalPredictedSegmentDecrement': 0.0, 'reducedBasalThreshold':
        int(activationThreshold * 0.6), 'activationThreshold':
        activationThreshold, 'sampleSize': sampleSize, 'implementation':
        'ApicalTiebreak', 'seed': self.seed}