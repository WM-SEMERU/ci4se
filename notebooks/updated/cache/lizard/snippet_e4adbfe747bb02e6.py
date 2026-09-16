def computeEnvelope(self):
    envelopeX = [(1 if np.abs(p) < 1 - self.envelopeWidth else np.exp(-1.0 *
        self.envelopeFactor * ((np.abs(p) - 1 + self.envelopeWidth) / self.
        envelopeWidth) ** 2)) for p in np.linspace(-1, 1, self.dimensions[0])]
    envelopeY = [(1 if np.abs(p) < 1 - self.envelopeWidth else np.exp(-1.0 *
        self.envelopeFactor * ((np.abs(p) - 1 + self.envelopeWidth) / self.
        envelopeWidth) ** 2)) for p in np.linspace(-1, 1, self.dimensions[1])]
    return np.asarray(np.outer(envelopeX, envelopeY).flatten())