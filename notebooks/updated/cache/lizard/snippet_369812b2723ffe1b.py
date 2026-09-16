def index_table(self, axis=None, baseline=None, prune=False):
    proportions = self.proportions(axis=axis)
    baseline = (baseline if baseline is not None else self.
        _prepare_index_baseline(axis))
    if axis == 0 and len(baseline.shape) <= 1 and self.ndim == len(self.
        get_shape()):
        baseline = baseline[:, (None)]
    indexes = proportions / baseline * 100
    return self._apply_pruning_mask(indexes) if prune else indexes