def computeEntropy(spikeTrains):
    MIN_ACTIVATION_PROB = 1e-06
    activationProb = np.mean(spikeTrains, 1)
    activationProb[activationProb < MIN_ACTIVATION_PROB] = MIN_ACTIVATION_PROB
    activationProb = activationProb / np.sum(activationProb)
    entropy = -np.dot(activationProb, np.log2(activationProb))
    return entropy