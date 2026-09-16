def _sample_as_dict(self, sample):
    if isinstance(sample, dict):
        return sample
    if isinstance(sample, (list, numpy.ndarray)):
        sample = enumerate(sample)
    return dict(sample)