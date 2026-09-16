def get_shape_str(tensors):
    if isinstance(tensors, (list, tuple)):
        for v in tensors:
            assert isinstance(v, (tf.Tensor, tf.Variable)
                ), 'Not a tensor: {}'.format(type(v))
        shape_str = ','.join(map(lambda x: str(x.get_shape().as_list()),
            tensors))
    else:
        assert isinstance(tensors, (tf.Tensor, tf.Variable)
            ), 'Not a tensor: {}'.format(type(tensors))
        shape_str = str(tensors.get_shape().as_list())
    return shape_str