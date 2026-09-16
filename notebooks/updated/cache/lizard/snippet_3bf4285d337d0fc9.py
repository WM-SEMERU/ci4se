def compute_strategy(self, grads):
    for g in grads:
        assert g.shape.is_fully_defined(), 'Shape of {} is {}!'.format(g.
            name, g.shape)
    self._shapes = [g.shape for g in grads]
    self._sizes = [g.shape.num_elements() for g in grads]
    self._total_size = sum(self._sizes)
    if self._total_size / self._num_split < 1024:
        logger.info('Skip GradientPacker due to too few gradients.')
        return False
    dtypes = set([g.dtype for g in grads])
    if len(dtypes) != 1:
        logger.info('Skip GradientPacker due to inconsistent gradient types.')
        return False
    self._grad_dtype = grads[0].dtype
    split_size = self._total_size // self._num_split
    split_size_last = self._total_size - split_size * (self._num_split - 1)
    self._split_sizes = [split_size] * (self._num_split - 1) + [split_size_last
        ]
    logger.info('Will pack {} gradients of total dimension={} into {} splits.'
        .format(len(self._sizes), self._total_size, self._num_split))
    return True