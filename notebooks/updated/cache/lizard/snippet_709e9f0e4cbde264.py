def _set_shape_on_tensor(tensor, shape):
    if shape is not None:
        try:
            tensor.set_shape(shape)
        except ValueError:
            raise ValueError(
                "Requested shape does not match tensor's shape: %s vs %s" %
                (shape, tensor.get_shape()))
    elif tensor.get_shape().ndims is None:
        raise ValueError('Unknown shape on tensor: %s' % tensor)