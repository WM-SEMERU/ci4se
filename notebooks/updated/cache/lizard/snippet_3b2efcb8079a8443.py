def _build(self, inputs):
    shape_inputs = inputs.get_shape().as_list()
    rank = len(shape_inputs)
    max_dim = np.max(self._dims) + 1
    if rank < max_dim:
        raise ValueError('Rank of inputs must be at least {}.'.format(max_dim))
    full_begin = [0] * rank
    full_size = [-1] * rank
    for dim, begin, size in zip(self._dims, self._begin, self._size):
        full_begin[dim] = begin
        full_size[dim] = size
    return tf.slice(inputs, begin=full_begin, size=full_size)