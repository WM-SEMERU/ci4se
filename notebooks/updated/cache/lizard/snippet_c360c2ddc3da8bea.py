def sample(self, withReplacement, fraction, seed=None):
    assert fraction >= 0.0, 'Negative fraction value: %s' % fraction
    return self.mapPartitionsWithIndex(RDDSampler(withReplacement, fraction,
        seed).func, True)