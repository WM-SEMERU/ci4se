def _infer_fused_data_format(self, input_batch):
    input_shape = input_batch.get_shape().as_list()
    input_shape_len = len(input_shape)
    if input_shape_len != 4:
        raise NotImplementedError(
            'fused batch norm supports only input with 4 dimensions, it received input of dimensionality {:d}'
            .format(input_shape_len))
    axis = range(input_shape_len)[:-1] if self._axis is None else self._axis
    axis = tuple(axis)
    if axis == (0, 1, 2):
        return 'NHWC'
    elif axis == (0, 2, 3):
        return 'NCHW'
    else:
        raise ValueError(
            'Invalid axis option {}. This does not correspond to either the NHWC format (0, 1, 2) or the NCHW (0, 2, 3).'
            .format(axis))