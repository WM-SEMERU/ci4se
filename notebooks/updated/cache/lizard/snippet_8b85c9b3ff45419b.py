def normalize_weights(self, IIMax, IEMax, EIMax):
    weights = [self.weightsII, self.weightsIEL, self.weightsIER, self.
        weightsELI, self.weightsERI]
    norms = [IIMax, IEMax, IEMax, EIMax, EIMax]
    for w, n in zip(weights, norms):
        maximum = np.amax(np.abs(w))
        w /= maximum
        w *= n